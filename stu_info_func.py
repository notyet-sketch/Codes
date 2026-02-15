try:
    students={}

    def add():
        id=input("Enter student id:")
        if id in students:
            print("Student exists.")
        else:
            name=input("Enter name:")
            age=input("Enter age:")
            if not age.isdigit():
                print("Invalid choice.")
                return
            age=int(age)
            sub=input("How many subjects? (Max 10) ")
            if not sub.isdigit():
                print("Invalid choice.")
                return
            sub=int(sub)
            if sub>10 or sub<1:
                print("Invalid subject count.")
                return
            marks=[]
            print(f"Enter marks(1-100) of {sub} sub:")
            for i in range(sub):
                mark=input()
                if not mark.isdigit():
                    print("numbers only.")
                    return
                mark=int(mark)
                if mark>100 or mark<1:
                    print("Invalid choice.")
                    return
                marks.append(mark)
            average=sum(marks)/len(marks)
            grade=calculate_grade(average)
            students[id]={
            "Name":name,
            "Age":age,
            "Marks":marks,
            "Average":average,
            "Grade":grade
        }
            print("Student added successfully.\n")



    def view():
        if not students:
            print("\nNo students found.\n")
        else:
            for key,value in students.items():
                print(f"\nID:{key}")
                for stu,info in value.items():
                    print(f"{stu}: {info}")
                print()


    def search():
        id=input("Enter id:")
        if id not in students:
            print("No students found.")
        else:
            for stu,info in students[id].items():
                    print(f"{stu}: {info}")

    def remove():
        id=input("Enter id:")
        if id not in students:
            print("No students found.")
        else:
            removed=students.pop(id)
            print(f"{id} was removed.\n")

    def update():
        id=input("Enter id:")
        if id not in students:
            print("No students found.")
        else:
            age=input("Enter age:")
            if not age.isdigit():
                print("Invalid choice.")
                return
            age=int(age)
            students[id]["Age"]=age
            print("Age updated.\n")

    def check_even_odd(num):
        return "EVEN" if num%2==0 else "ODD"
    
    def calculate_grade(average):
        if average>=80:
            return "A+"
        elif average>=70:
            return "A"
        elif average>=60:
            return "B"
        elif average>=50:
            return "C"
        else:
            return "F"


    def largest(num):
        return max(num)
    def change_mark():
        id=input("Enter id:")
        if id not in students:
            print("No students found.")
        else:
            sub=input("How many subjects? (Max 10) ")
            if not sub.isdigit():
                print("Invalid choice.")
                return
            sub=int(sub)
            if sub>10 or sub<1:
                print("Invalid subject count.")
                return
            marks=[]
            print(f"Enter marks(1-100) of {sub} sub:")
            for i in range(sub):
                mark=input()
                if not mark.isdigit():
                    print("Numbers only.")
                    return
                mark=int(mark)
                if mark<1 or mark>100:
                    print("Invalid choice.")
                    return
                marks.append(mark)
            average=sum(marks)/len(marks)
            grade=calculate_grade(average)


            students[id]["Marks"]=marks
            students[id]["Grade"]=grade
            students[id]["Average"]=average


    while True:
        choice=input("1.Add Student\n2.View all students\n3.Search student by ID\n4.Remove a student\n5.Update student age\n6.Even_Odd\n7.Max num\n8.Update marks\n9.Quit program\n>>>")
        if not choice.isdigit():
            print("Invalid choice.")
            continue
        choice=int(choice)
        if choice==1:
            add()
        elif choice==2:
            view()
        elif choice==3:
            search()
        elif choice==4:
            remove()
        elif choice==5:
            update()
        elif choice==6:
            num=input("Enter num:")
            if not num.isdigit():
                print("Invalid choice.")
                continue
            num=int(num)
            print(check_even_odd(num))

        elif choice==7:
            print("Enter 3 numbers: ")
            num=[]
            for _ in range(3):
                number=input()
                if not number.isdigit():
                    print("Invalid choice.")
                    continue
                number=int(number)
                num.append(number)
            print(f"Largest num: {largest(num)}")
        elif choice==8:
            change_mark()

        elif choice==9:
            print("Quitting...")
            break

except Exception as e:
    print(f"Something else wrong: {e}")
    