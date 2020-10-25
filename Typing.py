from random import randint
import time

class TypingGame:
    def __init__(self, sentence="", UserWriting="",timeStart=0,timeEnd=0):
        self.words = []
        self.sentence = sentence
        self.UserWriting = UserWriting
        self.timeStart = 0
        self.timeEnd = 0
        self.totalTime = 0
        self.correct = 0
    def getInput(self):
        self.UserWriting = input("Copy the sentence \n")[:len(self.sentence)]

    def getSentence(self):
        for x in range(5,randint(5,20)):
            self.sentence += self.words[randint(0,1001)] + " "

    def check(self):
        for x in range(0,len(self.UserWriting)):
            if(self.sentence[x] == self.UserWriting[x]):
                self.correct +=1

    def WPM(self):
        return int((len(self.sentence)/round(self.totalTime,2))*60)

    def beginTime(self):
        self.timeStart = time.time()

    def stopTime(self):
        self.timeEnd = time.time()

    def getTime(self):
      self.totalTime = round(self.timeEnd - self.timeStart,2)
      return self.totalTime

    def calcAcc(self):
      self.check()
      acc = self.correct/len(self.sentence)
      return round(acc*100,1)

    def genWords(self):
        f = open('1-1000.txt', 'r')
        self.words = f.read().split('\n')
        f.close()

    def main(self):
        start = input("Ready?(Y/N)")
        if(start == "y" or start == "Y"):
          tg = TypingGame()
          tg.genWords()
          print("type this sentence")
          tg.getSentence()
          print(tg.sentence)
          tg.beginTime()
          tg.getInput()
          tg.stopTime()
          tg.getTime()
          print("Gratz on finishing. You put: \n", tg.UserWriting,"\n And the sentence was \n", tg.sentence,)
          print("\n your stats were \n Total Accuracy:", tg.calcAcc(),"%")
          print("\n Total time:",tg.totalTime," seconds")
          print("\n Words per minute: ", tg.WPM())

        else: print("well idk what to tell you dude...")

tg = TypingGame()
tg.main()
#change
