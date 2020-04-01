#Program to covert Fahrenheit to Celsius
'''
C = (F-32)*5/9
f = C*9/5+32
bodmas: Brackets Of Division Multiplication Addition and Subtraction
'''

print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

opt = int(input("Enter your Choice: "))

if opt==1:
    # FtoC
    ftemp = float(input("Enter the Fahrenheit Value: "))
    ctemp = (ftemp-32)*5/9
    print()
    print("You Entered {0} F. {0} Fahrenheit is {1} Celsius".format(ftemp,ctemp))
    print()
elif opt==2:
    #CtoF
    ctemp = float(input("Enter the Celsius Value: "))
    ftemp = (ctemp*9/5)+32
    print()
    print("You Entered {0} C. {0} Celsius is {1} Fahrenheit".format(ctemp,ftemp))
    print()
else:
    print("Invalid Choice. Please Execute Again!")
