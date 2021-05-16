#Python beginner course quiz 1

- You need to submit the python file that indicates each questions. 
- You have 1 hour to finish this quiz
- No internet or the pre-programmed code allowed.
- Good Luck :) 



#Question 1 (3 pt)
###what is the difference between pycharm, python, anaconda, appjar and kivy?
pycharm is a IDE it is a place where you code, and they help like color each codes .

kivy and appjar is a both python module that helps to build GUI for python.

anaconda is for managing modules for python

#Question 2 (1 pt)
###write a program that subtracts the age of yours and user?

```python
user = int(input("write your age here"))
my_age = 21

ans = my_age - user
print(ans)

```

#Question 3 (30 pt)
###write a program that helps people to add their age and name into the container, and find their name from it.


```python
name_container = []

while True:
    command = input("what is the command")
    
    if command == "input":
        user_name = input("write the username")
        age = input("write your age")
        human = [user_name, age]
        name_container.append(human)
        
    elif command == "output":
        user_name = input("write the username")
        
        for n in name_container:
            
            if n[0] == "user_name":
                print(n[1])
                break
                
        else:
            print("your name is not inside our database.")
            
    else:
        print("wrong comment, please try again.")
        

```


#Question 4 (3 pt)
###explain this code

```python

i = 0
while i < 100:

    if i * i == 67:
        print("found it")
        print(i)
        break

    i += 1

```

This code will check if the number is prime.
This code will not return found it, since it is not a prime number. 

#Question 5 (20 pt)
Now you are making a personal banking program.
The program need to ask user command, and do a job that they requested. 

- Bank owner has 5000 dollar in the account. 
- Greet the user with name when you start up the program
- If user type 'out', need to ask how much, and withdraw the money from the bank
- If user type 'in' need to ask how much and deposit the money from the bank
- If user type 'exit' need to exit the prgram and say 'good bye'

Rules
- The program cannot withdraw more than what she has.
- HINT: while True and break ;) 

```python
money_left = 5000

while True:
    user_input = input("hi, KUN. what do you want to do? ")
    
    if user_input == "out":
        money_out = input("how much would you like to withdraw: ")
        
        if money_out > money_left:
            print("too less money in your bank account")
            
        else:
            money_left - int(money_out)
            print("successful!")
            print("this is how much you have in your bank account", money_left)
            
            
    elif user_input == "in":
        money_out = input("how much would you like to put in: ")
 
        money_left + int(money_out)
        print("successful!")
        print("this is how much you have in your bank account", money_left)
        
    elif user_input == "exit":
        print("bye")
        break
        
    else:
        print("invalid input")
        
        

```

