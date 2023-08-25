print("welcome to the rollercoster!")
height=int(input("What is your height in cm?"))
bill=0

if height >= 120: 
    print("you can ride the rollercoster!")
    age=int(input("enter your age"))
    if age < 12:
        bill=5
        print("Child tickets are $5.")
    elif age<18:
        bill=7
        print("Youth tickets are $7.")
    else:
        bill=12
        print("Adults tickets are $12.")

    wants_photo=input("do you want a photo taken? Y or N ")
    if wants_photo == "Y":
     bill +=3

    print(f"your final bill is {bill}")
else: 
    print("sorry you have to grow taller before you can ride")