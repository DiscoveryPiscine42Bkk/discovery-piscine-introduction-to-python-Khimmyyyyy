import random #add libary random
print('Welcome to the Guess the Number game!\n')# /n is the space between the line
print('I have generated a secret number between 1 and 100. You have 5 guesses.\n :') #i tere is no / then it will display only I
n = 5
real = random.randint(1,100)#1,100 is the range of number
max = 100
min = 1
while n > 0 :# n is the number of tries
    print('Attempts left:', n)
    n = n - 1# minus 1 every time bc minus the number of tries left
    x = eval(input('Enter your guess:'))
    if x == real :# if the number they put is correct n will be -1 so the game will stop
        n = -1
        print('Your guess is correct. The secret number is',real)
    elif x < real and x >= min and n > 0:# and is here bc mun tong mee all 3 conditions
        min = x + 1# if guess 10 and the number is more than that it will reduce the range
        print('Your guess is not correct. The secret number is beteen', min,'and',max,'\n')
    elif x < real and x <= min and n > 0 :
        print('That number is not within the range. Please enter a number more than', min, '\n')
    elif x > real and  x <= max and n > 0:
        max = x - 1
        print('Your guess is not correct. The secret number is beteen', min,'and',max,'\n')
    elif x > real and x >= max and n > 0:
        print('That number is not within the range. Please enter a number less than', max, '\n')
    elif x != real and n == 0:
        print('The secret number is', real)