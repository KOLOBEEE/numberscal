import random



score = 0
questions = 0

print("are you ready to be tested? ")
answer = input("please enter y to continue or n to exit: ")

while answer == "y":
    break
else:
    print("thank you. see you next time! ")


operation_keys = ["+", "-", "/", "*"]


num1 = random.randint(0,10)
num2 = random.randint(0,10)

print("you are now going to answer 5 questions: ")
print("these questions will be random.")

while questions < 5:
    operation_keys = random.choice(operation_keys)
    question = "{} {} {}".format(num1, operation_keys, num2)
    print("what is " +str(num1) + str(operation_keys) + str(num2))

    result = input()

    if result == (num1, operation_keys, num2):
        print("correct!")
        score = score +1
    
    else:
        print("incorrect!")


questions()



