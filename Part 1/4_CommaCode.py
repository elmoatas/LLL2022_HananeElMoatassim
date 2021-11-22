spam =[]
while True:
    print('vul woord in ' + str(len(spam)+1)+
    ' (klik op enter om te stoppen.):')
    woord= input()
    if woord =='':
        break
    spam+= [woord]
print(*spam, sep=',')