#주문, 관리자, 종료

while True:
    mode=input("원하는 모드를 선택하세요(주문, 관리자, 종료) : ")
    
    if mode=='주문' :
        order_bread()
    elif mode=='관리자' :
        admin_mode()
    elif mode=='종료' :
        print("시스템이 종료되었습니다.")
        break
    else :
        print("잘못된 입력입니다. 다시 입력하세요.")
    