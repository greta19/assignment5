'''
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int=0

while num_int>=0:
    if num_int>max_int:
        max_int=num_int
    num_int = int(input("Input a number: "))
    
print("The maximum is", max_int)    # Do not change this line



'''

n = int(input("Enter the length of the sequence: ")) # Do not change this line

i=4

if n==1:
    print(n)
elif n==2:
    print(1,2)
elif n==3:
    print(1,2,3)
else:
    print(1)
    print(2)
    print(3)
    
    a=1
    b=2
    c=3
    
    while i<=n:
        tala=a+b+c
        print(tala)
        a=b
        b=c
        c=tala
        
        i=i+1
    
