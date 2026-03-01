
def ask_questions(q):
    
    print(q["question"])

    for option in q["options"]:
        print(option)

    while True:
        user_input = input("Enter answer (a,b,c,d): ").lower()
        if user_input in ["a","b","c","d"]:
            return user_input
        else:
            print("Please enter only a, b, c or d.")
def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["a) Berlin", "b) Paris", "c) Rome", "d) Madrid"],
            "answer": "b"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["a) Earth", "b) Mars", "c) Venus", "d) Jupiter"],
            "answer": "b"
        }
    ]
    while True:

        score=0

        for q in questions:
            answer=ask_questions(q)

            if answer==q["answer"]:
                print("Correct!")
                score+=1
            else:
                print("Wrong!")

        print()
        print("-"*30)
        print("Your final score : ",score,"/",len(questions))
        percentage=(score/len(questions))*100
        print(f"Percentage : {percentage:.2f}%")
        print("-"*30)
        print()
    
        responce=input("Plar again ? (y/n) : ").lower()
        if responce!="y":
            print("Thanks for playing.")
            break
        else:
            quiz()


quiz()


