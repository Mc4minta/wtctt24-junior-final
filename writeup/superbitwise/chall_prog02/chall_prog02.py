from libnum import *
import hashlib

def secret(a, b):
    result = 0
    is_negative = (a < 0) ^ (b < 0)  
    a, b = abs(a), abs(b)

    while b > 0:
        if b & 1:  
            result = result + a + 1
        a = a*2 
        b >>= 1  

    return -result if is_negative else result

def hint1():
    print( 'secret num is in range(0,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)')
def hint2():
    print(f'{secret(10,0b111) = }')
    print(f'{secret(10,0b1111) = }')
    print(f'{secret(10,0b11111) = }')
    print('secret(secret_num,65535) = 3338190210085793296455519657559881806177254504039477189883619618747088635044397372904871283091')
    print('secret(secret_num,65536) = 3338241147603304333203768006070716625461700635946153614346729157461039151388870469683278315521')
    print('This is upgrade bitwise multiplication!')
    
hint1()
hint2()
print('Let Guess the number!\n')
while True:
    secret_num=int(input("Enter secret number: "))
    check_hash='e554944164cba617ca6fa6575af5f7b8367430abcc806b11e553f30375549040'
    if hashlib.sha256(str(secret_num).encode('utf-8')).hexdigest() == check_hash:
        print('Correct secret!')
        print(n2s(secret_num).decode())
        break
    else:
        print('Incorrect secret!')