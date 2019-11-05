#File: main.py
#Purpose: Homework for CS172
#Date: April 15, 2019
#Author: Jashanpreet Singh

from question import Question
#Set of questions stored in a list which are called by using the list's index
QuestionSet = [Question("Which of the following is a synonym for good?", "Work", "Bad", "Stupid", "Nice", "d"),
     Question("Which of the following is a synonym for bad?", "Horrific", "Cool", "Want", "Because", "a"),
     Question("Which of the following is a synonym for under?", "Hello", "Day", "Beneath", "Most", "c"),
     Question("Which of the following is a synonym for friend?", "Give", "Problem", "Course", "Ally", "d"),
     Question("Which of the following is a synonym for annoying?", "Different", "Irritating", "Leave", "Life", "b"),
     Question("Which of the following is a synonym for understand?", "Leave", "Seem", "Work", "Comprehend", "d"),
     Question("Which of the following is a synonym for cruel?", "Awesome", "Big", "Evil", "Number", "c"),
     Question("Which of the following is a synonym for positive?", "Child", "Person", "Good", "Company", "c"),
     Question("Which of the following is a synonym for smart?", "Young", "Intelligent", "Important", "Me", "b"),
     Question("Which of the following is a synonym for dumb?", "Foolish", "Time", "Activist", "Administrator", "a"),
     Question("Which of the following is a synonym for bright?", "Dull", "Table", "Shiny", "Jacket", "c"),
     Question("Which of the following is a synonym for right?", "Correct", "Computer", "Glasses", "False", "a")]
player1 = 0 #points variables for both players
player2 = 0
print('Welcome to the Synonyms Quiz!')
print('----------------------------')
for x in range(0, 12): #For loop to go through the 10 questions
    if x % 2 == 0: #allows us to switch between players, this is for player 1
        print('Player 1 Here is your Question.')
        print(QuestionSet[x])#prints the return of the Question Class
        answer = input("Type in your answer (a,b,c,d):\n") #Ask the user for input
        while True: #A loop that runs until the user enters a valid response
            if QuestionSet[x].AnswerChecker() == answer.lower():#handles if answer is correct
                print('That is correct!')
                print('----------------')
                player1 += 1 #gives player 1 a point for each correct answer
                break
            elif answer.lower() != 'a' and answer.lower() != 'b' and answer.lower() != 'c' and answer.lower() != 'd': #handles if input is not valid
                answer = input('Invalid Input Try Again:\n') #asks for input again
                continue
            else: #handles if answer is wrong
                print('Better Luck Next Time')
                print('---------------------')
                break
    else: #Following is for player 2 but the code is the same as player 1
        print('Player 2 Here is your Question.')
        print(QuestionSet[x])
        answer = input("Type in your answer (a,b,c,d):\n")
        while True:
            if QuestionSet[x].AnswerChecker() == answer.lower():
                print('That is correct!')
                print('----------------')
                player2 += 1
                break
            elif answer.lower() != 'a' and answer.lower() != 'b' and answer.lower() != 'c' and answer.lower() != 'd':
                answer = input('Invalid Input Try Again:\n')
                continue
            else:
                print('Better Luck Next Time')
                print('---------------------')
                break
# announcing the score
print('')
print('Final Score')
print('Player 1 Score:', player1)
print('Player 2 Score:', player2)
if player1 > player2: #If player 1 has more points
    print('Player 1 wins!')
elif player1==player2: #if player 1 and player 2 has the same amount of points
    print('It is a draw between Player 1 and Player 2.')
else: #If player 2 has more points
    print('Player 2 wins!')
