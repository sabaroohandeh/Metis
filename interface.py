import abc

class inputInt (abc.ABC):
    @abc.abstractmethod
    def xPos(self):
        pass

    @abc.abstractmethod
    def yPos(self):
        pass

class outputInt (abc.ABC):
    @abc.abstractmethod
    def finishGame(self):
        pass
    @abc.abstractmethod
    def new_stat(self):
        pass

class logicInt(abc.ABC):
    @abc.abstractmethod
    def applyInput(input):
        pass
    @abc.abstractmethod
    def inputIsValid(boolean):
        pass
    @abc.abstractmethod
    def is_player_win(self, player):
        pass

