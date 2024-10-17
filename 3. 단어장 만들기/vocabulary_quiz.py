with open('3. 단어장 만들기/vocabulary.txt', 'r') as f:
    for line in f:
        #변수 지정
        quiz = line.strip().split(': ')[1]
        answer = line.strip().split(': ')[0]
        
        #퀴즈 출제
        user_answer = input(f"{quiz}: ")

        #정답 판별
        if user_answer == answer:
            print("맞았습니다!\n")
        else:
            print(f"아쉽습니다. 정답은 {answer}입니다.\n")