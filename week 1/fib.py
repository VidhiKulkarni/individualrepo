#Fibonacci
def fib():
    num = int(input("Enter a number for fibonacci:")) #User Input
    try:
      num >= 0 #try to see if input is greater than or equal to 0
      if num < 0: #if input is less than 0
        print("Sorry, fibonacci does not exist for negative numbers") # Tell user that input must be positive
    except:
        print("You have not entered a integer. Please enter an integer.") #Tell user that input must be an integer
    else:
        def recursion(num): #
           if num <= 1: # if number is 0,1 return number
             return num #return number if these are the inputs
           else:
             return((num-1) + (num-2)) #return -1 and -2 of number
        for j in range(num):
            print(recursion(j)) #print final product

fib()


# def fibonacci(num):
#   first = 0
#   second = 1
#   count = 0
#   if num == 1:
#     print(first)
#   else:
#     while count < num:
#       print(first)
#       nth = first + second
#       first = second
#       second = nth
#       count += 1

  



# userinput(num)
