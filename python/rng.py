from random import randint

min_number=int(input("enter a min number:"))
max_number=int(input("enter a max number:"))

if(max_number<min_number):
    print("Invalid input-shutting Down")
else:
    rnd_number= randint(min_number,max_number)
    print(rnd_number)