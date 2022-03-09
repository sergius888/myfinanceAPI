# 1. Write a Python program to get the Python version you are using.

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

# 2. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
# Sample numbers list :

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]

for x in numbers:
    if x == 237:
        print(x)
        break
    elif x % 2 == 0:
        print(x)


# Exercise 2: Print the sum of the current number and the previous number

# my solution
for n in range(1, 10):
    current = n
    previous = n - 1
    sum = current ++ previous
    print("Current numbers is", current, "Previous number is", previous, "Sum is", sum)

# online solution

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    # modify previous number
    # set it to the current number
    previous_num = i



# Exercise 3: Remove first n characters from a string

strng = "I will try to avoid the letter for now but what if I have another n?"

first_n = strng.index("n")
remove = strng[first_n:][1:]

print(remove)

# bottom line - my coding "skills" in a nutshell
# import webbrowser
# webbrowser.open('https://i.imgflip.com/2r3xxq.jpg')

