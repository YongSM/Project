# 문제 2
# cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']

# 새로운 리스트에 kia, hyundai를 대문자로 추가하라.(upper())

cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']

def solutdion(cars):
    n = len(cars)
    for i in range(n): 
        if cars[i] == 'kia' or cars[i]== 'hyundai':
            cars[i] = cars[i].upper()
    return cars

print(solutdion(cars))
