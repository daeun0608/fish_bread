#주문, 관리자, 종료
stock={
    "팥붕어빵":10,
    "슈크림붕어빵":8,
    "초코붕어빵":5,
}

sales={
    "팥붕어빵":0,
    "슈크림붕어빵":0,
    "초코붕어빵":0,
}

def order_bread():
    while True:
        bread_type=input("주문할 붕어빵 선택 (팥붕어빵,슈크림붕어빵,초코붕어빵)\n만약 뒤로가길 원한다면 '뒤로가기'룰 압력하세요. --> ")

        if(bread_type=='뒤로가기'):
            break

        if bread_type in stock:     #in으로 확인하면 key만 확인한다
            bread_count=int(input(f'{bread_type} 몇 개를 구입할까요? --> '))
            if stock[bread_type]>=bread_count:
                stock[bread_type]-=bread_count
                sales[bread_type]+=bread_count
                print(f'{bread_type} {bread_count}개가 판매되었습니다.')
            else:
                print(f'미안해, 지금 주문가능한 빵의 개수는 {stock[bread_type]}개야.')
        else:
            print('잘못된 입력입니다, 주문을 다시 해주세요.')

#붗어빵 admin 기능
def admin_mode():
    while True:
        bread_type = input("추가할 붕어빵 선택 (팥붕어빵,슈크림붕어빵,초코붕어빵)\n관리자 모드를 종료하려면 '뒤로가기' 혹은 '종료'룰 압력하세요. --> ")

        if (bread_type == '뒤로가기' or bread_type=='종료'):
            break

        if bread_type in stock:  # in으로 확인하면 key만 확인한다
            bread_count = int(input(f'{bread_type} 몇 개를 추가할까요? --> '))
            stock[bread_type] += bread_count
            print(f'{bread_type}의 재고는 {stock[bread_type]}입니다.')
        else:
            print('잘못된 입력입니다, 다시 입력하세요.')

while True:
    mode=input("원하는 모드를 선택하세요(주문, 관리자, 종료) : ")

    if mode=='종료' :
        print("시스템이 종료되었습니다.")
        break
    elif mode=='주문' :
        order_bread()
    elif mode=='관리자' :
        admin_mode()
    else :
        print("잘못된 입력입니다. 다시 입력하세요.")
    