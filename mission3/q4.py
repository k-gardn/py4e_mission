import math


def count_prime_number(n, m):
    numbers = [i for i in range(n,m+1)]
    pcnt = m - n + 1
    for i in numbers:
        for j in range(2, int(math.sqrt(i)) + 1):  # n의 제곱근을 정수화 시켜준 후 + 1
            if i % j == 0:
                pcnt -= 1
                break
            else:
                continue
        if i == 1 :
            pcnt -= 1
    return pcnt


try:
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))
    primecnt = count_prime_number(n, m)
    print(f'소수개수 {primecnt}')

except:
    print('숫자를 제대로 입력해주세요.(첫 번째 수 < 두번쨰 수)')