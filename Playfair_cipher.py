import numpy as np

def encrypt(x,y):
    xx=x
    yy=y

    i=np.argwhere(array_matrix == x)
    j=np.argwhere(array_matrix == y)
    
    if(i[0][1]==j[0][1]):
        i1=(i[0][0]+1)%5
        j1=(j[0][0]+1)%5
        x=array_matrix[i1][i[0][1]]
        y=array_matrix[j1][j[0][1]]
    
    elif(i[0][0]==j[0][0]):
        i1=(i[0][1]+1)%5
        j1=(j[0][1]+1)%5
        x=array_matrix[i[0][0]][i1]
        y=array_matrix[j[0][0]][j1]
      
    else:
        x1=i[0][1]
        y1=j[0][1]
        x=array_matrix[i[0][0]][y1]
        y=array_matrix[j[0][0]][x1]
    print(xx+yy,"->",x+y)  
    return x+y

def decrypt(x,y):
    xx=x
    yy=y

    i=np.argwhere(array_matrix == x)
    j=np.argwhere(array_matrix == y)
    if(i[0][1]==j[0][1]):
        i1=(i[0][0]-1)%5
        j1=(j[0][0]-1)%5
        x=array_matrix[i1][i[0][1]]
        y=array_matrix[j1][j[0][1]]

    elif(i[0][0]==j[0][0]):
        i1=(i[0][1]-1)%5
        j1=(j[0][1]-1)%5
        x=array_matrix[i[0][0]][i1]
        y=array_matrix[j[0][0]][j1]
      
    else:
        x1=i[0][1]
        y1=j[0][1]
        x=array_matrix[i[0][0]][y1]
        y=array_matrix[j[0][0]][x1]
    print(xx+yy,"->",x+y)  
    return x+y

plaintext = input("Enter the plaintext\n")
key = input("Enter the key\n")
key = key.upper()
plaintext = plaintext.upper()
if(len(plaintext)%2 != 0):
    plaintext+='Z'

arr = []
i=0
p=[]
while(i<len(plaintext)-1):
    if(plaintext[i] !=" "):
        if(plaintext[i]==plaintext[i+1]):
            p.append(plaintext[i]+"X")
            i+=1     
        else:
            p.append(plaintext[i]+plaintext[i+1])
            i+=2

for ele in key:
    if ele not in arr:
        if ele == 'J':
            arr.append('I')
        else:
            arr.append(ele)

for i in range(65,91):
    if chr(i) not in arr:
        if i == 74:
            pass
        else:
            arr.append(chr(i))

array_matrix = np.array(arr)
array_matrix = array_matrix.reshape(5,5)

print(array_matrix)

print("Encrypting the data..\n ") 
enc=[]
for i in p:
    enc.append(encrypt(i[0],i[1]))
print("\nEncrypted data =","".join(enc))
n = int(input("Enter 1 to decrypt the cipher text\n"))
if n == 1:
    print("Decrypting the data...\n ")
    dec=[]
    for i in enc:
        dec.append(decrypt(i[0],i[1]))
    print("\nDecrypted data =","".join(dec))
else:
    exit(0)