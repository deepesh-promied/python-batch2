'''
Bank Project

Table Schema
Account Number Account Name Balance

Transaction File (CSV)
Transaction Id | Trascation Type | Source Account | Destination Account | Amount

Transaction Type : Transfer| Deposit | Withdraw

Types of Error:
Invalid Account Number (Source or Destination or both)
No Sufficient Balance (Transfer or Withdraw)
Invalid Transaction Type
Invalid Amount (Invalid Value or Negative Value)

'''
# Assignment: Add datetime
# Assignment: Correct Invalid Account Logic for withdraw and deposit
import sqlite3

#Custom Exceptions
class LoggerFiles:
    def __init__(self):
        self.fian = open('log/InvalidLog.txt','a')
        self.nsb = open('log/NotSufficientBalance.txt','a')
        self.itt = open('log/InvalidTransaction.txt','a')
        self.iam = open('log/InvalidAmount.txt','a')

    def close(self):
        self.fian.close()
        self.nsb.close()
        self.itt.close()
        self.iam.close()


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

logfiles = LoggerFiles()
mydb = sqlite3.connect('bankproj.db')
cur = mydb.cursor()
minimumBalance = 1000

try:
    with open('TransactionFile.csv','r') as ft:
        for transaction in ft:
            try:
                print(transaction)
                transactionData = transaction.strip().split(',')
                '''
                [0]--> Transaction Id
                [1]--> Transaction Type
                [2]--> Source Account
                [3]--> Destination
                [4]--> Amount
                '''
                if(transactionData[1] in ['Transfer','Deposit','Withdraw']):
                    cur.execute(f'select count(*) from account where accountNumber = {transactionData[2]} or accountNumber = {transactionData[3]}')
                    if(cur.fetchone()[0]!=0):
                        if(int(transactionData[4])>0):
                            if(transactionData[1] in ['Transfer','Withdraw']):
                                cur.execute(f'select balance from account where accountNumber = {transactionData[2]}')
                                if(cur.fetchone()[0]-int(transactionData[4])>=minimumBalance):
                                    if(transactionData[1] == 'Transfer'):
                                        cur.execute(f'update account set balance = balance-{transactionData[4]} where accountNumber = {transactionData[2]}')
                                        cur.execute(f'update account set balance = balance+{transactionData[4]} where accountNumber = {transactionData[3]}')                        
                                        mydb.commit()
                                    else:
                                        cur.execute(f'update account set balance = balance-{transactionData[4]} where accountNumber = {transactionData[2]}')
                                        mydb.commit()                                  
                                else:
                                    raise NoSufficientBalance(transactionData[2],transactionData[4],transactionData[0])
                            else:
                                cur.execute(f'update account set balance = balance+{transactionData[4]} where accountNumber = {transactionData[3]}')
                                mydb.commit()
                        else:
                            raise InvalidAmount(transactionData[4],transactionData[0])
                    else:
                        raise InvalidAccount('Both',[transactionData[2],transactionData[3]],transactionData[0])
                else:
                    raise InvalidTransactionType(transactionData[1],transactionData[0])
                
                mydb.commit()
                
            except InvalidTransactionType as iv:
                print(iv)
                print(iv,file=logfiles.itt)
            except InvalidAccount as ia:
                print(ia)
                print(ia,file=logfiles.fian)
            except InvalidAmount as iam:
                print(iam)
                print(iam,file=logfiles.iam)
            except NoSufficientBalance as nsb:
                print(nsb)
                print(nsb,file=logfiles.nsb)
            except:
                print('Exception')
except:
    print('Exception')

finally:
    mydb.close()
    logfiles.close()
