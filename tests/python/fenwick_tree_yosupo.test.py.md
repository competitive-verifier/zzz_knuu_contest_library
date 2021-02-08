---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verify-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import sys\nfrom python_library.data_structures.fenwick_tree import FenwickTree\n\
    \ninput = sys.stdin.buffer.readline\n\n\ndef main() -> None:\n    _, Q = map(int,\
    \ input().split())\n    fwt = FenwickTree([int(x) for x in input().split()])\n\
    \    ans = []\n    for _ in range(Q):\n        type_, l, r = map(int, input().split())\n\
    \        if type_ == 0:\n            fwt.add(l, r)\n        else:\n          \
    \  ans.append(fwt.query(l - 1, r - 1))\n    print(*ans, sep=\"\\n\")\n\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: tests/python/fenwick_tree_yosupo.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: tests/python/fenwick_tree_yosupo.test.py
layout: document
redirect_from:
- /verify/tests/python/fenwick_tree_yosupo.test.py
- /verify/tests/python/fenwick_tree_yosupo.test.py.html
title: tests/python/fenwick_tree_yosupo.test.py
---