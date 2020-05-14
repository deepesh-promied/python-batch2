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