import random
import string 
import requests 
# function that generates a single random character 
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength = 12 
# function that generates a password of random characters 
def generate_strong_password():
    password = ""
    for i in range(passwordLength): 
        password = password + random_character() 
    print (password)


# 
def fetch_word(): 
    url = "https://random-word-api.herokuapp.com/word?length=6"

    response = requests.get(url)
    word = response.json()[0]
    return word 

# function to generate weaker but memorable password
def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    word1 = replacingLetters(word1)
    word2 = replaceLetters(word2)
    password = word1 + word2
    return password


def replaceLetters(word):
    word = word[0].upper() + word[1:]
    if "a"  in word: 
        word = word.replace("a", "@")
    if "o"  in word: 
        word = word.replace("o", "%")
    if "q"  in word: 
        word = word.replace("q", "#")



    
# replace 3 others letters with numbers or symbols 
    return word
