##### 암호문 빈도계산 #####
freq_dict={}
with open(r'cipher.txt', 'rb') as f:
    cnt=0
    while f.read(1):
        f.seek(-1,1)
        c=f.read(1).decode()
        # 알파벳만 해시테이블에 저장
        if c.isalpha()==False:
            continue
        # 없을 경우 새로 만듬
        if c not in freq_dict:
            freq_dict[c]=1
        # 있을 경우 카운트 증가
        else:
            freq_dict[c]+=1
        cnt+=1
    # 전체 비율 계산 (소수점 2째자리까지 표현)
    for key in freq_dict:
        freq_dict[key]=round(freq_dict[key]/cnt*100,2)
    # value를 기준으로 소팅
    sorted_freq = sorted(freq_dict.items(),key = lambda x : x[1], reverse=True)
# 전체 해시를 출력
for ele in sorted_freq:
    print("\"",ele[0],"\" : ",ele[1],sep='')