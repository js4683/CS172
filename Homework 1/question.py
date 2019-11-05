#File: question.py
#Purpose: Homework for CS172
#Date: April 15, 2019
#Author: Jashanpreet Singh

class Question():
    def __init__(self, ques='', ans1 ='', ans2='', ans3= '', ans4='', correct =''):#An object with the paramaters in order: question, option 2, option 3, option 4, correct answer
        self.__question = ques
        self.__answer1 = 'A.' + ans1
        self.__answer2 = 'B.' + ans2
        self.__answer3 = 'C.' + ans3
        self.__answer4 = 'D.' + ans4
        self.__correctAnswer = correct
#Following methods allow a user to change the options in a question
    def SetOption1(self, opt1):
        self.__answer1 = 'A.' + opt1
    def SetOption2(self, opt2):
        self.__answer2 = 'B.' + opt2
    def SetOption3(self, opt3):
        self.__answer3 = 'C.' + opt3
    def SetOption4(self, opt4):
        self.__answer4 = 'D.' + opt4
#getters for the options along with calling the setters
    def getQuestion(self):
        return self.__question
    def getOption1(self):
        return self.__answer1
    def getOption2(self):
        return self.__answer2
    def getOption3(self):
        return self.__answer3
    def getOption4(self):
        return self.__answer4
    def AnswerChecker(self):
        return self.__correctAnswer
#returns the question followed by all the answer choices
    def __str__(self):
        return ('{0}\n{1}\n{2}\n{3}\n{4}'.format(self.getQuestion(), self.getOption1(), self.getOption2(), self.getOption3(), self.getOption4()))
