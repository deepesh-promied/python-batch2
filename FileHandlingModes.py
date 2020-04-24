try:
    with open('filepractice9.txt','x+') as fp:
        fp.write('This is a demo text in xclusive mode')
        fp.seek(5)
        x = fp.read()
        print(x)
except FileExistsError:
    print('File Already Exists')
except ZeroDivisionError:
    print('Zero Division Error')
except:
    print('All Exceptions')
else:
    print('In the else block')
finally:
    fp.close()