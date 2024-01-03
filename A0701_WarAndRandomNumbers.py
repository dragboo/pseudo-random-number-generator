# Assignment 0701: War and Random Nunmbers 

# Name: Suraj Nihal, Pushyap
# Date: 10/24/2023
# Student ID: 2023345

# Video Link: https://youtu.be/zLtvyScacw8

# I have not given or received any unauthorized assistance on this assignment

class WarAndPeacePseudoRandomNumberGenerator:

    def __init__(self, seed=0, step=100):
        self.seed = seed
        self.step = step
        self.currentPosition = self.seed
        self.pairList = []

        with open("war-and-peace.txt", "r") as infile:
            infile.seek(0,2)                                    
            self.totalLength = infile.tell()                                           # getting the total length of the file     

    def getCharlist(self):
        '''
        generates the pair list of characters
        '''    
        infile = open("war-and-peace.txt","r")
        
        char1, char2 = "", ""
        currentPosition = 0
        firstRun = True
        self.pairList = []

        while len(self.pairList) <= 16:                                               # getting 16 unqiue pairs of characters 
            if len(self.pairList) == 0 and firstRun:
                infile.seek(self.currentPosition % self.totalLength)        
                char1 = infile.read(1)                                                # getting character based on the current position
                infile.seek((self.currentPosition + self.step) % self.totalLength)
                char2 = infile.read(1)
            else:
                currentPosition = infile.tell()                                       
                infile.seek((currentPosition + self.step) % self.totalLength)
                char1 = infile.read(1)
                currentPosition = infile.tell()
                infile.seek((currentPosition + self.step) % self.totalLength)
                char2 = infile.read(1)
            
            if char1 != char2:                                 
                self.pairList.append((char1,char2))                                   # adding the pair to the list only when they are different
            elif firstRun:
                firstRun = False

        self.currentPosition = infile.tell()                                          # updating the current position so it does not check for the same characters
        infile.close()

    def customRandom(self, min=0, max=1):
        '''
        generates pseudo random numbers between 0 and 1
        '''
        self.getCharlist()
        result = 0
        n = 1

        for x, y in self.pairList:                                                    # checking for the ASCII values between the characters     
            if x>y:
                result += 1 / (2 ** n)                                                # earlier pairs have a larger impact on results
            n += 1
        return result * (max - min) + min                                             # scaling to fit the range between 0 and 1

prng = WarAndPeacePseudoRandomNumberGenerator(1234)

def getPrnList(n):
    '''
    generates a list of n pseudo random numbers 
    '''
    prnList = [prng.customRandom() for _ in range(n)]
    return prnList


if __name__ == "__main__":                                                                # helps by not invoking the code block when the module is imported 

    print(getPrnList(10))                                                                 # printing 10 pseudo random numbers

    def getResult():
        '''
        prints the minimum, maximum and average of 10,000 pseudo random numbers 
        '''
        randomList = getPrnList(10000)
        print(min(randomList))
        print(max(randomList))
        print(sum(randomList)/len(randomList))

    getResult()

