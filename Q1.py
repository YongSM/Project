#import random
#random_number = random.radint(1, 100)
#input_number = int(input ("숫자를 입력하세요: "))

import random

best_count = 99

def play_game():
    random_number = random.randint(1,100)
    count = 0
    global best_count

    while True:
    
        input_num = int(input("[Up/Down 게임] 1~100 사이의 숫자를 입력하시오. :"))
    
        if 1 <= input_num <= 100:
                       
            if input_num > random_number :
                count +=1
                print('Down')
                
            elif input_num < random_number :
                count +=1
                print('Up')
            
            elif input_num == random_number :
                count +=1 
                print(f"축하합니다. {count}회 도전 끝에 맞췄습니다!")
                
                if count < best_count:
                    best_count = count
            
                while True:
                    
                    again = input("게임을 다시 하시겠습니까?(y/n):")
                    
                    if again.lower == 'y':
                        print("이전 게임 플레이 최고 기록:", best_count)
                        break
                    
                    elif again.lower == 'n':
                        print("게임 종료")
                        break
                    else:
                        print("y/n만 입력 가능합니다.")
                

        else:
            print("1~100 범위 내 숫자를 입력하시오.")              


if __name__ == "__main__":
    play_game()