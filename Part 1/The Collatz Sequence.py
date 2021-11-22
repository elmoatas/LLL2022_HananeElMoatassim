def collats(number):
    if number%2 == 0:
        return number
    elif number%2 == 1:
        return number*3 +1
print ('geef een nummer')
n = int(input())
print(str(collats(n)))