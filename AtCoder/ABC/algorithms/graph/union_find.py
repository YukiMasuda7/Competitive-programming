# UnionFind
#グラフの連結成分を管理するデータ構造
#グラフの連結(Union)と2頂点が連結かを確認する(Find)処理を高速で行う

class UnionFind:
  def __init__(self,N):
    self.N=N
    self.parent_size=[-1]*N

  def leader(self,a):
    if self.parent_size[a]<0: return a
    self.parent_size[a]=self.leader(self.parent_size[a])
    return self.parent_size[a]

  def merge(self,a,b):
    x,y=self.leader(a),self.leader(b)
    if x == y: return
    if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
    self.parent_size[x] += self.parent_size[y]
    self.parent_size[y]=x

  def same(self,a,b):
    return self.leader(a) == self.leader(b)

  def size(self,a):
    return abs(self.parent_size[self.leader(a)])

  def groups(self):
    result=[[] for _ in range(self.N)]
    for i in range(self.N):
      result[self.leader(i)].append(i)
    return [r for r in result if r!=[]]