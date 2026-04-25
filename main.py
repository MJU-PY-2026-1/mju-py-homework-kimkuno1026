# 파일이름 : 안녕,일본:성공적인 정착을 위한 경제 가이드
# 작 성 자 : 김건오(60231683)

name = input("이름을 입력하세요: ")
budget_krw = int(input("현재 보유중인 원화(KRW)를 입력하세요: "))
exchange_rate = float(input("금일 엔화 환율을 입력하세요 (예:9.1): "))
flight_fee = int(input("항공권 결제 금액(KRW)를 입력하세요: "))
stay_months = int(input("일본에 체류할 예정인 개월 수를 입력하세요: "))

total_jpy = (budget_krw - flight_fee) / exchange_rate * 100 

print(f"{name}님의 워홀 초기 비용 분석입니다!")
print(f"보유원화:{budget_krw}원, 적용 환율{exchange_rate}")
print(f"항공료 제외,일본에서 사용할수 있는 총 엔화는 {total_jpy}엔입니다.")

expense_items = []
print(f"일본에서 가장 돈이 많이 들것 같은 항목 3개를 입력하세요.(월세 제외)")
for i in range(3):
  item = input(f"i+1}번째 항목: ")
  expense_items.append(item)
  
expense_item.insert(0,"월세 (고정)")
list_count = len(expense_items)
expense_items.sort()

print(f"{name}님의 경제 분석 리포트")
print(f"현재 등록된 지출 관리 항목({list_count}개):{expense_items}")


