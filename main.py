# 파일이름 : 안녕,일본:성공적인 정착을 위한 경제 가이드
# 작 성 자 : 김건오(60231683)

name = input("이름을 입력하세요: ")
budget_krw = int(input("현재 보유중인 원화(KRW)를 입력하세요: "))
exchange_rate = float(input("금일 엔화 환율을 입력하세요 (예:9.1): "))
flight_fee = int(input("항공권 결제 금액(KRW)를 입력하세요: "))
stay_months = int(input("일본에 체류할 예정인 개월 수를 입력하세요: "))

total_jpy = (budget - flight_fee) / exchange_rate * 100 

print(f"{name}님의 워홀 초기 비용 분석입니다!")
print(f"보유원화:{budget}원, 적용 환율{exchange_rate}")
print(f"항공료 제외,일본에서 사용할수 있는 총 엔화는 {total_jpy}엔입니다.")
