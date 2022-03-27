from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="069"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc080_a".format(times, problem)) as res:
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
  N=int(input())
  A=list(map(int,input().split()))
  ans={0:0, 1:0, 2:0}
  for i in range(N):
    if A[i]%4==0: ans[2]+=1
    elif A[i]%2==0: ans[1]+=1
    else: ans[0]+=1
  if ans[1]==0 and ans[0]<=ans[2]+1 or ans[0]<=ans[2]: print('Yes')
  else: print('No')
  """ここから上にコードを記述"""

  print(test_case[__+1])