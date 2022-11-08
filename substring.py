import random
import string

def randomWord(length):
    words = string.ascii_lowercase
    return ''.join(random.choice(words) for i in range(length))

def substring(word):
    substrings =[]
    for i in range(0, len(word), 4):
        substrings.append(word[i:i+4])
    return substrings

def countSubtrings(word):
    subs = substring(word)
    results = {}
    for i in range(0, len(subs)):
        counter = word.count(subs[i])
        if(counter  > 1):
            results[subs[i]] = counter

    return results    

def main():
    while True:
        try:
            length = input("Insert the length:")
            word = randomWord(length)
            results = countSubtrings(word)
            print("The word is :"+word+" \n")
            print("The result is")
            print(results)
        except:
            print("Only numbers")

if __name__ == "__main__":
    main()