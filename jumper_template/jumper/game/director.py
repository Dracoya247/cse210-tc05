from game.console import Console
from game.jumper import Jumper
from game.word import Word

class Director():
    """This class directs(controls) the sequence of play. This should
    be easy for the programmer to understand the sequence of the game."""

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.word = Word()

    def start_game(self):
        """Initiates the game in a loop controlling the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        """while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()"""

        word = word.get_word()
        ending = False
        play_game = True

        while play_game:

            console.write(word)

            lives = jumper.get_parachute()				
            console.write(lives)
    
            letter = console.read()	
        
            if word.guess(letter):
                word.fill_letter(letter)
            else:
                jumper.cut_line()
            
            console.write(parachute)			
            if word.word_done():
                ending = True
                play_game = False				
                        
            if jumper.is_dead():
                play_game = False


        console.display_ending(ending)				