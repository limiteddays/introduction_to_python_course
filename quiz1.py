#Question 1)
#write a program that can calculate the difference between your age and some user

user = int(input())
your_age = 21

print(your_age - user)

#Question 2)
#do a while loop and ask user to put their name in every time and save it.
#if their name is admin, get a number of users who typed their name.

name_container = []
while True:

    user_name = input("write your username")

    if user_name == "admin":
        print(name_container)
        break

    name_container.append(user_name)
    print("okay name saved")

#question 3)
#explain this code

# user = input()
# container = []
# container.append(user)
# print(container)

#first, we put the user name as a value
#then put the name inside the list called container.

#Question 4)
#what is the difference between = and ==

#one checks if it is equal
# one sets the variable.


#Question 5)
#now you are creating a bank application.
#use appjar and create button - send, recieve, and show how much moeny that they have.