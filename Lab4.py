##Final Project (Lab 4)
##Johnathon Maschler
##December 17, 2020
##(12.7.20) Entry 1: 3:40 p.m. Start 5:15 p.m. End

#Project Euler: Problem 1 — Multiples of 3 and 5
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''

# def multiples3():
sumAll = 0 # set variable to zero to add the values to
for integer in range(1000): #use a for loop to iterate over all of the numbers 1000
    if integer%3 == 0 or integer%5 == 0: #for the numbers that have no remainder when divided by 3 or 5, add them to the sumAll variable
        sumAll = sumAll + integer #Continue to add them the variable sumAll
        # else:
        #     for integer in 1000:
        #         if integer%5 == 0:
        #             sumAll = sumAll + integer
print (sumAll) 

# __name__ == "__main__"
#     print (multiples3(sumAll))



#Even Fibonacci Numbers: Problem 2
'''By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

count = 0
num1 = 0
num2 = 1
nth = num1+num2
# nth = num1 + num2
# num1 = num2
# num2 = nth
while nth <= 4000000: #while the nth term is less than 4,000,000 I will continue to go through all of fibonacci's numbers
    # num1 = 0
    # num2 = 1
    nth = num1 + num2 #make sure to redefine each number everytime it loops through
    num1 = num2
    num2 = nth
    if nth %2 ==0: #make sure that we only add the numbers that are even to the total count
        count = nth + count
    else: #if it's not even just pass, don't add it
        pass

print (count) #our total number (it's correct)

'''———'''
##(12.26.20) Entry 2: 8:00 p.m. Start 9:40 p.m. End
#Largest Prime Factor: Problem 3
'''What is the largest prime factor of the number 600851475143'''

# bignum = int(600851475143)


# def prime(bignum):
#     listprime = []
#     for numero in range(2, bignum):
#         if bignum % numero != 0:
#             listprime.append(numero)
#         else:
#             pass
# def largestPrime(bignum):
#     result = []
#     for something in range(2, bignum):
#         if Prime(something):
#             if bignum % something == 0:
#                 result.append( something )
#     return result

# print (largestPrime(bignum)) GETS STUCK IN LOOP EVERYTIME — Does not work

'''had to look up the different possible ways to find largest prime factors and then converted it to code here'''
import math # in order to find the largest square root

possibleNums = [] #need an empty list that we will eventually pull the factor out of
bignum = 600851475143

for numero in range(2, math.ceil(math.sqrt(bignum))): #finding the square roots of bignum that is still perfectly divisible by itself
    # print ('printingn it' , numero) bad idea it's just printing every number lol
    while bignum % numero == 0: #see comment on line above
        bignum=bignum/numero #redefine what bignum is equal to each time in order to eventually find the greatest prime factor
        possibleNums.append(numero) # every time a number is perfectly divisible by bignum it will get added to the list

# print(possibleNums) #prints a list of all four of the possible numbers but we want the greatest one so print just the last one

print(possibleNums[3]) #should be the greatest prime factor


##(01.08.21) Entry 3: 10:30 a.m. Start 12:20 p.m. End
#Largest Palindrome Product: Problem 4:
'''Find the largest palindrome made from the product of two 3-digit numbers.'''

# largelist = list(range(999))
# largelist = largelist[::-1]


#     for i in largelist:
#         if largelist[i]*largelist[i+1] != reverse.str(largelist[i]*largelist[i+1]):
#             palindrome = Tr
# def palindrome(sum): #I had tried to define it as a function but either way I was unable to product an answer
#although I cannot find the error in this code

product = 0 #the value of product will change
for a in range(999, 100, -1): #will iterate through each number starting from greatest
    for b in range(a, 100, -1): #while also comparing them with a
        x = a * b #it will constantly test each time a is multiplied by b
        if x > product:
            s = str(a * b) #convert it to a string
            if product == s[::-1]: #test to see if it's a palindrome
                product = a * b #then print product
print('product: ', product)
                    



#Smallest Multiple: Problem 5:
'''What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
small = 1
while True: #using a while loop, I find the smallest divisible number with an if statement that keeps
    #adding to 'small' until 'small' is evenly divisible by every number that I put in the if statement
    if small%1==0 and small%2==0 and small%3==0 and small%4==0 and small%5==0 and small%6==0 and small%7==0 and small%8==0 and small%9==0 and small%10==0 and small%11==0 and small%13==0 and small%14==0 and small%15==0 and small%16==0 and small%17==0 and small%18==0 and small%19==0 and small%20==0:
        break
    else:
        small = small+1 #if it isn't evenly divisible then it will keep adding 1 to 'small' until it equals True
