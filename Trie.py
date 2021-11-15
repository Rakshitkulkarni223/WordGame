from random import randint
from flask import Markup

class DictWord():
    def __init__(self):
        self.word = ''
        self.meaning = ''
    def __init__(self , word1 , meaning1 ):
        self.word = word1
        self.meaning = meaning1

class Trienode():
    def __init__(self):
        self.children=[None]*256
        self.isEndOfWord = False
        self.meaning = None

class Trie():
    # define the constructor for the trie class
    def __init__(self):
        self.root = self.getnode()

    # return the new node
    def getnode(self):
        return Trienode()


    # insert key(string) into the trie
    # O(n) time
    def insert(self , key , meaningOfWord ):

        itrNode = self.root

        length=len(key)

        for i in range(length):

            index=ord(key[i])
            if index < 0 or index >= 256 :
                continue
                # print( key[i] , index )
            # print( index )
            # if node already has a children at given position we continue to next char
            # else we make a new node at the current index
            if not itrNode.children[index]:
                itrNode.children[index]=self.getnode()


            itrNode = itrNode.children[index]

        # to indicate the end of word
        itrNode.isEndOfWord = True
        itrNode.meaning = meaningOfWord

    # search for a key into the dictionary
    # returns meaning if present else returns false
    # search O(n)
    def search(self,key):
        itrNode=self.root

        for i in range(len(key)):
            index=ord(key[i])

            # we fail to finda the given prefix key[0...i] into the dictionary
            if not itrNode.children[index]:
                return [False,'']

            itrNode=itrNode.children[index]


        if itrNode.isEndOfWord :
            # return
            return [True,itrNode.meaning]
        else:
            return [False , '' ]

    def hamming(self, path, curNode, word, distance):
        possibleWords = []

        if distance < 0 or curNode == None:
            return []

        if word == '':
            if curNode.isEndOfWord:
                curWord = DictWord(path, curNode.meaning)
                possibleWords.append(curWord)
                return possibleWords
            return []

        car, cdr = word[0], word[1:]

        for i in range(256):
            char = chr(i)
            if char == car:
                penalty = 0
            else:
                penalty = 1
            # print( penalty , path )

            for result in self.hamming(path + char, curNode.children[i], cdr, distance - penalty):
                possibleWords.append(result)
        return possibleWords

    def approximateSearch(self, word, error):
        possibleWords = []

        if error <= 0:
            return possibleWords

        path = ''
        curNode = self.root
        return self.hamming(path, curNode, word, error)

    def getfizzywords(self,word,error):

        possibleWords=self.approximateSearch(word,error)

        res = ''
        n = len(possibleWords)

        for i in range(n):
            if i != n - 1:
                res += "{}) {} -> {}".format(i + 1, possibleWords[i].word, possibleWords[i].meaning)
                res += "\n"
            else:
                res += "{}) {} -> {}".format(i + 1, possibleWords[i].word, possibleWords[i].meaning)

        if res == '':
            return "No such possible word exists!!!"
        else:
            return res


    def getNodesAtDepthHelper( self , curNode , curWord , remDepth ):
        if remDepth == 0 or curNode == None :
            return

        possibleWords = []
        if remDepth == 1 and curNode:
            for i in range( 256 ):
                if curNode.children[i] != None and curNode.children[i].isEndOfWord == True:
                    newWord = DictWord(curWord + chr(i), curNode.children[i].meaning )
                    possibleWords.append(newWord)
            return possibleWords

        for i in range(256):
            if curNode.children[i] != None:
                possibleWords += self.getNodesAtDepthHelper(curNode.children[i], curWord+chr(i), remDepth-1)

        return possibleWords



    def getNodesAtDepth(self , depth ):
        dict = {}

        curWord = ''
        curNode = self.root
        remDepth = depth

        return self.getNodesAtDepthHelper( curNode , curWord , remDepth )

    def getWords(self,depth):

        possibleWords=self.getNodesAtDepth(depth)

        res = ''
        n = 10

        exist={}

        for i in range(n):
            pos=randint(0,len(possibleWords)-1)
            if exist.get(pos)!=None:
                continue
            else:
                exist[pos]=True
                if i != n - 1:
                    res += "{}) {} -> {}".format(i + 1, possibleWords[pos].word, possibleWords[pos].meaning)
                    res += "\n"
                else:
                    res += "{}) {} -> {}".format(i + 1, possibleWords[pos].word, possibleWords[pos].meaning)

        if res == '':
            return "No such possible word exists!!!"
        else:
            return res

    def generateRandomWordHelper( self , options , curWord , curNode , remLen ):
        if remLen == 0 or curNode == None :
            return

        possibleWords = []
        if remLen == 1:
            for possibleChars in options:
                # print( possibleChars )
                if curNode.children[ ord( possibleChars ) ] != None and curNode.children[ ord( possibleChars ) ].isEndOfWord   == True:
                    newWord = DictWord(curWord + possibleChars, curNode.children[ ord( possibleChars ) ].meaning )
                    possibleWords.append( newWord )
            return possibleWords

        for possibleChar in options:
            # print( possibleChar )

            if curNode.children[ ord(possibleChar) ] != None:
                # print('hi')
                nextNode = curNode.children[ ord(possibleChar) ]
                nextWord = curWord + possibleChar
                possibleWords += self.generateRandomWordHelper(options, nextWord , nextNode , remLen-1 )

        return possibleWords

    def generateRandomWord( self , options , lenOfWord ):
        curWord = ''
        curNode = self.root
        # print( options )
        # print('\n\n\n')

        possibleWords = self.generateRandomWordHelper( options , curWord , curNode , lenOfWord )

        # print(len(possibleWords),dict(possibleWords))

        res=''
        n=len(possibleWords)

        for i in range(n):
            if i!=n-1:
                res+="{}) {} -> {}".format(i+1,possibleWords[i].word,possibleWords[i].meaning)
                res+="\n"
            else:
                res += "{}) {} -> {}".format(i+1,possibleWords[i].word, possibleWords[i].meaning)

        if res=='':
            return "No such possible word exists!!!"
        else:
            return res
