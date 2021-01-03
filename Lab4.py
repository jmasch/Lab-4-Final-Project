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
