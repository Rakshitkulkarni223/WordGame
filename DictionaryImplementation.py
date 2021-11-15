from itertools import permutations
import time
import Trie
import json

def extractfile(file_name):

    # keys=map()
    # with open(file_name,"r") as f:
    #     for data in f:
    #         data =''.join(c for c in data if c != '\n')
    #         keys.add(data)
    # print("Our dictionary contains the following words now " )
    # for word in keys:
    #     print( word , end="\t" )
    # print("\n")
    # return keys
    f = open(file_name)
    data = json.load(f)
    return data

def parse_file(file):
    while True:
        try:
            keys = extractfile(file)
            # print('Loading...')
            return keys

        except:
            print("Keep the 'dictionary.txt' in the same folder of this file")
            time.sleep(10)
            continue


def solution(t):
    print("Hello")
    # while True:
    #     word = input( "Enter the word to search : ")
    #     result = t.search(word)
    #     if result[0]:
    #         print( word , "is present in the dictionary")
    #         print( 'Meaning = ', result[1] )
    #     else:
    #         print( word , "is absent in the dictionary")
            
    #         hammingData = t.hamming('', t.root, word, 3 , '')
    #         # print(hammingData)
    #         for i in hammingData:
    #             print(i)

    # wordsAtDepth2 = t.getNodesAtDepth(1)
    # for word in wordsAtDepth2:
    #     print(word.word , word.meaning )

    randomWords = t.generateRandomWord(['m','o', 'h', 'i','t' ], 5 )
    for words in randomWords:
        print(words.word , words.meaning )
   


def main():
    # now data contains keys with their meaning
    data = extractfile('data/dictionary.json')

    t=Trie.Trie()

    # inserting word into the trie
    for key, meaning in data.items() :
        # print( key , meaning[0] )
        # break
        t.insert( key , meaning[0] )
        
    print("Sucessfully built the trie")
    return t
    # solution(t)


if __name__=='__main__':
    main()
