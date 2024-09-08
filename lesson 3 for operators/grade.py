print("Enter the marks of five subjects")
m1=int(input("Enter the marks of first subject"))
m2=int(input("Enter the marks of second subject"))
m3=int(input("Enter the marks of third subject"))
m4=int(input("Enter the marks of fourth subject"))
m5=int(input("Enter the marks of fifth subject"))
sum=m1+m2+m3+m4+m5
average=sum/5
if(average >  80):
    print("You are an A+ grade")
elif(average >60):
    print("You are an B+ grade ")
else: 
    print(" You are an C grade ")
