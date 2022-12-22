#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
num1 =random.randrange(1000, 10000)
num1=str(num1)
n2 =input("Guess the 4 digit number:")
if (n2 == num1):
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    ctr = 0
    while (n2 != num1):
        if len(n2)<4 or len(n2)>4:
            n2=input("\nError! Enter a valid 4 digit number: \n")
        elif n2.isnumeric()==False:
            n2=input("\nError! Enter only digits from 0-9: \n")
        ctr += 1
        count = 0
        #n = str(n)
        #num = str(num)
        #print(type(n))
        correct = ['X']*4
        for i in range(0, 4):
            if (n2[i] == num1[i]):
                count += 1
                correct[i] = n2[i]
            else:
                continue

        if (count < 4) and (count != 0):
            print("Not quite the number. But you did get ",count, " digit(s) correct!")
            print("Also these numbers in your input were correct.")
            for k in correct:
                print(k, end=' ')
            print('\n')
            print('\n')
            n2 =input("Enter your next choice of numbers: ")
            

        elif (count == 0):
            print("None of the numbers in your input match.")
            n2 =input("Enter your next choice of numbers: ")
            

    if n2 == num1:
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")


# In[ ]:





# In[ ]:




