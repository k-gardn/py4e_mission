def gugudan(number):
    for i in range(1, 10):
        if i % 2 == 0:
            continue

        else:
            result = number * i
            if result <= 50:
                print(f'{number} X {i} = {result}')
try:
    number = int(input("몇 단? : "))
    gugudan(number)

except:
    print('숫자만 입력해주세요!!')
