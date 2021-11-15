from flask import Flask, render_template, request
import DictionaryImplementation

import random

import string

trie=DictionaryImplementation.main()

letters = list(string.ascii_uppercase)

letter=''

word=''

app = Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/word1',methods= ['POST'])
def word1():
    userinput = request.form.get('word1')

    res=trie.search(userinput)

    if res[0]:
        return render_template('home.html',Meaning=userinput+' -> '+res[1])
    else:
        ans=trie.getfizzywords(userinput,2)
        return render_template('home.html',Meaning="Exact Match for {} not found but we found the following  {}".format(userinput,ans))

@app.route('/word2_1', methods=['POST'])
def get2_1():
    global letter
    letter = random.choices(letters,k=1)
    return render_template('home.html',area_for_random_letter=letter[0])

@app.route('/word2', methods=['POST'])
def get2():

    global letter

    userinput = request.form.get('word2')

    next_letter=''

    if letter[0]=='Z':
        next_letter='A'
    else:
        next_letter=letters[letters.index(letter[0])+1]

    if next_letter==userinput:
        return render_template('home.html',Next_word="✅")
    else:
        return render_template('home.html',Next_word="❌ Next Letter After {} is : {}".format(letter[0],next_letter))

@app.route('/word3', methods=['POST'])
def get3():
    length = request.form.get('word3')
    length=int(length)

    res=trie.getWords(length)
    print(res)
    return render_template('home.html',words=res)

@app.route('/word4', methods=['POST'])
def get4_A():
    global word
    userinput = request.form.get('A')
    if userinput!=None:
        word+=userinput

    userinput = request.form.get('B')
    if userinput != None:
        word += userinput

    userinput = request.form.get('C')
    if userinput != None:
        word += userinput

    userinput = request.form.get('D')
    if userinput != None:
        word += userinput

    userinput = request.form.get('E')
    if userinput != None:
        word += userinput

    userinput = request.form.get('F')
    if userinput != None:
        word += userinput

    userinput = request.form.get('G')
    if userinput != None:
        word += userinput

    userinput = request.form.get('H')
    if userinput != None:
        word += userinput

    userinput = request.form.get('I')
    if userinput != None:
        word += userinput

    userinput = request.form.get('J')
    if userinput != None:
        word += userinput

    userinput = request.form.get('K')
    if userinput != None:
        word += userinput

    userinput = request.form.get('L')
    if userinput != None:
        word += userinput

    userinput = request.form.get('M')
    if userinput != None:
        word += userinput

    userinput = request.form.get('N')
    if userinput != None:
        word += userinput

    userinput = request.form.get('O')
    if userinput != None:
        word += userinput

    userinput = request.form.get('P')
    if userinput != None:
        word += userinput

    userinput = request.form.get('Q')
    if userinput != None:
        word += userinput

    userinput = request.form.get('R')
    if userinput != None:
        word += userinput

    userinput = request.form.get('S')
    if userinput != None:
        word += userinput

    userinput = request.form.get('T')
    if userinput != None:
        word += userinput

    userinput = request.form.get('U')
    if userinput != None:
        word += userinput

    userinput = request.form.get('V')
    if userinput != None:
        word += userinput

    userinput = request.form.get('W')
    if userinput != None:
        word += userinput

    userinput = request.form.get('X')
    if userinput != None:
        word += userinput

    userinput = request.form.get('Y')
    if userinput != None:
        word += userinput

    userinput = request.form.get('Z')
    if userinput != None:
        word += userinput

    return render_template('home.html',Letter=word)

@app.route('/word4_1', methods=['POST'])
def get4_B():
    global word
    length = request.form.get('word4')

    if word=='' or length=='':
        return render_template('home.html', words_meaning="No Such possible words exist!!!")

    word=word.lower()
    word=list(word)
    length=int(length)


    res = trie.generateRandomWord(word, length)

    word=''

    return render_template('home.html', words_meaning=res)


if __name__ == "__main__":
    app.run(debug=True)