def find_even_number(n, m):
    numbers = [i for i in range(n, m + 1)]  # 숫자 n부터 m까지 list 생성.
    sum = (numbers[0] + numbers[-1])
    for i in numbers:
        if i % 2 == 0:
            print(f'{i} 짝수')
            if i != sum / 2:
                continue
            else:
                print(f'{i} 중앙값')

try:
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))
    find_even_number(n, m)
except:
    print("숫자를 제대로 입력해주세요.(첫 번째 수 < 두번쨰 수) ")
