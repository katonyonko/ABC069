from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="069"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc080_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  H,W=map(int,input().split())
  N=int(input())
  A=list(map(int,input().split()))
  ans=[[0]*W for _ in range(H)]
  r,c=0,0
  for i in range(N):
    for k in range(A[i]):
      ans[r][c]=i+1
      if r%2==0 and c<W-1: c+=1
      elif r%2==0 and c==W-1: r+=1
      elif r%2==1 and c>0: c-=1
      else: r+=1
  for i in range(H):
    print(*ans[i])
  """ここから上にコードを記述"""

  print(test_case[__+1])