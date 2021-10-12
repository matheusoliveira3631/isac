import wikipedia

wikipedia.set_lang("pt")
def define(word):
    try:
        text=wikipedia.summary(word)
        return text
    except:
        suggestion=wikipedia.suggest(word)
        text=wikipedia.summary(suggestion)
        return text