#Custom Exceptions
class InvalidAccount(Exception):
    def __init__(self,account,accList,transactionID):
        self.account = account
        self.accList = accList
        self.transactionID = transactionID

    def __str__(self):
        return (f'Invalid {self.account} Account. Account Number = {self.accList} in Transaction Id: {self.transactionID}')
    
class NoSufficientBalance(Exception):
    def __init__(self,accountNumber,amount,transactionID):
        self.accountNumber = accountNumber
        self.amount = amount
        self.transactionID = transactionID
    
    def __str__(self):
        return f"Insufficient Balance in {self.accountNumber} for amount {self.amount} in Transaction Id {self.transactionID}"

class InvalidTransactionType(Exception):
    def __init__(self,transactionType,transactionId):
        self.transactionType = transactionType
        self.transactionId = transactionId
    
    def __str__(self):
        return f"Invalid Transaction Type: {self.transactionType} in Transaction {self.transactionId}"

class InvalidAmount(Exception):
    def __init__(self,amount,transactionId):
        self.amount = amount
        self.transactionId = transactionId
    def __str__(self):
        return f"Invalid amount {self.amount} in Transaction {self.transactionId}"