class Jumper():
    
    def __init__(self):
        self.parachute = 4
        pass

    def get_parachute(self, parachute):
        return self.parachute

    def cut_line(self, parachute):
        self.parachute -= 1

    def is_dead(self, parachute):
        if self.parachute == 0:
            return True
        return False