# calculator
num1=int(input("enter first number"))
num2=int(input("enter second number "))
opr=input(" enter operator..")
if opr=="+":
  print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
  print("invalid number")