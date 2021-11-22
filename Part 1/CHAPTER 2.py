#if statement
name = 'mary'
password = 'swordfish'
if name == 'mary':
    print('hello, mary')
    if password== 'swordfish':
        print('acces granted')
    else:
        print('wrong password')

#elif statement
name = 'carol'
age = 3000
if name == 'alice':
    print('hi alice')
elif age<12:
    print('you are not Alice kiddo')
elif age > 100:
    print('you are not alice granny')
elif age >2000:
    print('unlike you alice is not undead immortal vampire!')
#while loop
spam = 0
while spam <5:
    spam += 1
    print('Hello world '+ str(spam))






