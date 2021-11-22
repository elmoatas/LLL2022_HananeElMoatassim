# spam =['cat', 'bat', 'rat', 'elephant']
# print(spam[2])
# print(spam[-2])
# print(spam[0:3])
# print(len(spam))
# spam[1]= 'aardvark'
# print(spam[1])
# del spam[1]
# print(spam)
# catNames=[]
# while True:
#     print('Enter the name of cat ' + str(len(catNames)+1)+
#           ' (Or enter nothing to stop.):')
#     name= input()
#     if name =='':
#         break
#     catNames = catNames + [name]
# print ('the cat names are:')
# print (catNames)
# for name in catNames:
#     print(' '+ name)

# for i in range (4):
#     print(i+1)

# supplies = ['pens','staplers','flame-throwers', 'binders']
# for i in range ( len(supplies)):
#     print ('Index ' + str(i +1) + ' in supplies is: ' + supplies [i])
# print('cat' in supplies)
# print('cat' not in supplies)

# cat =['fat','black', 'loud']
# size, color, disposition = cat

# spam =['hello', 'hi', 'howdy', 'heyas']
# print(spam.index('hello'))

spam =['cat', 'dog', 'bat']
spam.append('moose')
def printSpam():
    for i in range (len(spam)):
        print(spam[i])
printSpam()
spam.insert(1, 'chicken')
printSpam()
spam.remove('bat')
printSpam()
spam.sort(reverse =True)
printSpam()