print (small) #the problem is that this method takes over thirty seconds to calculate an answer


#Sum Square Difference: Problem 6:
'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

def sumSquare (ans): #function to find the sum of the squares
    integer = 0
    for x in range(1, ans+1): #this will loop through each number within the inputted number 'ans'
        integer = integer + (x*x) #redefine integer as integer + x squared. Keep adding these up for as many integers as possible
        # print (integer) #test
    return (integer)
# print(sumSquare(100)) 

def squareSum (sum): #function for the square of the sums 1-100
    integer = 0 #essentially the exact same as the previous function
    for x in range(1, sum+1):
        integer = integer + x #instead of adding x squared we just add x and this will be the sum of the numbers 1-100
    return integer
    
answe = ((squareSum(100))**2)#couln't figure out how to square it within the function so squared the sums here
print (answe - sumSquare(100))# final answer (correct)


#10001st Prime: Problem 7:
'''What is the 10,001st prime number?'''
from math import sqrt
def maybePrime(x): #function to make sure that the integer is a prime number
    if x<=2: #covering all the possible conditions for which it could be a prime number
        return False
    if x==3 or x==2: #these are obvious primes
        return True
    for q in range(2, int(sqrt(x)) + 1): #if the square root is evenly divisible by two then it can't be prime
        if x % q == 0:
            return False
    return True #True means that it is prime
print(maybePrime(119173)) #Test

'''I need to play around with this code because it prints out a prime number
the problem is it isn't the right number...'''
def nthPrime (x):
    count = 0 #will continue to add to this until the count reaches 10,001st prime number
    integer = 2 #start with the smallest prime number
    while count != x: #enter a loop until x = 100001
        integer = integer+1 #keep adding one until we get count to be 100001
        if maybePrime(integer) == True: #make sure that the number is prime
            count = count + 1 #if it's prime we add one to our count
            if count == x: #once the count makes it to the xth prime number then we will exit the loop and return the prime integer
                return integer

print(nthPrime(10001))



#Largest Product in a series: Problem 8:
'''Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?'''

num = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

possibleProducts=[] #start with an empty list to add all the possible values into
for i in range(0,len(num)-12): #iterate through each number and -12 so the string index does not go out of range
    consecutive=int(num[i])*int(num[i+1])*int(num[i+2])*int(num[i+3])*int(num[i+4])*int(num[i+5])*int(num[i+6])*int(num[i+7])*int(num[i+8])*int(num[i+9])*int(num[i+10])*int(num[i+11])*int(num[i+12])
    possibleProducts.append([consecutive]) #every possible product of 13 consecutive digits
# print(list1)#test
print('product: ',(max(possibleProducts))) #using the max function it will pull out the largest number for me


#Special Pythagorean Triplet: Problem 9:
'''There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

def pythTriplet(): #define a function. I had made the error of calling on a, b, c but this was erroneous as I would realize
    for a in range(1, 1000):#iterates through each number until a,b and c are satisfied
        for b in range(1, 1000):
            c = 1000-a-b
            # for c in range(1, 1000): #instead of including a third for loop, I just made it simple b/c c has to equal 1000-a-b
            if a*a + b*b == c*c: #once this command returns True then the for loops stop iterating through the ranges
                return a*b*c #this is the triplet that will be printed out
            # print (a+b+c) #test (it equals 1000 but prints it out many times—as many times as the for loop loops)
print (pythTriplet())


#Summation of Primes: Problem 10:
'''Find the sum of all the primes below two million.'''
'''I just made use of the function I wrote earlier to find prime numbers'''

from math import sqrt
def maybePrime(x): #function to make sure that the integer is a prime number
    if x<=2: #covering all the possible conditions for which it could be a prime number
        return False
    if x==3 or x==2: #these are obvious primes
        return True
    for q in range(2, int(sqrt(x)) + 1): #if the square root is evenly divisible by two then it can't be prime
        if x % q == 0:
            return False
    return True #True means that it is prime

sum = 0 #going to keep adding prime numbers to this
for i in range(2, 2000000): #iterate through each number
    if maybePrime(i):#if the function says that that particular number is prime then it will get added to our 'sum'
        sum = sum+i
print(sum)

#Largest Product in a Grid: Problem 11:
'''What is the greatest product of four adjacent numbers in
the same direction (up, down, left, right, or diagonally) in the 20×20 grid?'''

'''wow this is a really interesting problem that I'm not sure I can really wrap my head around just yet!'''
