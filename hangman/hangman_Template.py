import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.words_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.words_guessed) 
        self.list_letters = []
        pass

    def check_letter(self, letter):
        '''
        long comments dsjhdlsdklksdljskldkdsjdls check letter is a function to 
        '''
        self.letter = self.letter.lower()   

     
        if self.letter in self.word:
            for i in range(len(list(self.word))):
                if  self.word[i] == self.letter: #if letter is in the word:
                    self.num_letters -= 1
                    self.words_guessed[i] = self.letter #replace '_' with the letter
            if self.letter not in self.list_letters: #if the letter isnt in the list of letters used, then put it in the list 
                self.list_letters.extend(self.letter)
                print(f'Used letters: {self.list_letters}', f'Nice! {self.letter} is in the word!', self.words_guessed) # and print this    
            else:
                print(f'You have already tried {self.letter}') #if it is in the list, then print thi
        else:
            if self.num_lives != 0:
                if self.letter not in self.list_letters: #if the letter isnt in the list of letters used, then put it in the list 
                        self.list_letters.extend(self.letter)
                        self.num_lives -= 1
                        print(f'Sorry, {self.letter} is not in the word.', f'You have {self.num_lives} lives left.')
                        print(f'Letter that you just tried: {self.letter}', self.list_letters)
                else:  
                    print(f'You have already tried {self.letter}') #if it is in the list, then print thi
 
 
    def ask_letter(self):
        self.letter = input('Please enter a letter:')
        if len(self.letter) > 1:
            print('Please, enter just one character')
        else:
            self.check_letter(self.letter)
        pass 
    
    def play_game(self):
        self.game = Hangman(['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'], num_lives=5)
        while True:
            self.ask_letter() #todo 1: To test this task, you can call the ask_letter method
            if self.num_lives == 0:
                print(f'YOU LOST, the word was:{self.word}')
                break
            elif '_' not in self.words_guessed:
                print('Congratulations, you won!')
                break
            



if __name__ == '__main__':
    game = Hangman(['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'], 5)
    game.play_game()
