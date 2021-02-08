---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from copy import deepcopy\nfrom typing import List\n\n\ndef pascalsTriangle(n:\
    \ int) -> List[List[int]]:\n    assert n >= 0\n    psTri = [[0]*n for _ in range(n)]\n\
    \    for i in range(n):\n        psTri[i][0] = 1\n        psTri[i][i] = 1\n  \
    \      for j in range(1, i):\n            psTri[i][j] = psTri[i-1][j-1] + psTri[i-1][j]\n\
    \    return deepcopy(psTri)\n"
  dependsOn: []
  isVerificationFile: false
  path: python_library_typed/math/pascalsTriangle.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: python_library_typed/math/pascalsTriangle.py
layout: document
redirect_from:
- /library/python_library_typed/math/pascalsTriangle.py
- /library/python_library_typed/math/pascalsTriangle.py.html
title: python_library_typed/math/pascalsTriangle.py
---