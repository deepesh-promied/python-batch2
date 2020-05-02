#Function With Parameters
'''
def <functionName>(<parameters>):
    stat 1
    stat 2
    ...
    stat n
'''

def calcCommision(lsales,nsales,isales):
    sales = lsales + nsales + isales
    comm = sales*.05
    role = 'Average'
    if sales>=10000:
        role = 'Star Performer'
    return [comm,role]

if __name__ == '__main__':
    x = calcCommision(5000,2000,3000)
    print(x)
    y = calcCommision(50000,0,0)
    print(y)
    print(calcCommision(8000,200,0))
