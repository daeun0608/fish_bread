from fishbread_model import BreadShop

shop=BreadShop()

while True:
    mode=input("원하는 모드를 선택하세요(주문, 관리자, 종료) : ")

    if mode=='종료' :
        shop.calculate_sales()           #임시용
        print("시스템이 종료되었습니다.")
        break
    elif mode=='주문' :
        shop.order_bread()
    elif mode=='관리자' :
        shop.admin_mode()
    else :
        print("잘못된 입력입니다. 다시 입력하세요.")
    