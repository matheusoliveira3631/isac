import wikipedia, time
wikipedia.set_lang("pt")
def define(word):
    try:
        text=wikipedia.summary(word)
        return text
    except:
        suggestion=wikipedia.suggest(word)
        text=wikipedia.summary(suggestion)
        return text
 
#=========================><========================#
#time related methods
def now():
    import time
    time_list=time.strftime("%a, %d, %m, %Y, %H, %M").split(', ')
    if time_list[5][0]=='0':
        temp=time_list[5]
        time_list[5]=temp[1]
    months={
        '1':'Janeiro',
        '2':'Fevereiro',
        '3':'Março',
        '4':'Abril',
        '5':'Maio',
        '6':'Junho',
        '7':'Julho',
        '8':'Agosto',
        '9':'Setembro',
        '10':'Outubro',
        '11':'Novembro',
        '12':'Dezembro',
    }

    days={
        'Mon':'Segunda',
        'Tue':'Terça',
        'Wed':'Quarta',
        'Thu':'Quinta',
        'Fri':'Sexta',
        'Sat':'Sábado',
        'Sun':'Domingo',
    }
    if time_list[5]=='00':
        time_string=f'Hoje é {days.get(time_list[0])}, dia {time_list[1]} de {months.get(time_list[2])} de {time_list[3]}, e são {time_list[4]} horas' 
    else:
        time_string=f'Hoje é {days.get(time_list[0])}, dia {time_list[1]} de {months.get(time_list[2])} de {time_list[3]}, e são {time_list[4]} horas e {time_list[5]} minutos'
    return time_string