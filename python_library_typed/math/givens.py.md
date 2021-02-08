---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - http://www.slideshare.net/tmaehara/ss-18244588
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, TypeVar, Tuple\n\ndef givens(A: List[List[float]],\
    \ b: List[float]) -> List[float]:\n    \"\"\" solve linear equation\n        cf.\
    \ http://www.slideshare.net/tmaehara/ss-18244588\n        complexity: O(n^3)\n\
    \        used in kupc2012_C\n    \"\"\"\n    def mkrot(x: float, y: float) ->\
    \ Tuple[float, float]:\n        r = pow(x ** 2 + y ** 2, 0.5)\n        return\
    \ x/r, y/r\n\n    def rot(x: float, y: float, c: float, s: float) -> Tuple[float,\
    \ float]:\n        return c*x+s*y, -s*x+c*y\n\n    n = len(b)\n    for i in range(n):\n\
    \        for j in range(i+1, n):\n            c, s = mkrot(A[i][i], A[j][i])\n\
    \            b[i], b[j] = rot(b[i], b[j], c, s)\n            for k in range(i,\
    \ n):\n                A[i][k], A[j][k] = rot(A[i][k], A[j][k], c, s)\n    for\
    \ i in reversed(range(n)):\n        for j in range(i+1, n):\n            b[i]\
    \ -= A[i][j] * b[j]\n        b[i] /= A[i][i]\n    return b\n"
  dependsOn: []
  isVerificationFile: false
  path: python_library_typed/math/givens.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: python_library_typed/math/givens.py
layout: document
redirect_from:
- /library/python_library_typed/math/givens.py
- /library/python_library_typed/math/givens.py.html
title: python_library_typed/math/givens.py
---