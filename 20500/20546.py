money = int(input())  # 초기 자금
StockPrices = list(map(int, input().split())) # 14일간 주식 가격
    
# 준현 BNK 전략
jh_cash = money # 준현의 현금
jh_stock = 0 # 준현의 주식 보유량

for StockPrice in StockPrices:
    if jh_cash >= StockPrice:   #남은 돈으로 주식을 살 수 있다면
        jh_stock += jh_cash // StockPrice  # 최대한 많은 주식 구매
        jh_cash %= StockPrice # 남은돈 업데이트

# 성민 TIMING 전략
sm_cash = money # 성민의 현금
sm_stock = 0  # 성민의 주식 보유량

for i in range(2, len(StockPrices)):   # 3일째부터 확인
    # 3일 연속 상승
    if StockPrices[i-2] < StockPrices[i-1] < StockPrices[i]:
        sm_cash += sm_stock * StockPrices[i] # 모든 주식 판매 ( 주식 수 x 현재 주식 가격 = 현금으로 전환)
        sm_stock = 0 # 보유주식 초기화
    # 3일 연속 하락
    elif StockPrices[i-2] > StockPrices[i-1] > StockPrices[i]:
        sm_stock += sm_cash // StockPrices[i] # 현재 현금으로 살 수 있는 최대 주식 수
        sm_cash %= StockPrices[i]   # 주식 구매 후 남은 잔액

jh_total = jh_cash + jh_stock * StockPrices[-1] #준현의 총 자산
sm_total = sm_cash + sm_stock * StockPrices[-1]  # 성민의 총 자산

# 결과 출력
if jh_total > sm_total:
    print("BNP")
elif jh_total < sm_total:
    print("TIMING")
else:
    print("SAMESAME")
