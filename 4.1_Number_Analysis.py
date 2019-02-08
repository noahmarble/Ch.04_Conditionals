'''
NUMBER ANALYSIS PROGRAM
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program

In: 32
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''
number=int(input("input a number:"))

evenorodd = number%2                    #even or odd test
if evenorodd == 1:
    print("test 1: odd")
else:
    print("test 1: even")
                                         # pos, neg, or zero test
if number == 0:
    print("test 2: zero")
elif number < 0:
    print("test 2: negative")
elif number > 0:
    print("test 2: positive")
                                    #inclusively between -100 and 100 test
if -101 < number < 101:
    print("test 3: inclusive")
else:
    print("test 3: exclusive")