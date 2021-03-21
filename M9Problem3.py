#Miguel Rodriguez
#March 21,2021
#CSS 225 Lab Activity 9
#Write a program that generates a random number, then prints one of the following:
#If the number is divisible by 3, print “Fizz”
#Elif the number is divisible by 5 print “Buzz”
#Otherwise, print just the number


for i in range(1,100):
    if i % 3==0:
        print("Fuzz")
    elif i % 5==0:
        print("Buzz")
    else:
        print(i)
