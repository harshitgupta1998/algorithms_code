# Understand the concept of big number and how to handle the carry and store them in the variable
import sys
def fact(n):
    # define an answer list
    res=[None]*500
    # intialise the values
    res[0]=1
    res_size=1
    x=2
    # iterative call the function
    while x<=n:
        res_size =multiply(x,res,res_size)
        x+=1
    i=res_size-1
    # print the value in reverse to get the answer
    while i >= 0:
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i = i - 1

def multiply(x,res,res_size):
    # intialize the value
    carry=0
    i=0
    # Iterative store the res and add carry
    while i<res_size:
        prod=res[i]*x+carry
        res[i]=prod&10
        carry=prod//10
        i+=1
    # If the res_size is done and carry is still present
    while(carry):
        res[res_size]=carry%10
        carry//=10
        res_size+=1
    return res_size


fact(100)