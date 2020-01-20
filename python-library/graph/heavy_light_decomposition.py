from collections import deque
import sys
input = sys.stdin.buffer.readline


class SegmentTree:
    """Segment Tree (Point Update & Range Query)

    Query
        1. update(i, val): update i-th value to val
        2. query(low, high): find f(value) in [low, high)

    Complexity
        time complexity: O(log n)
        space complexity: O(n)
    """

    def __init__(self, N, f, default):
        self.N = 1 << (N-1).bit_length()
        self.default = default
        self.f = f
        self.segtree = [self.default] * ((self.N << 1) - 1)

    @classmethod
    def create_from_array(cls, arr, f, default):
        N = len(arr)
        self = cls(N, f, default)
        for i in range(N):
            self.segtree[self.N - 1 + i] = arr[i]

        for i in reversed(range(self.N - 1)):
            self.segtree[i] = self.f(
                self.segtree[(i << 1) + 1], self.segtree[(i << 1) + 2])
        return self

    def update(self, i, val):
        i += self.N - 1
        self.segtree[i] = val
        while i > 0:
            i = (i - 1) >> 1
            self.segtree[i] = self.f(
                self.segtree[(i << 1) + 1], self.segtree[(i << 1) + 2])

    def __getitem__(self, k):
        return self.segtree[self.N - 1 + k]

    def query(self, low, high):
        # query [l, r)
        low, high = low + self.N, high + self.N
        ret = self.default
        while low < high:
            if low & 1:
                ret = self.f(ret, self.segtree[low-1])
                low += 1
            if high & 1:
                high -= 1
                ret = self.f(ret, self.segtree[high-1])
            low, high = low >> 1, high >> 1
        return ret


class Edge:
    def __init__(self, dst, weight):
        self.dst, self.weight = dst, weight

    def __lt__(self, e):
        return self.weight > e.weight


class Graph:
    def __init__(self, V):
        self.V = V
        self.E = [[] for _ in range(V)]

    def add_edge(self, src, dst, weight):
        self.E[src].append(Edge(dst, weight))


class HeavyLightDecomposition:
    def __init__(self, g: Graph, root: int = 0,
                 need_subtree: bool = False) -> None:
        self.g = g
        self.vid, self.head = [-1] * g.V, [0] * g.V
        self.heavy, self.parent = [-1] * g.V, [0] * g.V
        self.dfs(root)
        if not need_subtree:
            self.bfs(root)
        else:
            self.tail = [0] * g.V
            self.dfs2(root)

    def dfs(self, root=-1):
        stack = [(root, -1, False)]
        sub, max_sub = [1] * self.g.V, [(0, -1)] * self.g.V
        while stack:
            v, par, flag = stack.pop()
            if not flag:
                self.parent[v] = par
                stack.append((v, par, True))
                stack.extend((e.dst, v, False)
                             for e in self.g.E[v] if e.dst != par)
            else:
                if par != -1:
                    sub[par] += sub[v]
                    max_sub[par] = max(max_sub[par], (sub[v], v))
                self.heavy[v] = max_sub[v][1]

    def bfs(self, root=0):
        k, que = 0, deque([root])
        while que:
            r = v = que.popleft()
            while v != -1:
                self.vid[v], self.head[v] = k, r
                k += 1
                for e in self.g.E[v]:
                    if e.dst != self.parent[v] and e.dst != self.heavy[v]:
                        que.append(e.dst)
                v = self.heavy[v]

    def dfs2(self, root: int = 0) -> None:
        stack = [(root, 0)]
        k = 0
        while stack:
            v, state = stack.pop()
            if state == 0:
                u = v
                while u != -1:
                    self.vid[u] = k
                    k += 1
                    self.head[u] = v
                    stack.append((u, 1))
                    u = self.heavy[u]
            elif state == 1:
                stack.append((v, 2))
                for child in self.g.E[v]:
                    if child.dst not in [self.parent[v], self.heavy[v]]:
                        stack.append((child.dst, 0))
            else:
                self.tail[v] = k

    def lca(self, u, v):
        while self.head[u] != self.head[v]:
            if self.vid[u] > self.vid[v]:
                u, v = v, u
            v = self.parent[self.head[v]]
        else:
            if self.vid[u] > self.vid[v]:
                u, v = v, u
        return u

    def query_path(self, u, v, one, query, merge, edge: bool = False):
        # u, v の間のパスに対するクエリを計算する
        # one は単位元、query は列に対するクエリ、merge はマージする演算
        left = right = one
        while True:
            if self.vid[u] > self.vid[v]:
                u, v = v, u
                left, right = right, left
            if self.head[u] == self.head[v]:
                break
            left = merge(query(self.vid[self.head[v]], self.vid[v] + 1), left)
            v = self.parent[self.head[v]]
        return merge(merge(query(self.vid[u] + edge, self.vid[v] + 1),
                           left), right)


def yosupo():
    # https://judge.yosupo.jp/problem/lca
    N, Q = map(int, input().split())
    graph = Graph(N)
    for i, p in enumerate(map(int, input().split())):
        graph.add_edge(p, i+1, 1)
    hld = HeavyLightDecomposition(graph)
    ans = [hld.lca(*map(int, input().split())) for _ in range(Q)]
    print(*ans, sep="\n")


def yosupo2():
    # https://judge.yosupo.jp/problem/vertex_add_path_sum
    import operator
    N, Q = map(int, input().split())
    weights = [int(x) for x in input().split()]
    graph = Graph(N)
    for _ in range(N-1):
        u, v = map(int, input().split())
        graph.add_edge(u, v, 1)
        graph.add_edge(v, u, 1)
    hld = HeavyLightDecomposition(graph)
    new_weights = [0] * N
    for i in range(N):
        new_weights[hld.vid[i]] = weights[i]
    rsq = SegmentTree.create_from_array(new_weights, operator.add, 0)

    ans = []
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 0:
            rsq.update(hld.vid[a], rsq[hld.vid[a]] + b)
        else:
            ans.append(hld.query_path(a, b, 0, rsq.query, operator.add))
    print(*ans, sep="\n")


def yosupo3():
    # https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    import operator
    N, Q = map(int, input().split())
    weights = [int(x) for x in input().split()]
    graph = Graph(N)
    for i, v in enumerate(map(int, input().split())):
        graph.add_edge(i+1, v, 1)
        graph.add_edge(v, i+1, 1)
    hld = HeavyLightDecomposition(graph, 0, True)
    new_weights = [0] * N
    for i in range(N):
        new_weights[hld.vid[i]] = weights[i]
    rsq = SegmentTree.create_from_array(new_weights, operator.add, 0)

    ans = []
    for _ in range(Q):
        query = [int(x) for x in input().split()]
        if query[0] == 0:
            a, b = query[1:]
            rsq.update(hld.vid[a], rsq[hld.vid[a]] + b)
        else:
            u = query[1]
            ans.append(rsq.query(hld.vid[u], hld.tail[u]))
    print(*ans, sep="\n")


if __name__ == "__main__":
    # yosupo()
    # yosupo2()
    yosupo3()
