import io
import sys

_INPUT = """\
6
3
abcbac
4
abababab
3
agccga
4
atcodeer
3
abccba
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def z_algorithm(s):
    N = len(s)
    Z_alg = [0]*N

    Z_alg[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and s[j] == s[i+j]:
            j += 1
        Z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k + Z_alg[k]<j:
            Z_alg[i+k] = Z_alg[k]
            k += 1
        i += k
        j -= k
    return Z_alg

  N=int(input())
  T=input()
  x=z_algorithm(T+T[::-1])
  y=z_algorithm(T[::-1]+T)
  ans=-1
  if T[:N]==T[N:2*N][::-1]: ans=0
  for i in range(1,N):
    if x[3*N-i]>=i and y[2*N+i]>=N-i:
      ans=i
      break
  if ans!=-1:
    print(T[ans:ans+N][::-1])
  print(ans)