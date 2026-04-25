# 파일이름 : 안녕,일본:성공적인 정착을 위한 경제 가이드
# 작 성 자 : 김건오(60231683)

#워홀러 정보 입력 및 환전 금액 출력
name = input("이름을 입력하세요: ")
budget_krw = int(input("현재 보유중인 원화(KRW)를 입력하세요: "))
exchange_rate = float(input("금일 엔화 환율을 입력하세요 (예:9.1): "))
flight_fee = int(input("항공권 결제 금액(KRW)를 입력하세요: "))
stay_months = int(input("일본에 체류할 예정인 개월 수를 입력하세요: "))

total_jpy = (budget_krw - flight_fee) / exchange_rate * 100 

print("-"*40)
print(f"{name}님의 워홀 초기 비용 분석입니다!")
print(f"보유원화:{budget_krw}원, 적용 환율{exchange_rate}")
print(f"항공료 제외,일본에서 사용할수 있는 총 엔화는 {total_jpy:.2f}엔입니다.")
print("-"*40)

#
expense_items = [] 
print(f"일본에서 가장 돈이 많이 들것 같은 항목 3개를 입력하세요.(월세 제외)")
for i in range(3):
  item = input(f"{i+1}번째 항목: ")
  expense_items.append(item)

expense_items.sort()
expense_items.insert(0,"월세 (고정)")
list_count = len(expense_items)

print(f"{name}님의 경제 분석 리포트")
print(f"현재 등록된 지출 관리 항목({list_count}개):{expense_items}")
print("-"*40)

#예산 등급 판정
if total_jpy >= 3000000:
  grade = "안정"
  msg = "한 달 이상 수입 없이도 안정적으로 생활하며 일자리를 고를 수 있습니다"
elif total_jpy >= 2000000:
  grade = "보통"
  msg = "평범한 수준입니다.한달 이내에 아르바이트를 구하는것이 좋습니다"
else :
  grade = "위험"
  msg = "초기 자금을 더 확보 할 것을 권장합니다"

#체류 기간 고려한 예산 등급 판정

if grade == "안정" or grade == "보통" :
  if stay_months >= 6 and budget_krw >0 :
    advide = "자금 여유가 있으니 일본을 즐기며 알바를 시작하세요"
  else : 
    advice = "초기정착이 빠를수록 여행이나 문화 활동에 시간을 쓸 수 있습니다"
else :
  advice = "시급이 높은 지역을 우선적으로 고려하거나,기숙사가 제공되는 일자리를 찾아보세요!"

print(f"종합 등급:{grade},{msg}")
print(f"가이드의 조언:{advide}")


  
    
    
    


  
  


