# Python function to find a range of primes
def findprimes(min, max):
    for Number in range(min, max + 1):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if (Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(" %d" % Number, end='  ')
print()

def primes():
    minimum = int(input("Enter the minimum value: "))
    maximum = int(input("Enter the maximum value: "))
    findprimes(minimum, maximum)



if __name__ == "__main__" :
    #Imperative
    primes()
