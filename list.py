from os import close


james = open('james2.txt')
julie = open('julie2.txt')
mikey = open('mikey2.txt')
sarah = open('sarah2.txt')

def sanitize(data):
    data = james.readline()
    return data

print(sanitize(james))
# print(james.readline())
# print(julie.readline())
# print(mikey.readline())
# print(sarah.readline())