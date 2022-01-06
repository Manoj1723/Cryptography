plaintext = input("Enter the plaintext\n")
ciphertext = ""
K = 3
for i in plaintext:
    if i != " ":
        ciphertext += chr(((ord(i)-97+K)%26)+97)
    else:
        ciphertext += " "
print("Encrypting the data..\n ")
print("Ciphertext => ",ciphertext)
n = int(input("Enter 1 to decrypt the cipher text and know the key\n"))
if n == 1:
    print("Decrypting the data...\n ")
    k = 0
    plaintext_dec = ""
    c = 1
    while(c == 1):
        k +=1
        for i in ciphertext:
            if i != " ":
                plaintext_dec += chr(((ord(i)-97-k)%26)+97)
            else:
                plaintext_dec += " "
        print(plaintext_dec)
        c = int(input("Enter 1 if the plaintext isn't obtained\n"))
        plaintext_dec = ""
    print("Key =",k)
else:
    exit(0)