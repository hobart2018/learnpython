def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(answer):
    words = answer.split()
    wordtype = {'north': 'direction',
                'south': 'direction',
                 'east': 'direction',
                 'go': 'verb',
                 'kill':'verb',
                 'eat': 'verb',
                 'the': 'stop',
                 'in': 'stop',
                 'of': 'stop',
                 'bear': 'noun',
                 'princess': 'noun',
                 }
    tokenword=[]
    for word in words:
        if word[0] >= '0' and word[0] <='9':
            tokenword.append(('number', convert_numbers(word)))
        else:
            try:
                tokenword.append((wordtype[word], word))
            except KeyError:
                tokenword.append(('error', word))
    return tokenword
