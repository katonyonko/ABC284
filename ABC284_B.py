import io
import sys

_INPUT = """\
6
4
3
1 2 3
2
20 23
10
6 10 4 1 5 9 8 6 5 1
1
1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    print(sum([A[i]%2 for i in range(N)]))