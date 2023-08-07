from abc import abstractmethod, ABC






class BaseLoan(ABC):
    def __init__(self, interest_rate, amount):
        self.interest_rate = interest_rate    # In percentage %
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self):
        pass