import sys
x = int(input("enter 'sum' of number : "))            #18
y = int(input("enter how many digit you want : "))    #2

digits = int(('9' * y))                               #99


def getSum(x,y,digits):

    if x<= 9*int(y):                                 #if y= 2-----> 1>=x>=18
        sum = 0
        for digit in str(digits):
            sum += int(digit)
        return sum, digits
    else:
        print(f"For {y} digit number 'sum' should be less than {9*y} ")
        sys.exit(0)                             #break---end of execution


result = getSum(x,y,digits)                     #assigning return value
my_sum = result[0]                              #unpacking
digits = result[1]                              #unpacking
while True:
    if x == my_sum:                             #if 'sum' = 18
        break
    else:
        digits = int(digits) - 1                #99-1 = 98
        reduced = getSum(x,y,digits)            #assign= call for count sum
        my_sum = reduced[0]                     #assigning reduced--> 17


add = list(str(digits))
print(f"List of digits ---> {add}")
print(f"Answer (highest number) : {digits}")

