from PyDictionary import PyDictionary

dictionary = PyDictionary()

filler = ["'", '{', '}', '[', ']']

d = {
    'test': 'nice'
}

def means(word):
    if type(d) is type(dictionary.meaning(word)):
        meaning = str(dictionary.meaning(word))
        for x in filler:
            meaning = meaning.replace(x, '')
        msg = word + ' meaning:\n' + meaning 
        return msg
    else:
        return 'made up word it doesnt exist i guess'

