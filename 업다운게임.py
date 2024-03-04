import random
import sys

best_count = 99

def question_number():
    random_number = random.randint(1,100)
    print(f"맞춰야하는 숫자 : {random_number}")
    return random_number

def play_game():
    global best_count
    count = 0
    close_flag = False
    random_number = question_number()
    
    while True:
        if close_flag:
            sys.exit()
        
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
                    
                    if again.lower() == 'y':
                        print("이전 게임 플레이 최고 기록:", best_count)
                        play_game()
                    
                    elif again.lower() == "n":
                        print("게임 종료")
                        close_flag = True
                        break
                    else:
                        print("y/n만 입력 가능합니다.")
                

        else:
            print("1~100 범위 내 숫자를 입력하시오.")              


if __name__ == "__main__":
    play_game()
