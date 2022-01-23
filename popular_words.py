text = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
words = ['i', 'was', 'three', 'near']

def popular_word(text: str, words: list) -> dict: 
    text = text.lower()
    text = text.split()
    dc = {}
    for w in words: 
        dc[w] = text.count(w)

    return dc

print(popular_word(text, words))
