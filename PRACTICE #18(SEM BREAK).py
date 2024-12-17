def QUIZ():
    #INTRO
    print("SIMPLE QUIZ")
    name = input("Enter your name: ")
    print("Instructions:", '\n',
          "1. This is a 5 item quiz", '\n',
          "2. You have 5 lives, once it hit zero GAME OVER", '\n',
          "3. If you got all the answer correctly YOU WIN", '\n',
          "4. wrong spelling wrong, no caps", '\n')

    #MAIN
    lives = 5
    QUESTIONS = [
        ("1. What is the capital of France?", "paris"),
        ("2. Who wrote 'Romeo and Juliet'?", "william shakespeare"),
        ("3. What is the chemical symbol for water?", "h2o"),
        ("4. How many vowels are in the alphabet?", "5"),
        ("5. What is the national anthem of the Philippines", 'Lupang Hinirang')
    ]

    while lives != 0:
        for question, correct_answer in QUESTIONS:
            answer = input(f"{question}? ")
            if answer == correct_answer:
                print("Correct!")
            else:
                lives -= 1
                print("Remaining lives", lives)
        else:
            print('\n', 'THE QUIZ IS OVER', '\n', "You got", lives, "Out of 5")
            break
    else:
        print('\n', 'THE QUIZ IS OVER', '\n', "You got", lives, "Out of 5")

QUIZ()

