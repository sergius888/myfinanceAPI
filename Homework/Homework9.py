
#This exercises are for the input function
#you can play a little with the function here https://www.w3schools.com/python/ref_func_input.asp

#ex1
# take 2 numbers from the user
# print the sum back

a = int(input("Please pick the first number: "))
b = int(input("Now the second number: "))
sum = a + b
print("The sum of your numbers is", sum)


#ex2
# take 3 numbers from the user
# print the biggest one

num1 = input("first number ")
num2 = input("second number ")
num3 = input("third number ")
# print(max(num1, num2, num3))
list = [num1, num2, num3]
def biggest(data):
    max_value = data[0]
    for x in data:
        if max_value < x:
            max_value = x
    return max_value
print("The biggest number is", biggest(list))



# ex3
# ask the user's name
# ask him his age
print if he is allowed to drink

name = str(input("What is your name? "))
age = int(input("How old are you? "))
if age >= 18:
    print("Thank you", name + ",", "you are allowed to drink")
else:
    print("Sorry, come back in", 18 - age, "years")

# ex4
# ask the user for at least 5 words
# put them in a sentence

input_string = input("Enter at least 5 words separated by comma ")
words_list = input_string.split(",")
if len(words_list) < 5:
    print("You have to input at least 5 words")
else:
    sentence = " ".join(words_list)
    print(sentence)


#ex5
import random
x = random.randint(0, 9) #this will pick a random number between 0 and 9
#create a guessing game, the user must tell a number between 0 and 9 and you must tell him if he guessed it
guess = int(input("Guess a number between 0 and 9"))
if guess == x:
    print("You guessed the number")
else:
    print("You did not guess the number. The correct number was", x)
