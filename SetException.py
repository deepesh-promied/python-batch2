try:
    set1 = set([12,24,56,67,78,78])
    print(set1)
    set1.remove(68)
except ZeroDivisionError:
    print('Zero Division Exception')
except:
    print('All Exceptions')