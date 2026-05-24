# 파일이름 : 안녕,일본:성공적인 정착을 위한 경제 가이드
# 작 성 자 : 김건오(60231683)

#워홀러 정보 입력 및 환전 금액 출력
name = input("이름을 입력하세요: ")
budget_krw = int(input("현재 보유중인 원화(KRW)를 입력하세요: "))
exchange_rate = float(input("금일 엔화 환율을 입력하세요 (예:9.1): "))
flight_fee = int(input("항공권 결제 금액(KRW)를 입력하세요: "))
stay_months = int(input("일본에 체류할 예정인 개월 수를 입력하세요: "))


total_jpy = (budget_krw - flight_fee) / exchange_rate

visa_fee = 150000
total_jpy -= visa_fee

print("-"*40)
print(f"{name}님의 워홀 초기 비용 분석입니다!")
print(f"보유원화:{budget_krw}원, 적용 환율{exchange_rate}")
print(f"항공료&비자 제외,일본에서 사용할수 있는 총 엔화는 {total_jpy:.0f}엔입니다.")
print("-"*40)

#지출 계산 카테고리
expense_items = [] 
print(f"월세를 제외한 일본에서 가장 돈이 많이 들것 같은 항목 3개를 입력하세요.")
for i in range(3):
  item = input(f"{i+1}번째 항목: ")
  if item == " " :
    print("공백은 입력 할수 없습니다.다시 입력해주세요")
    continue
    
  expense_items.append(item)

expense_items.sort()
expense_items.insert(0,"월세")
list_count = len(expense_items)

print(f"{name}님의 경제 분석 리포트")
print(f"현재 등록된 지출 관리 항목({list_count}개):{expense_items}")
print("-"*40)

#예산 등급 판정 및 조언
if total_jpy >= 300000:
  grade = "안정"
  msg = "한 달 이상 수입 없이도 안정적으로 생활하며 일자리를 고를 수 있습니다"
elif total_jpy >= 200000:
  grade = "보통"
  msg = "평범한 수준입니다.한달 이내에 아르바이트를 구하는것이 좋습니다"
else :
  grade = "위험"
  msg = "초기 자금을 더 확보 할 것을 권장합니다"


#체류 기간 고려한 예산 등급 판정 및 조언
if grade == "안정" or grade == "보통" :
  if stay_months >= 6 and budget_krw >0 :
    advice = "자금 여유가 있으니 일본을 즐기며 알바를 시작하세요"
  else : 
    advice = "초기정착이 빠를수록 여행이나 문화 활동에 시간을 쓸 수 있습니다"
else :
  advice = "시급이 높은 지역을 우선적으로 고려하거나,기숙사가 제공되는 일자리를 찾아보세요!"

print(f"종합 등급:{grade},{msg}")
print(f"가이드의 조언:{advice}")
print("-"*40)

#3차 과제.
#전역 변수 선언
hourly_wage = 0
working_hours_per_week = 0

#함수1 알바 근무 정보 입력
def input_job_conditions():
  global hourly_wage, working_hours_per_week
  print("일본 현지 아르바이트 정보을 입력합니다.")
  hourly_wage = int(input("알바 시급(엔)을 입력하세요."))
  working_hours_per_week = int(input("주일당 근무 시간을 입력하세요."))
  print("아르바이트 정보가 성공적으로 등록 되었습니다.")

#함수2 예상 월급 계산
def calculate_monthly_income():
  monthly_income = hourly_wage * working_hours_per_week * 4
  return monthly_income

#함수3 목표 저축액 가능여부 분석
def analyze_saving_possibillity(calculated_income):
  print(f"\n{'='*10}{name}님의 현지 월급 및 저축 분석{'='*10}")
  print(f"예상 월수입: 약{calculated_income:,.0f}엔")

  goal_saving = int(input("한 달에 저축하고 싶은 목표 금액(엔)을 입력하세요: "))

  #일본 워홀러 평균 최소 생활비(야칭 포함) 120000엔 설정
  living_cost = 120000
  available_money = calculated_income - living_cost

  if available_money >= goal_saving:
    print(f"저축 가능합니다! 생활비({living_cost:,}엔)와 목표 저축액({goal_saving:,}엔)을 모두 충당할 수 있습니다.") 

  else :
    shortage = goal_saving - available_money
    print(f"보완이 필요합니다. 현재 계획으로는 목표액보다 약{shortage:,.0f}엔이 부족합니다.")

  print("="*50)

print("\n초기 정착 분석이 완료되었습니다.이어서 현지 수입/저축 관리를 시작합니다")

while True:
  print("\n" + "="*15 + "워홀 현지 경제 시뮬레이터" + "="*15)
  print("1. 알바 정보 입력")
  print("2. 예상 월수입 확인")
  print("3. 목표 적축액 달성 분석")
  print("4. 종료")
  print("="*55)

  menu_choice = input("원하는 메뉴 번호를 선택하세요: ").strip()

  if menu_choice == "1":
    input_job_conditions()

  elif menu_choice == "2":
    if hourly_wage == 0:
      print("[경고] 1번 메뉴에서 알바 정보를 먼저 입력해주세요.")
      continue

    my_monthly_income = calculate_monthly_income()
    print(f"\n {name}님의 예상 월수입은 총[{my_monthly_income:,.0f}엔]입니다.")

  elif menu_choice == "3":
    if hourly_wage ==0:
      print("[경고] 1번 메뉴에서 알바 정보를 먼저 입력해주세요.")
      continue

    my_monthly_income = calculate_monthly_income()
    analyze_saving_possibillity(my_monthly_income)

  elif menu_choice =="4":
    print("프로그램을 종료합니다")
    break

  else:
    print("올바른 번호(1~4)를 입력해주세요. ")


    
      




  
    
    
    


  
  


