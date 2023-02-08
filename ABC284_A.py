import io
import sys

_INPUT = """\
6
3
Takahashi
Aoki
Snuke
4
2023
Year
New
Happy
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=[input() for _ in range(N)]
  for i in range(N):
    print(S[N-1-i])