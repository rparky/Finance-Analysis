words = []
for entry in records:
    temp = entry.description_.split(' ')
    temp2 = []
    for element in temp:
        a = element.strip()
        temp2.extend(a.split(','))

    words.extend(temp2)

words = list(filter(None, words))
words.sort()

lesswords = list(dict.fromkeys(words))
lesswords.sort()

dates = []
numbers = []
probablynumber = []
cash = []
stillwords = []
for word in lesswords:
    if Utils.is_date_time(word):
        dates.append(datetime.strptime(word, '%d-%m-%Y'))
    elif Utils.is_date_time2(word):
        dates.append(datetime.strptime(word, '%Y-%m-%d'))
    elif Utils.is_float(word):
        numbers.append(float(word))
    elif '£' in word:
        cash.append(word)
    elif Utils.is_float(word[0]):
        probablynumber.append(word)
    else:
        stillwords.append(word)

# first remove dates
# then remove money
# then remove other random numbers