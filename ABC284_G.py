import io
import sys

_INPUT = """\
6
4 100000000
7 1000000000
2023 998244353
100000 353442899
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  sq=[1]
  for i in range(N): sq.append(sq[-1]*N%M)
  fac=[1]
  for i in range(N): fac.append(fac[-1]*(N-i-1)%M)
  ans=0
  for i in range(N):
    ans+=fac[i]*(i+1)*i//2*sq[N-i-1]
    ans%=M
  print(ans*N%M)