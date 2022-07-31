import random

dataMapping = ["가위", "바위", "보"]

def convertInput(inputData):
    inputDataInt = 0
    if inputData == "가위":
        inputDataInt = 0
    elif inputData == "바위":
        inputDataInt = 1
    elif inputData == "보":
        inputDataInt = 2
    else:
        inputDataInt = 3

    return inputDataInt


def rsp_advanced(games):
    for i in range(1, games + 1):
        inputData = input("가위 바위 보: ")
        my = convertInput(inputData)
        while my == 3:
            print('가위, 바위,보 중에 다시 입력해주세요!')
            inputData = input("가위 바위 보: ")
            my = convertInput(inputData)

        computer = random.randint(0, 2)

        print("나:", dataMapping[my])
        print("컴퓨터:", dataMapping[computer])

        if (my == computer):
            print(f"{i}번째 판 비겼습니다.")
        elif (computer - my in {1, -2}):
            print(f"{i}번째 판 컴퓨터의 승리!")
        else:
            print(f"{i}번째 판 나의 승리!")
        print('===============')

try:
    games = int(input("몇 판을 진행하시겠습니까? : "))
    rsp_advanced(games)
except:
    print('오류입니다. 숫자만 입력해주세요!')


