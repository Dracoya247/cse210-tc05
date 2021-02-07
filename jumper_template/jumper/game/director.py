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
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        pass

    def do_updates(self):
        pass

    def do_outputs(self):
        pass