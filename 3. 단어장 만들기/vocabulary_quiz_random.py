import random

with open('3. 단어장 만들기/vocabulary.txt', 'r') as f:
    #단어장 사전 만들기
    voca = {}
    for line in f:
        korean_word = line.strip().split(': ')[1]
        english_word = line.strip().split(': ')[0]
        voca[korean_word] = english_word

    while True:
        #문제와 답 생성
        question = random.choice(list(voca.keys()))
        answer = voca[question]
        
        #정답 입력
        user_answer = input(f"{question}: ")

        #종료
        if user_answer == 'q':
            break
        #정답 판별
        elif user_answer == answer:
            print("맞았습니다!\n")
        else:
            print(f"아쉽습니다. 정답은 {answer}입니다.\n")

