Stu={'Luffy':77,'Zoro':99,'Sanji':69,'Brook':81,'Nami':64,'Usoop':55,'Robin':88,'Jinbe':85}

Name=input("Enter the student's name: ")
result=Name in Stu
if result==True:
    print(Name+"'s marks:",Stu[Name])
else:
    print("Student not found")

