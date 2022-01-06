def gcd(a, h):
    while (1):
        temp = a%h
        if (temp == 0):
          return h
        a = h
        h = temp

p = 17
q = 11
n = p*q
e = 7
phi = (p-1)*(q-1);
while (e < phi):
    if (gcd(e, phi)==1):
        break;
    else:
        e+=1
d = pow(e,-1,phi)
message = input("\nEnter the message\n")
try:
    message = int(message)
    c = pow(message, e)%n
    print("\nEncrypted data =", c)
    m = pow(c, d)%n
    print("\nOriginal Message Sent = ", m)
    print()
except:
    enc = []
    for i in message:
        if i == " ":
            c = pow(32, e)%n
            enc.append(c)
        else:
            c = pow(ord(i), e)%n
            enc.append(c)
    print("\n\nEncrypted value =",enc)
    print("\n\n------- Decrypting -------\n\n")
    dec=[]
    for i in enc:
        m = pow(i, d)%n
        dec.append(m)
    org=""
    for i in dec:
        if i == 32:
            org += " "
        else:
            org += chr(i)
    print("Original message =",org)
    print()