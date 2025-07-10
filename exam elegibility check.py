medical_cause= input("Did you have a medical cause? Y or N: ")
attendance= int(input("Enter your attendance percentage: "))

if medical_cause == "Y":
    print("You are eligible to participate in the exam!")
else:
    if attendance>=75:
        print("You are eligible to participate in the exam! ")
    else:
        print("You are not eligible to participate in the exam!")
