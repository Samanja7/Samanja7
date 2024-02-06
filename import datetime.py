import datetime

day=int(input("Enter the day(DD) : "))
month=int(input("Enter the Month(MM) : "))
yr=int(input("Enter the Year(YYYY) : "))


Aquarius="""
Aquarius energy does. This member of the zodiac embodies rebellion, creativity, eccentricity, and intelligence. They're driven by a desire to evolve past antiquated ideals, and help society move into a more compassionate space. They can be seen as unpredictable or disorganized, but often surprise people with their streaks of brilliance and hidden genius.
"""
Pisces="""
Pisces signs have a peaceful and gentle presence about them, with an uncanny ability to tap into the emotions of the collective. They're extremely malleable and need to be careful of who they surround themselves with. Since they are hyper-intuitive, they can sometimes become disconnected–making it important for this water sign to ground often.
"""
Aries="""
Aries are typically brave and outgoing. They're assertive by nature and won't hesitate to tell you how they feel. But they do need to be mindful that they don't hurt anyone's feelings by speaking impulsively. They can be headstrong at times, and make better leaders than followers.
"""
Taurus="""
No one will expose you to the finer things in life quite like a Taurus. This fixed earth sign has impeccable taste and loves to indulge. They tend to be financially responsible, but still know how to treat themselves and the ones they love. Though they do have a stubborn streak, this member of the zodiac is incredibly loyal and reliable.
"""
Gemini="""
Geminis make great students and communicators. They're witty and charming, but also have a darker side to them. They love to socialize but can become nervous or overstimulated when they don't take time for themselves. This sign is also great at multitasking but needs to be careful not to take on too much at once.
"""
Cancer="""
Cancers feel deeply, though will often keep these sentiments hidden under their shell. They are intuitively nurturing and love to take care of the people around them. They have a reputation for being moody and aren't always the best at unpacking their feelings with others. They often opt to sort out their issues alone.
"""
Leo="""
Leos make great friends and companions. They are confident and larger-than life, easily charming the people they encounter. However, this sign can be dramatic from time to time, especially if they feel disrespected. They feel passionately about their personal interests but need to be mindful that they show interest in the lives of those around them as well.
"""
Virgo="""
Virgos are organized, driven, and meticulous in their work. They are very detail-oriented, making them master editors with extremely high standards. However, they need to be mindful that they are not overly demanding or critical of themselves or those around them.
"""
Libra="""
Libra is one of the most laid-back members of the zodiac. They are extremely relationship-oriented but can sometimes prioritize their partner's needs over their own. This Venus ruled sign has a keen eye for aesthetics with impeccable personal style and well decorated homes
"""
Scorpio="""
Scorpios are hard to ignore. They are extremely intuitive and make natural psychologists with an ability to easily read those around them. They form intense bonds with their friends and romantic partners, but they can become possessive or jealous if they're not completely confident with themselves.
"""
Sagitarius="""
Sagittarius is one of the most beloved members of the zodiac–with an adventurous, charismatic, and generous spirit. They lean toward optimism and love to take risks, but need to be mindful of living in the present and making practical plans for the future. Sagittarius are natural philosophers and are always looking to explore the mysteries of the universe.
"""
Capricorn="""
Capricorns are known for their endurance and determination. Career-motivated and focused on status, these earth signs are highly driven to reach their professional goals and take their responsibilities very seriously. They're typically resistant to change and will often stick with their personal routines for many years.
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

if month>=3 and month<=4:
    if month==3 and day>=21:
        print(Aries)
    elif month==4 and day<=19:
        print(Aries)

if month>=4 and month<=5:
    if month==4 and day>=20:
        print(Taurus)
    elif month==3 and day<=20:
        print(Taurus)

if month>=5 and month<=6:
    if month==5 and day>=21:
        print(Gemini)
    elif month==6 and day<=20:
        print(Gemini)

if month>=6 and month<=7:
    if month==6 and day>=21:
        print(Cancer)
    elif month==7 and day<=22:
        print(Cancer)

if month>=7 and month<=8:
    if month==7 and day>=23:
        print(Leo)
    elif month==8 and day<=22:
        print(Leo)

if month>=8 and month<=9:
    if month==8 and day>=23:
        print(Virgo)
    elif month==9 and day<=22:
        print(Virgo)

if month>=9 and month<=10:
    if month==9 and day>=23:
        print(Libra)
    elif month==10 and day<=22:
        print(Libra)

if month>=10 and month<=11:
    if month==11 and day>=23:
        print(Scorpio)
    elif month==12 and day<=21:
        print(Scorpio)

if month>=11 and month<=12:
    if month==11 and day>=23:
        print(Sagitarius)
    elif month==12 and day<=21:
        print(Sagitarius)

if month>=11 and month<=1:
    if month==11 and day>=22:
        print(Capricorn)
    elif month==1 and day<=19:
        print(Capricorn)