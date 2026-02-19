class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.courses=[]
        self.marks={}
    
    def add_course(self,course):
        self.courses.append(course)
    
    def add_score(self,course,score):
        self.marks[course]=score
    
    def average(self):
        if not self.marks:
            return 0
        
        return sum(self.marks.values())/len(self.marks)
    
class School:
    def __init__(self):
        self.students=[]
        
    def add_student(self,student):
        self.students.append(student)
    
    def add_score_to_student(self,student_id,course,score):
        for student in self.students:
            if student.student_id==student_id:
                student.add_score(course,score)
    
    def average_for_class(self):
        if not self.students:
            return 0
        
        total=0
        for student in self.students:
            total+=student.average()
            return total/len(self.students)


        
    

        
        
     
           

        
                
    
        
        
    