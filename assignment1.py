name=input("Enter your full name: ")
email=input("Enter your email address: ")
mobile_number=input("Enter your mobile number: ")
age=int(input("Enter your age: "))
if name[0]!=" " and name[-1]!=" " and name.count(" ")>=1:
    if ('a' <= email[0] <= 'z') or ('A' <= email[0] <= 'Z') or ('0' <= email[0] <= '9') and email.count("@")==1 and email.count(".")>=1  and email.count(" ")==0:

    #if (('a' <= email[0] <= 'z') or ('A' <= email[0] <= 'Z') or ('0' <= email[0] <= '9')) \
   #and email.count("@") == 1 \
   #and email.count(".") >= 1 \
   #and email.count(" ") == 0:
        if len(mobile_number) == 10 and mobile_number.isdigit():
              if age>=18 and age<=60:
                   print("User Profile is VALID")
              else:
                   print("User Profile is INVALID")
        else:
          print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
       print("User Profile is INVALID")