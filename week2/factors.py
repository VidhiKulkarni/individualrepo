def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()


def tester():
  class factors:
    def __init__(self):
      return
    def __call__(self, n):
      if isinstance(n, int) == True and 0 < n and n < 10000:
        x = n
        temp_list = []
        final_list = []
        for i in range(x):
          while 0 < x:
            temp_list.append(x)
            x = x - 1
        #print(temp_list) all the numbers before n
        for i in range(n):
          if n % temp_list[i] == 0:
            final_list.append(temp_list[i])
        return final_list
      else:
        print("input was not valid: ")
        # return"null"
  factors_test = factors()
  
  print("1 factors = ",factors_test(1))
  print("5 factors = ",factors_test(5))
  print("50 factors = ",factors_test(50))
  print("0 factors = ",factors_test(0)) #no 0
  print("-1 factors = ",factors_test(-1)) #no negative numbers
  print("99999999999 factorial = ",factors_test(99999999999)) #too large
  print("25.5 factorial = ",factors_test(25.5)) #no decimals allowed
  print("V factorial = ",factors_test("V"))  #no alphabets allowed
  
tester()
