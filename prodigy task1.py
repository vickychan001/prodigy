def encryption(text,key):
    e=''
    for i in text:
        if i.isupper():
            e=e+chr((ord(i)+k-65)%26+65)
        elif i.islower():
            e=e+chr((ord(i)+k-97)%26+97)
        else:
            e=e+i
    return e
def decryption(text,key):
    d=''
    for i in text:
        if i.isupper():
            d=d+chr((ord(i)-k-65)%26+65)
        elif i.islower():
            d=d+chr((ord(i)-k-97)%26+97)
        else:
            d=d+i
    return d

ptext=input("Enter a plaintext: ")
k=int(input("Enter the key value: "))
ptext=encryption(ptext,k)
print("the cipher text: ",ptext)
etext=input("Enter a encryptedtext: ")
k=int(input("Enter the key value: "))
etext=decryption(etext,k)
print("the plain text: ",etext)

