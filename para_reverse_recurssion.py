def rpara(paragraph):
    words = paragraph.split()
    reversed_words = [wordreversal(word) for word in words]
    return ' '.join(reversed_words)

def wordreversal(word):
    if len(word) == 0:
        return ''
    else:
        return word[-1] + wordreversal(word[:-1])


paragraph = input()
print(paragraph)
rp = rpara(paragraph)
print(rp)
