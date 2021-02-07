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