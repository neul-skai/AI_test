data="치킨전문점에서|고객의주문에의해|치킨판매|산업공구|다른 소매업자에게|철물 수공구|절에서|신도을 대상으로|불교단체운영|영업장에서|고객요구로|자동차튜닝|실내포장마차에서|접객시설을 갖추고|소주,맥주제공|철,아크릴,포맥스|스크린인쇄|명판"

#okt (open korea text) (구 Twitter)
from konlpy.tag import Okt
okt=Okt()
print(okt.morphs(data))     #morphs: 형태소 추출    #가장 기본적이고 단순한 형태
print(okt.pos(data))        #pos: 품사 태깅
print(okt.nouns(data))      #nouns: 명사추출     #? 포맥스 -> 포/ 맥스로 분리됨 - 어떻게 설정할 수 있지?

#꼬꼬마(kkma)
from konlpy.tag import Kkma
kkma=Kkma()
print(kkma.morphs(data))     #morphs: 형태소 추출
print(kkma.pos(data))        #pos: 품사 태깅
print(kkma.nouns(data))      #nouns: 명사추출  #치킨/ 치킨전문점/ 전문점 <- 구체적으로 나뉨 다만 중복이 많아 고려 필요

#메캅(Mecab) -  버려   / 상대적으로 빠르다고 함
from konlpy.tag import Mecab
mecab=Mecab()

#코모란(Komoran)                #불교를 싫어하는 것으로 추정됨 / 인식하지 못하는 문장이 있음.
from konlpy.tag import Komoran
komo=Komoran()
print(komo.morphs(data))     #morphs: 형태소 추출
print(komo.pos(data))        #pos: 품사 태깅
print(komo.nouns(data))      #nouns: 명사추출

#한나눔(Hannanum)               # 개쓰레기임 / 왜만든건지 1도 이해할 수 없음
from konlpy.tag import Hannanum
hanna=Hannanum()
print(hanna.morphs(data))     #morphs: 형태소 추출
print(hanna.pos(data))        #pos: 품사 태깅
print(hanna.nouns(data))      #nouns: 명사추출 
