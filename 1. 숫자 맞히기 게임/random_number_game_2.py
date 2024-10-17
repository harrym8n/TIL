import random

answer = random.randint(1,20)

#변수 정의
tries = 0
guess = -1

#게임 실행
while guess != answer and tries < 4:
    guess = int(input(f"기회가 {4-tries}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "))
    tries += 1
    if guess > answer:
        print("Down")
    elif guess < answer:
        print("Up")
    
if guess == answer :
    print(f"축하합니다. {tries}번 만에 숫자를 맞히셨습니다.")
else:
    print(f"아쉽습니다. 정답은 {answer}입니다.")