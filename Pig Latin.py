def pig_latin(word):
    if word[0] in "aeiou":
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'
        
sentence = input("Enter a sentence you want to translate to Pig latin: ")
print(' '.join(pig_latin(word) for word in sentence.split()))