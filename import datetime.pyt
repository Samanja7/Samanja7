import datetime

day=int(input("Enter the day(DD) : "))
month=int(input("Enter the Month(MM) : "))
yr=int(input("Enter the Year(YYYY) : "))


Aquarius="""
Aquarius are strange set of people
They are MAd and Crazy
"""
Pisces="""
Pisces signs have a peaceful and gentle presence about them, with an uncanny ability to tap into the emotions of the collective. They're extremely malleable and need to be careful of who they surround themselves with. Since they are hyper-intuitive, they can sometimes become disconnected–making it important for this water sign to ground often.
"""


x= datetime.datetime.now()
print(x)


if month>=1 and month<=2:
    if month==1 and day>=20:
        print(Aquarius)
    elif month==2 and day<=18:
        print(Aquarius)

if month>=2 and month<=3:
    if month==2 and day>=19:
        print(Pisces)
    elif month==3 and day<=20:
        print(Pisces)