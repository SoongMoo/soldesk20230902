import random
qty =  int(input("구매수량을 입력하세요. : "))
lotto = []
cnt = 1
while cnt <= qty:
    i = 1
    while i <= 45:
        lotto.append(i) 
        i += 1
    size = len(lotto) # 45
    y = 1
    while y <= 6:
        size -= 1
        idx = random.randint(0, size)
        lottoNum = lotto.pop(idx)  
        print(lottoNum, end=", ")
        y += 1
    lotto.clear() # 빈리스트를 만들어 주기
    print()
    cnt += 1