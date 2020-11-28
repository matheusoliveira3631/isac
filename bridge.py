from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize




def isolate_term(sentence):
    n=0
    tokens=word_tokenize(sentence)
    stpw=stopwords.words("portuguese")
    terms=[]
    keywords=[]
    for i in tokens:
        if i in stpw:
            keywords.append(i)

    while n<len(tokens):
        if tokens[n] in stpw:
            sec=tokens[n+1:]
            for i in sec:
                if i in stpw:
                    pass
                else:
                    terms.append(i)
            break
        else:
            n+=1
    res={
        'terms':terms,
        'keywords':keywords
    }
    return res
    
    