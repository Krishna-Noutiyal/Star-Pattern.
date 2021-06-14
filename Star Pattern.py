# row=int(input("Enter the rows: "))
# boolen=bool(int(input("Enter 1 or 0: ")))
# print(boolen)
# if boolen==True:
#     for x in range(1,row+1):
#         print("*"*x)
#         x -= 1
# elif boolen==False:
#     for x in range(1,row+1):
#         print("*"*row)
#         row -= 1


a = ["Krishna", 1, 3, "Gauri"]
# The value of i will change evertime like it wil first become krishna and the 1 and so on 
# for i in a:
#     print(i, end=" ")


""" Star Pattern """

# n = int(input("Enter the no of rows you want:"))
#This means for every digit in range form 1 to the number entered by user [n+1 is because the number enterd by user is absoulte means 1 smaller then the number python counts(python counts form 0) ]
# for digits in range(1,n+1):
#     print("*"*digits)  



"""
Now lets understand how the above code worked 
1- user entered the number of rows he want
2- ran a for loop with variable digits for a specific times by using range function
   ran it form 1 to the n number of times +1 because the code will stop, print("Hello "*0) This does not print anyting because it is multiplied by 0 times
3- abhi bhi samaj nahi aaya to dekho jese n = 5 aur for loop run hoga 1 se lekar ke 5 tak 
   itna samaj aaya, ab age chalo python count karta he 0 se that mean for loop me value kuch esi hog 1,2,3,4,5
       0,1,2,3,4
    hena to abe hame star print karna he uske liye usko digits se multiply kiy ab agar star ko 0
    se multiply karoge to kuch print nahi hoga ab bache 1,2,3,4 pythoncounting ke hisab se 
    to issi liye agar +1 nahi lagaoge to 1 row kam print hogi 
4- printing the star by multiplying it digits times  
"""
"""
For Star pattern like:
*
**
***
****
*****
"""
# n = int(input("Enter the number of rows: "))

# for row in range(1, n+1):
#       for column in range(1, row+1):
#          print("*", end=" ")
#       print()

"""
For Star pattern like:
*****
****
***
**
*
"""
# n = int(input("Enter the number of rows: "))

# for row in range(n+1, 1, -1 ):
#       for column in range(1, row):
#          print("*", end=" ")
#       print()


"""
Actual exercise 
"""
print("Pattern 0:- \n\n*****\n****\n***\n**\n**")
print("Pattern 1:- \n\n*\n**\n***\n****\n*****")
while (True):
   try:
      n = int(input("Enter the number of rows: "))
      t = bool(int(input("What type of pattern you want type 0 or 1: ")))
      print(t)
      if t == True:
         print("True")
         for rows in range(1, n+1):
            for columns in range(0,rows):
               print("*", end=" ")
            print()

         again = input("\n\tPress 1 to continue or enter to exit:")
         if again == "1":
            continue
         else:
            print("\n\t\t Thanks for using pattern printing\n")
            break

      elif t == False:
         print("False")
         for rows in range(n,0,-1):
            for columns in range(0, rows):
               print("*", end=" ")
            print("\r")
         #Asking user to continue or end
         again = input("\n\tPress 1 to continue or enter to exit:")
         if again == "1":
            continue
         else:
            print("\n\t\t Thanks for using pattern printing\n")
            break
   except :
      print("\n\tOoups!! Looks like u enter someting wrong")
      
      again = input("\n\tPress 1 to continue or enter to exit:")

      if again == "1":
         continue
      else:
         print("\n\t\t Thanks for using pattern printing\n")
         break



