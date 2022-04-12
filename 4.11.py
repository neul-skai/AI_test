#04.11 - 이하늘
import re
import pandas as pd
from tqdm import tqdm
from konlpy.tag import Okt
from pykospacing import Spacing
from collections import Counter

df = pd.read_table('E:/가천대/AI 활용대회/파이썬/실습용자료.txt',sep='|',encoding = 'euc-kr')
kordata = df.loc[:,['text_obj', 'text_mthd', 'text_deal']]
df1=df
kordf = df1['text_obj'] +' '+ df1['text_mthd'] +' '+ df1['text_deal'] 
df1['kor']=kordf.astype(str)

#한국어만 추출하기
def extract_word(text):
    hangul = re.compile('[^가-힣]') 
    result = hangul.sub(' ', text) 
    return result

lix = df['kor'].values.tolist() #x만 출력해서 리스트로 변환
type(lix)

s = [] #빈리스트

for i in range(0,len(lix)):
    s.append(extract_word(lix[i]))
s[1]

#빈칸 없애기
def remove_blank(x):
    return x.replace(' ', '')

for i in range(0,len(s)):
    s[i] = remove_blank(s[i])
s[1]

#띄어쓰기하기
spacing=Spacing()
for i in range(0,len(s)):
    s[i] = spacing(s[i])