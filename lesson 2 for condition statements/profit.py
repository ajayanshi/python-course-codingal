actual=int(input("enter the actual amount"))
selling=int(input("enter the selling amount"))
if selling > actual :
    print("you have got a profit of", selling-actual)
else:
    print("you have got a loss of", actual-selling)
