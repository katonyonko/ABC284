import io
import sys

_INPUT = """\
6
4 2
1 2
2 3
4 6
1 2
1 3
1 4
2 3
2 4
3 4
8 21
2 6
1 3
5 6
3 8
3 6
4 7
4 6
3 4
1 5
2 4
1 2
2 7
1 4
3 5
2 5
2 3
4 5
3 7
6 7
5 7
2 8
4 3
3 2
1 2
3 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  def dfs(G,r=0):
    global ans
    st=[]
    st.append((r,0))
    st.append((r,1))
    while st:
      x,y=st.pop()
      if y==0:
        used[x]=False
      else:
        used[x]=True
        for v in G[x]:
          if used[v]==True: continue
          ans+=1
          if ans>10**6: ans=10**6; return
          st.append((v,0))
          st.append((v,1))

  N,M=map(int,input().split())
  G=[[] for _ in range(N)]
  for i in range(M):
    u,v=map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)
  used=[False]*N
  ans=1
  dfs(G,0)
  print(ans)