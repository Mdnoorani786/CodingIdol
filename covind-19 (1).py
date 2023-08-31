print("covind-19 - 2019 Based Data.")
import pandas as pd
dic={
'january':["amber","davide","suriya","anit","pankaj"],
"Gender":["female","male","female","male","male"],
"effect":["infacted","uninfacted","death","infacted","death"],
"February":["akhlad","sonu","naaz","katrina","salman"],
"GENDER":["female","male","female","female","male"],
"EFFECT":["unifacted","uninfacted","death","uninfacted","death"],

}
m={
"March":["naziya","ajhar","Ajit kumar","katrina","sallu"],
"GENDER":["female","male","male","female","male"],
"EFFECT":["unifacted","uninfacted","death","uninfacted","death"],
"April":["sofiya","akhtar","Ankitkumar","katrina","soni"],
"GENDER":["female","male","male","female","female"],
"effect":["infacted","infacted","death","uninfacted","uninfacted"],


}
c={"may":["naziya","ajhar","Ajit kumar","katrina","sallu"],
"GENDER":["female","male","male","female","male"],
"EFFECT":["unifacted","uninfacted","death","uninfacted","death"],
"June":["sofiya","akhtar","Ankitkumar","katrina","soni"],
"GENDER":["female","male","male","female","female"],
"effect":["infacted","infacted","death","uninfacted","uninfacted"]
}
x={ "july":["naziya","ajhar","Ajit kumar","katrina","sallu"],
"GENDER":["female","male","male","female","male"],
"EFFECT":["unifacted","uninfacted","death","uninfacted","death"],
"august":["fiya","aqbal","Ankitkumar","athar","samni"],
"GENDER":["female","male","male","female","female"],
"effect":["death","infacted","death","uninfacted","uninfacted"],
}
w={"September":["nazia","amhar","Ajay", "kumar","ritika",],
"GENDER":["female","male","male","female","female"],
"EFFECT":["infacted","infacted","death","infacted","death"],
   "October":["fiya","aqbal","Ankitkumar","athar","samni"],
"GENDER":["female","male","male","female","female"],
"effect":["death","infacted","death","uninfacted","uninfacted"],
   
}
q={"November":["nazia","amhar","Ajay", "kumar","ritika",],
"GENDER":["female","male","male","female","female"],
"EFFECT":["unifacted","uninfacted","death","uninfacted","death"],
"December":["fiya","aqbal","Ankitkumar","athar","samni"],
"GENDER":["female","male","male","female","female"],
"effect":["death","infacted","death","uninfacted","uninfacted"],
}

print()
print("JANUARY TO FEBRUARY....:")
s=pd.DataFrame(dic)
print(s)

print(" ")
print("MARCH TO APRIL..:")
print()

n=pd.DataFrame(m)
print(n)
print()
print("MAY TO JUN..:")
print()
A1=pd.DataFrame(c)
print(A1)
print()
print("JULY TO AUGUST...:")
g=pd.DataFrame(x)
print(g)
print()
print("SEPTEMBER TO OCTOBER...:")
g1=pd.DataFrame(w)
print(g1)
print()
print()
print("NOVEMBER TO DECEMBER....:")
g2=pd.DataFrame(q)
print(g2)
print()
def myfun(dic,m,c,x,w,q):
    print("Covind-19 People List...:")
    print("january",dic["january"])
    print("February",dic["February"])
    print("March",m["March"])
    print("April",m["April"])
    print("may",c["may"])
    print("june",c["June"])
    print ("july",x["july"])
    print ("august",x["august"])
    print ("September",w["September"])
    print ("October",w["October"])
    print ("November",q["November"])
    print ("December",q["December"])
    print()
    print("Total people.:",12*5)
 
   
myfun(dic,m,c,x,w,q)
print("january =ambar  and abrar uninfected..:2")
print("january = David infected..:. 1")
print("january= Surya and pankaj are Death..2")
print("February = Akhlad ,sonu and katrina  are uninfacted..3.")
print("February = Salman and naaz are Death..3:")
print("March= nazia uninfected..1")
print("March= Shahil ,ajhar and Ajit are infected ..:3")
print("March= Saifan Death..1")
print("April = Aqbal and Sonu unifected..2")
print("April=Sunali ,aqbal and Javed are infected.:3")
print("may=najya,rashid and kumar are uninfacted..3.")
print("may=sabana and sabina are infected..2.")
print("June=sofiya,saif, and saba are uninfected..3.")
print("June=krity and kunal are deatt..2.")
print("july=jubair, jainab are uninfected..2")
print("july=jinat,sahil,alishan are death..3")
print("august=deva, seth,ivan,jorge are uninfected..4")
print("august= robert is infected..1")
print("September=janet,lewis are uninfected..2")
print("Septrmber=pappu, bhola,bhopal are death..3")
print("Octuber=smith,jones,sabiya,sana,rushan,uninfected..5")
print("November=hall is uninfected..1")
print("November=evans ,thomsen, jeckson,wood are infected..4")
print("December=arsalan,sadaf, affan,amit are uninfeceted..4")
print("December=afjal is deth..1")
print("Total Uninfeceted People=31")
print("Total Infeceted People = 14")
print("Total Death People = 15")
print("Total People =60")
print()
print("\n")
print()
print("=====================>CHECK VIROUS<========================")
print("\n")
print("if   you  want to check  you are infected or not.. please  give input..:")
print()
print("\n")
name = input("Enter your name: ")
Age=int(input("Enter your age..:"))
city = input("Enter your city: ")


F = input("Do you have fever? (yes/no): ").lower()
print()
g = input("Do you have cough? (yes/no): ").lower()
print()
print("\n")
f= input("Are you losing weight? (yes/no): ").lower()
print()
print("\n")

if F== "yes" or g == "yes":
    print()
    print("\n")
 
    print("You are infected.")
    print()
    print(" you have to go for quarantine.😱")
    print()
    print("you have to go to the hospital.")
    print()
elif f=="no" or g=="no":
   print()
   print()
   print("You are uninfected.")
   print()
   print("But you have to be careful.")
   print()
   print("Someone whose age is above 50 they have to be very careful  ")
   print()
 