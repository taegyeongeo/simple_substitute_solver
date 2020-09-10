from math import log10
class ngram_score(object):
    # n-gram 빈도수가 계산된 파일을 입력 받음, 'ABCD 234324' 형식으로 되어있음
    def __init__(self,ngramfile,sep=' '):
        # n-gram 파일을 딕셔너리로 불러옴
        self.ngrams = {}
        f = open(ngramfile, 'r')
        for line in f.readlines():
            key,count = line.split(sep)
            self.ngrams[key] = int(count)
        f.close()
        # n-gram에서 n을 저장
        self.L = len(key)
        # 개별 항목 빈도수를 합한 total count를 저장
        self.N = sum(self.ngrams.values())
        # item 개별 빈도수를 총 total count로 나누고 이를 상용로그로 치환
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)
        
        self.floor = log10(0.01/self.N)

    def score(self,text):
        score = 0
        # 입력된 텍스트의 모든 n-gram(길이가 n인 sub-string)에 대해 score 계산
        for i in range(len(text)-self.L+1): 
            key = text[i:i+self.L]
            # n-gram파일에 현재 텍스트의 substring이 있으면 스코어에 더해줌 
            if key in self.ngrams:
                score += self.ngrams[key]
            # 그렇지 않으면 가장 낮은 값을 더해줌
            else:
                score += self.floor
        return score
       