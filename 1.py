class BankAccount:

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = float(balance)


    def withdraw(self, amount: float) -> str:
        if self.__balance>=amount:
            self.__balance = self.__balance-amount
            return f'\tСо счета снято {amount} денег\n\tНа счету осталось {self.__balance}'
        else:
            return f'На счете недостаточно средств: {self.__balance} < {amount}'   


    def deposit(self, amount: float) -> float:
        self.__balance += amount
        return self.__balance

    def get_balance(self) -> float:
        return self.__balance



owner1 = BankAccount('Петя', 50_000)
print(owner1.get_balance())

print(owner1.withdraw(5000))


        
