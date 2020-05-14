#Bank Exception Using functions
import CustomException as ce
from LoggerFiles import LoggerFiles
import sqlite3


mydb = sqlite3.connect('bankproj.db')
cur = mydb.cursor()
minimumBalance = 1000

def checkTransactionType(lst):
    if lst[1] in ['Transfer','Deposit','Withdraw']):
        return True
    else:
        raise ce.InvalidTransactionType(lst[1],lst[0])

def checkAccountNumber(lst):
    if lst[1] == 'Withdraw':
        cur.execute(f'select count(*) from account where accountNumber = {lst[2]}')
        if(cur.fetchone()[0]==1):
            return True
        else:
            raise ce.InvalidAccount('Withdraw',lst[2],lst[0])      
    elif lst[1] == 'Deposit':
        cur.execute(f'select count(*) from account where accountNumber = {lst[3]}')
        if(cur.fetchone()[0]==1):
            return True
        else:
            raise ce.InvalidAccount('Deposit',lst[3],lst[0]) 
    elif lst[1] == 'Transfer':
        cur.execute(f'select count(*) from account where accountNumber in ({lst[3]},{lst[2]})')
        if(cur.fetchone()[0]==2):
            return True
        else:
            raise ce.InvalidAccount('Both',[lst[2],lst[3]],lst[0])

def checkBalance(lst):
    if lst[1] in ['Withdraw','Transfer']:
        cur.execute(f'select balance from account where accountNumber={lst[2]}')
        if(cur.fetchone()[0]-lst[4]>=minimumBalance):
            return True
        else:
            raise ce.NoSufficientBalance(lst[2],lst[4],lst[0])

def checkAmount(lst):
    if lst[4]>0:
        return True
    else:
        raise ce.InvalidAmount(lst[4],lst[0])

loggerfiles = LoggerFiles()

if __name__=='__main__':
    try:
        with open('TransactionFile.csv','r') as ft:
            for transaction in ft:
                dataList = transaction.strip().split(',')
                checkTransactionType(dataList)
                checkAccountNumber(dataList)
                checkBalance(dataList)
                checkAmount(dataList)
                
                '''
                Transaction Perform
                '''
    
    except ce.InvalidTransactionType as iv:
        print(iv)
        print(iv,file=logfiles.itt)
    except ce.InvalidAccount as ia:
        print(ia)
        print(ia,file=logfiles.fian)
    except ce.InvalidAmount as iam:
        print(iam)
        print(iam,file=logfiles.iam)
    except ce.NoSufficientBalance as nsb:
        print(nsb)
        print(nsb,file=logfiles.nsb)
    except:
        print('Exception')






