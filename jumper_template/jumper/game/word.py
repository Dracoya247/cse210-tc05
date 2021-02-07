from Math import * 

class Word():

    #Random words
    word_list = ['rainbow', 'computer', 'science', 'programming', 
            'python', '', 'player', 'condition', 
            'reverse', 'water', 'board', 'geeks'] 

    def get_word(self):

        return word_list[int(Math.random() * 11)]        

    def guess(self, letter, word):

        for l in word:
            if l == letter:
                return True
        return False

    def word_done(self, puzzle):

        for l puzzle:
            if l == "_":
                return False
        return True

"""
An idea/outline to how it could also be:
import random


    #Random words
word_list = 'ant baboon badger bat bear beaver camel cat clam cobra cougar\
        coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk\
        lion lizard llama mole monkey moose mouse mule newt otter owl panda\
        parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep\
        skunk sloth snake spider stork swan tiger toad trout turkey turtle\
        weasel whale wolf wombat zebra rainbow computer science programming\
        python player condition reverse water board geeks'.split()

def get_random(word_list):
        word_index = random.randint(0, len(word_list) - 1)
        return word_list [word_index]

secret_word = get_random(word_list)
print(secret_word)
"""