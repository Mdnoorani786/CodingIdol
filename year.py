#python 3.7.1
year=int(input("enter year :"))
 
if (year%400==0) and (year%100==0):
   print(year, "is a leap year")
elif (year%4==0)   and (year%100!=0):
  print(year, " is a leap year")
else:
  print(year, "sorry this is not a leap year")