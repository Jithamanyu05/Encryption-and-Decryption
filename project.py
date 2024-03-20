# ---Code---
fp = open("file1.txt","x")
fp = open("encrypted.txt","x")
fp = open("decrypted.txt","x")

# writing data into file1 which will be encypted

fp = open("file1.txt","w")
x = input("Enter the string ypu want to encrypt : \n")

fp.write(x)

# generating a random number to shift the charcters by those many places.
import random as ran
num = ran.randint(1,20)
print(num)

# ----encryption algorithm----

fp = open("file1.txt","r")
st = fp.read()
fp.close()
# shifting alphabet positions by 'num' positions
encstr = ""
for char in st:
    if char.isupper():
        base = ord('A')
        enchar = chr((ord(char)- base + num) % 26 + base)
        encstr = encstr + enchar 
    elif char.islower():
        base = ord('a')
        enchar = chr((ord(char)- base + num) % 26 + base)
        encstr = encstr + enchar 
    elif char == ' ':
        encstr = encstr + ' '
    else:
        enchar = chr((ord(char) + num))
        encstr = encstr + enchar
           
    
# storing the encrypted string in encypted.txt

fp = open("encrypted.txt","w")
fp.write(encstr)
fp.close()

# ----decryption algorithm---

fp = open("encrypted.txt","r")
st = fp.read()
fp.close()
decstr = ""
for char in st:
    if char.isupper():
        base = ord('A')
        dechar = chr((ord(char)- base - num) % 26 + base)
        decstr = decstr + dechar 
    elif char.islower():
        base = ord('a')
        dechar = chr((ord(char)- base - num) % 26 + base)
        decstr = decstr + dechar
    elif char == ' ':
        decstr = decstr + ' '
    else:
        dechar = chr((ord(char) - num))
        decstr = decstr + dechar
    
# storing the decrypted data into the decrypted file

fp = open("decrypted.txt","w")
fp.write(decstr)
fp.close()
