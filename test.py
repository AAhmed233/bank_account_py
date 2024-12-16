from model import BankAccount,CheckingAccout,SavingAccount
from dao import insertChekingAccount,insertTransaction,insertSavingAccount

class Bank:
    bank:list[BankAccount]=[]

    @staticmethod
    def add(account:BankAccount)->bool:
        Bank.bank.append(account)
        if isinstance(account, CheckingAccout):
            value = (account.balance , 'Cheking', 0)
            insertChekingAccount(value)
        else:
            value = (account.balance , 'Saving', account.interestRate)
            insertSavingAccount(value)
        return True
    
    @staticmethod
    def list()->list[BankAccount]:
        return Bank.bank
    
    @staticmethod
    def search(id:int)->BankAccount:
        for product in Bank.bank:
            if product.acountId == id:
                return product
        return None
         
    @staticmethod
    def print(list):
        for product in list:
            if isinstance(product, SavingAccount):
                print(product.acountId, product.balance, product.interestRate)
            else:
                print(product.acountId, product.balance)

    @staticmethod
    def addTransfer(accountId, transactionType, amount, timestamp, relatedAccountId):
        value = (accountId, transactionType, amount, timestamp, relatedAccountId)
        insertTransaction(value)
        

if __name__ == "__main__":
    printer:BankAccount = CheckingAccout(1000)
    lapop:BankAccount = SavingAccount(0.3, 5000)

    Bank.add(printer)
    Bank.add(lapop)
    lapop:BankAccount = SavingAccount(0.5, 7000)
    Bank.add(lapop)
    Bank.print(Bank.list())
    id = 2
    for product in Bank.list():
        if product.acountId == id :
            product.withdraw(900)
            product.transfer(Bank.search(1), 100)

    Bank.print(Bank.list())