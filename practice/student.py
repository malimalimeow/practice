import os

def add_student():
    while True:
        try:
            number = int(input("How many students would be added?"))
        
        except ValueError:
            print("please input a number")
            continue
        
        if number<=0 :
            print("please input a positive number")
            continue
        
        break
    
    students_data=[]
    for i in range(0,number):
        while True:
            name = input("student's name:")
            
            if any(char.isdigit() for char in name):
                print("please input a name")
                continue
            
            break
        
        while True:
            try:
                score = int(input("student's score:"))
            except ValueError:
                print("please input a score")
                continue
            
            if score<0 or score>100:
                print("please input a valid score")
                continue
            
            break
        
        student={"name":name, "score":score}
        students_data.append(student)
        
    print(f"{number} students added.",students_data)
    return students_data

def stats(students):
    
    highest_score=max(students,key=lambda x:x["score"])
    highest=f"{highest_score['name']}({highest_score['score']})"
    
    lowest_score=min(students,key=lambda x:x["score"])
    lowest=f"{lowest_score['name']}({lowest_score['score']})"
    
    avg=round((sum(s["score"]for s in students)/len(students)),2)
    
    return highest,lowest,avg
    
def order(students):
    
    while True:
        try:
            method=int(input("please input the number to choose the results order.\n 1:Ascending Order of scores\n 2:Descending Order of scores\n 3:Name order alphabetically\n"))
            
        except ValueError:
            print("please input the number only")
            continue
            
        if method not in [1,2,3]:
            print("please input the valid number only")
            continue
        
        break
    
    if method== 1:
        students.sort(key=lambda x:x["score"])
    
    elif method==2:
        students.sort(key=lambda x:x["score"],reverse=True)
    
    elif method==3:
        students.sort(key=lambda x:x["name"])
    
    return students

def search(students):
    while True:
            name=input("Name:").lower()
            if any(char.isdigit() for char in name):
                print("please input a valid name.")
                continue
            
            break
        
    for n in students:
        if name==n["name"]:
            return f"{name}'s score is {n['score']}"
    
   
    return "sorry, no record."

def write_in(students, classname):
    
    with open (f"{classname}.txt","w")as file:
        for n in students: 
            name=n["name"]
            score=str(n["score"])   
            file.write(f"{name},{score}\n")  
              
    highest,lowest,avg=stats(students)
    with open (f"{classname}.txt","a")as file:
        file.write(f"average score:{avg}")
4
def read_in(classname):
    if not os.path.exists(f"{classname}.txt"):
        with open(f"{classname}.txt","w")as file:
            pass
        return ""
    
    students=[]
    with open(f"{classname}.txt","r")as file:
        for row in file:
            row=row.strip()
            
            if "," not in row:
                break
            
            else:
                name,score=row.split(",")
                students.append({"name":name,"score":int(score)})
    
    return students
                
def menu(classname):
    students=read_in(classname)
    
    while True:
        try:
            choice=int((input("What do you want to do today?\n(please input number)\n1. Show statistics\n2. Sort students\n3. Search student\n4. Add and Save to file\n5. Exit\n")))
        
        except ValueError:
            print("please input valid number")
            continue   
         
        if not choice in [1,2,3,4,5]:
            print("please input valid number")
            continue  
        
        if choice==5:
            print("Good Bye")
            break
        
        
        if choice==1:
            highest,lowest,avg=stats(students)
            print(f"Top:{highest}\nLast:{lowest}\nAverage score:{avg}\n")
            
        
        elif choice==2:    
            students=order(students)
            write_in(students, classname)
            print(f"{classname}.txt is ordered and saved.\n")
            
        elif choice==3:
            print(search(students),"\n")
            
        elif choice==4:
            students.extend(add_student())
            write_in(students, classname) 
            print(f"{classname}.txt is saved.\n")
            


        
            
    
    
        
        
        
        

