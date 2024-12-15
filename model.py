from abc import ABC,abstractmethod
from typing import Final

class BankAccount(ABC):
     _id = 0
     def __init__(self, balance:float=0) -> None:
          self.balance = balance
          BankAccount._id += 1
          self.acountId = BankAccount._id

     def deposit(self, amount:float) -> float :
          self.balance += amount
          return amount
    
     def transfer(self, other:'BankAccount', amount:float)->None:
          other.deposit(self.withdraw(amount)) 

     @abstractmethod
     def withdraw(self, amount:float) -> float:
         pass

     def __str__(self) -> str:
          return f'{self.acountId:2d} {self.balance:5d}'

     

class SavingAccount(BankAccount):
     SAVING_AMOUNT: Final[float] = 100

     def __init__(self, interestRate:float, balance: float) -> None:
          if balance >= SavingAccount.SAVING_AMOUNT :
               super().__init__(balance)
               self.interestRate = interestRate
          else:
               print("account not created !!!")
               return None     

     def withdraw(self, amount: float):
          if self.balance - amount >= SavingAccount.SAVING_AMOUNT:
               self.balance = self.balance - amount
               return amount
          availabe_amount:float = self.balance - SavingAccount.SAVING_AMOUNT
          self.balance = SavingAccount.SAVING_AMOUNT
          return availabe_amount

     def addPeriodicInterest(self)->float:
          interest:float = self.balance * self.interestRate
          self.balance = self.balance * interest
          return interest
     
     def __str__(self) -> str:
          return f'{super().__str__()} {self.interestRate:5d}'

class CheckingAccout(BankAccount):
     FREE_TRANSACTIONS:Final[int]    = 3
     TRANSACTION_FEE:Final[float]    = 0.2
     DRAFT_OVER:Final[float]         = 500

     def __init__(self, balance: float = 0) -> None:
          super().__init__(balance)
          self.transaction_count = 0

     def  withdraw(self, amount: float) -> float:
          self.transaction_count += 1
          if self.balance + CheckingAccout.DRAFT_OVER - amount >= 0 :
               self.balance = self.balance - amount
               return amount
          available_amount = self.balance + CheckingAccout.DRAFT_OVER
          self.balance = self.balance - available_amount
          return available_amount  

     def deductFess(self)->float:
          fees:float = 0
          if self.transaction_count > CheckingAccout.FREE_TRANSACTIONS:
               fees:float = (self.transaction_count - CheckingAccout.FREE_TRANSACTIONS) * CheckingAccout.TRANSACTION_FEE
               self.balance -= fees
          return fees
     
     def deposit(self, amount: float) -> float:
          self.transaction_count += 1
          return super().deposit(amount)
     
     def transfer(self, other: 'BankAccount', amount: float) -> None:
          self.transaction_count += 1
          return super().transfer(other, amount)

class transfer():
    def __init__(self, id : int, accountId: int, transactionType: str, amount: float,
                date: str,relatedAccountId :int ) -> None:
        self.id = id
        self.accountId = accountId
        self.transactionType = transactionType
        self.amount = amount
        self.date = date
        self.relatedAccountId = relatedAccountId
    
        

    def __str__(self):
        return f'{self.id:2d} {self.accountId:5d} {self.transactionType:8d} {self.amount:5d}{self.date:10s} {self.relatedAccountId:5d}'
            
        