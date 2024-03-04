#가위바위보 게임 만들기
import random
import os

cnt = 0
win = 0
life = [1]
for i in life: #for문으로 가위바위보 만들어보기
# 가위바위보 아스키 아트 출력
# 1. 사람은 는 가위, 바위, 보 중 하나를 선택한다.
    cnt += 1
    print("가위, 바위, 보 중 하나를 생각하세요")
    user_choice = int(input("(1. 가위 /2. 바위 /3. 보) : "))
    choice = {1:'가위', 2:'바위', 3:'보'}
    print(f"당신의 선택은...{choice[user_choice]}")

    # 2. 컴퓨터의 결과는 랜덤으로 출력한다.
    # 랜덤 함수로 결정한다.
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        print("컴퓨터는 가위를 선택했습니다.")
    elif computer_choice == 2:
        print("컴퓨터는 바위를 선택했습니다.")
    else:
        print("컴퓨터는 보를 선택했습니다.")

    # 2. 결과 출력
    if user_choice - computer_choice == 0: # 비겼을 때
        print("비겼습니다!")
    elif user_choice - computer_choice == 1 or user_choice - computer_choice == -2:#이겼을 때
        print("당신이 이겼습니다.")
        win += 1
    else: #졌을 때
        print("당신이 졌습니다.")

    user_wants_continue = 0
    #3. 다시 할지 질문하기
    while user_wants_continue != 1:
        game_continue = input("다시 하시겠습니까?(y/n): ").lower()
        #사용자가 둘 중 하나로만 입력하도록 하기
        # 4. 다시 한다면 처음으로 돌아가기
        if game_continue == 'y':
            print("게임을 다시 진행합니다.")
            user_wants_continue = 1
            life.append('1')
            os.system("cls")
        elif game_continue == 'n':
            user_wants_continue = 1
            win_per = round(win/cnt * 100,2)
            print(f"총 {cnt}번 게임해서 {win}번 이겼습니다. 당신의 승률은 {win_per}%입니다.")
        else:
            print("y와 n중 하나로만 입력해 주세요!")
