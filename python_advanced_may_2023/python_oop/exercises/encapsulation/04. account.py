class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def __is_valid_pin(self, account_pin, input_pin):
        return account_pin == input_pin

    def get_id(self, pin):
        if not self.__is_valid_pin(self.__pin, pin):
            return "Wrong pin"
        return self.__id

    def change_pin(self, old_pin, new_pin):
        if not self.__is_valid_pin(self.__pin, old_pin):
            return "Wrong pin"
        self.__pin = new_pin
        return "Pin changed"

# test code
account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
