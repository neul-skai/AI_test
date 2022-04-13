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

#1단계-한국어만 추출하기
def extract_word(text):
    hangul = re.compile('[^가-힣]') 
    result = hangul.sub(' ', text) 
    return result

lix = df1['kor'].values.tolist() #x만 출력해서 리스트로 변환
type(lix)


s = [] #빈리스트

for i in range(0,len(lix)):
    s.append(extract_word(lix[i]))
s[1]

#2단계-빈칸 없애기
def remove_blank(x):
    return x.replace(' ', '')

for i in range(0,len(s)):
    s[i] = remove_blank(s[i])
s[1]

#3단계 - 띄어쓰기하기
spacing=Spacing()
for i in range(0,1000):
    s[i] = spacing(s[i])

s[1]

##4.13
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np

df['x'] = s
dset=pd.DataFrame(df)

#랜덤 추출 - 10,000개
ds = dset.sample(n = 10000, random_state=42)
len(ds)

x = ds['x']
y= ds[['digit_1','digit_2','digit_3']]
y1 = ds['digit_1']

#학습/테스트 데이터셋 분할
x_train, x_test, y_train, y_test = train_test_split(x,y1, test_size=0.2, random_state=42)
len(x_test)
len(x_train)
len(y_test)
len(y_train)

#데이터 전처리(벡터화)
vectorizer = CountVectorizer()
tfid = TfidfTransformer()

x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.fit_transform(x_test)

x_train_tfid = tfid.fit_transform(x_train_vec)
x_test_tfid = tfid.fit_transform(x_test_vec)

x_test_tfid.toarray()

#다중분류 나이브 베이브 + 그리드 서치로 모델 학습
nb = MultinomialNB()
param_grid = [{'alpha':np.linspace(0.01,1,100)}]
gs = GridSearchCV(estimator=nb, param_grid=param_grid, scoring='accuracy',cv=5,n_jobs=-1)
gs.fit(x_train_tfid,y_train)

#학습결과
print('베스트 하이퍼 파라미터: {0}'.format(gs.best_params_))
print('베스트 하이퍼 파라미터 일 때 정확도: {0:.2f}'.format(gs.best_score_))

# 최적화 모델 추출
model = gs.best_estimator_

# 테스트세트 정확도 출력
score = model.score(x_test_tfid, y_test)
print('테스트세트에서의 정확도: {0:.2f}'.format(score))

# 테스트세트 예측 결과 샘플 출력
predicted_y = model.predict(X_test_tfid)
for i in range(10):
    print('실제 값: {0}, 예측 값: {1}'.format(labels[y_test[i]], labels[predicted_y[i]]))

import tensorflow as tf
tf.__version__

import scipy
scipy.__version__

import numpy
numpy.__version__
