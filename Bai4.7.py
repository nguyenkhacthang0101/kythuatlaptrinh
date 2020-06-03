import math

def isPrimeNumber(n):
    if (n<2):
        return False
    squareRoot =  int(math.sqrt(n));
    for i in range(2, squareRoot + 1):
        if (n%i == 0):
            return False
n = int(input("Nhap cac soduong: "))
print("Tat ca so nguyen to nho hon ",n,"la ");
sb = ""
if (n>=2):
    sb = sb+"2"+" "
for i in range(3,n+1):
    if (isPrimeNumber(i)):
        sb = sb + str(i) +" "
    i = i+2
print(sb)
    
