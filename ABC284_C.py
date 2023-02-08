import io
import sys

_INPUT = """\
6
5 3
1 2
1 3
4 5
5 0
4 6
1 2
1 3
1 4
2 3
2 4
3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  used=[False]*N
  def dfs(G,r=0):
    parent=[-1]*len(G)
    st=[]
    st.append(r)
    while st:
        x=st.pop()
        if used[x]==True:
            continue
        used[x]=True
        for v in G[x]:
            if v==parent[x]:
                continue
            parent[v]=x
            st.append(v)
  G=[[] for _ in range(N)]
  for i in range(M):
    u,v=map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)
  ans=0
  for i in range(N):
    if used[i]==True: continue
    dfs(G,i)
    ans+=1
  print(ans)