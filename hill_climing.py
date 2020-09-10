import random
import re
from ngram_score import ngram_score
from pycipher import SimpleSubstitution as SimpleSub
##### 힐 클라이밍 계산 #####

# 4글자기준(최적이라고 함) 빈도수로 fitness 계산한다
fitness = ngram_score('quadgrams.txt')
# 암호문을 읽고 전처리하여 'ABCD...' 형태로 변형
f=open(r'cipher.txt', 'r')
contents=f.read()
ctext = re.sub("[^A-Z]+", "",contents)
# 초기 키값 설정, 키 값은 알파벳 순서대로 1대1 매핑됨
maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# 초기 스코어 최저로 설정
maxscore = -99e9
# 이전값 저장, 스코어의 향상이 없을 경우 되돌아 가기 위함
parentscore,parentkey = maxscore,maxkey[:]

# 반복 횟수
i = 0
while 1:
    i = i+1
    random.shuffle(parentkey)
    deciphered = SimpleSub(parentkey).decipher(ctext)
    parentscore = fitness.score(deciphered)
    count = 0
    while count < 1000:
        # 랜덤으로 두 알파벳을 swap한 키 후보군을 만듬
        a = random.randint(0,25)
        b = random.randint(0,25)
        child = parentkey[:]
        child[a],child[b] = child[b],child[a]
        # 암호문을 키 후보군으로 decryption
        deciphered = SimpleSub(child).decipher(ctext)
        # 4-gram으로 fitness 계산
        score = fitness.score(deciphered)
        # swap후 계산한 스코어가 더 좋을 경우 key를 업데이트 함
        if score > parentscore:
            parentscore = score
            parentkey = child[:]
            count = 0
        count = count+1
    # 위 과정을 1000번 반복, parent엔 1000 반복 내에서 optimal한 key와 key에 대한 스코어가 존재

    # 업데이트한 스코어가 이전 스코어보다 높을 경우
    if parentscore>maxscore:
        # 최대치를 현재 스코어로 갱신한 후 다음 루프를 돈다.
        maxscore,maxkey = parentscore,parentkey[:]
        print(f'[{i}번째 루프] 현재 스코어 : {maxscore}')
        # 현재 키값(지금까지는 optimal)으로 암호문을 치환
        ss = SimpleSub(maxkey)
        print(f'현재 키 값 : {maxkey}')
        print(f'평문 by 현재 키 값 : {ss.decipher(ctext)}')