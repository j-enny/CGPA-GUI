from tkinter import *

# simple result display

# Beginning of the tkinter main window
nextWin = Tk()
nextWin.title("Result Sheet")
nextWin.geometry("640x700")

scroll = Scrollbar(nextWin)
scroll.pack(side='right',fill=Y)

SchInfolabel = Label(nextWin, text="Student Result Sheet", font=("Times New Roman", 22, "bold"),bg="darkgray",fg="white").pack(fill="both")
sessionLabel = Label(nextWin, text="2017/2018", font=('Times New Roman', 12, 'bold'), bg="dark gray", fg="white").pack(fill="both")

#defining the first label frame
Student_Info = LabelFrame(nextWin, text="Student Data")
Student_Info.pack(fill="both", expand="yes")


#defining the SECOND label frame
course_Info = LabelFrame(nextWin, text="Courses")
course_Info.pack(fill="both", expand="yes")



# defining text variables
names = StringVar()
matricnum = StringVar()
depart = StringVar()
levels = StringVar()
myCourses = IntVar()
coursecodes = []
courseunits = []
scores = []



# creating labels
name = Label(Student_Info, text='Name').place(x=10, y=10)
matric = Label(Student_Info, text='Matric num').place(x=10, y=40)
dept = Label(Student_Info, text='Programme').place(x=10, y=70)
level = Label(Student_Info, text='Level').place(x=10, y=100)
coursecode = Label(course_Info, text='Course Code').place(x=10, y=10)
courseUnit = Label(course_Info, text="Course Unit").place(x=100, y=10)
Score = Label(course_Info, text="Score").place(x=230, y=10)



# creating entry fields
name_entry = Entry(Student_Info, textvariable=names, width=70)
name_entry.place(x=100, y=10)
matric_entry = Entry(Student_Info, textvariable=matricnum, width=70)
matric_entry.place(x=100, y=40)
dept_entry = Entry(Student_Info, textvariable=depart, width=70)
dept_entry.place(x=100, y=70)
level_entry = Entry(Student_Info, textvariable=levels, width=70)
level_entry.place(x=100, y=100)
numCourse = Label(Student_Info, text="Total number of courses")
numCourse.place(x=200, y=130)
entry1 = Entry(Student_Info, textvariable=myCourses, width=5)
entry1.place(x=350, y=160)

n = 0

# Function to create fields for student courses
def addentry():
    global n
    n = myCourses.get()
    if n == 0:
        tkMessageBox.showerror('Invalid Entry','Number of Courses can not be 0', default = RETRY, parent='course_Info')
    else:
        z = 10
        p = 40
        for i in range(int(n)):
            cc=StringVar()
            coursecodes.append(cc)
            newEntry = Entry(course_Info, textvariable=cc, width=8)
            newEntry.place(x=z, y=p)
            z += 120
            cu = IntVar()
            courseunits.append(cu)
            nextEntry = Entry(course_Info, textvariable=cu, width=6)
            nextEntry.place(x=z, y=p)
            z += 120
            sc = IntVar()
            scores.append(sc)
            scoreEntry = Entry(course_Info, textvariable=sc, width=6)
            scoreEntry.place(x=z, y=p)
            z -= 240 
            p += 30

        button2 = Button(course_Info,text="Compute Result", command=displayResult)
        button2.place(x=z, y=p)


addbutton = Button(Student_Info, text="Add Courses", command=addentry).place(x=450, y=160)



# This function fetches all information given on the previous window and displays them on the new window
def displayResult():
    
    # creating a new window on the existing window
    Gpa = Toplevel(nextWin)
    Gpa.title("Gpacalc")
    Gpa.geometry("640x640+0+0")
    prev = Label(Gpa, text="Student Result Sheet", font=('Times New Roman', 22, 'bold'), bg="dark gray", fg="white").pack(fill="both")
    prev2 = Label(Gpa, text="2017/2018", font=('Times New Roman', 12, 'bold'), bg="dark gray", fg="white").pack(fill="both")

    #defining the THIRD label frame
    Student_Auto = LabelFrame(Gpa, text="Student Data")
    Student_Auto.pack(fill="both", expand="yes")

    #defining the FOURTH label frame
    CGPA = LabelFrame(Gpa, text="Cummulative")
    CGPA.pack(side=LEFT, fill="both", expand="yes")
    
    Name = names.get()
    Matric = matricnum.get()
    Level = levels.get()
    Programme = depart.get()

    # LABELS THAT WILL APPEAR ON THE NEW WINDOW IN THE FIRST LABEL FRAME
    label1 = Label(Student_Auto, text="NAME:").place(x=10, y=10)
    name_label = Label(Student_Auto, text=Name).place(x=60, y=10)
    label2 = Label(Student_Auto, text="MATRIC NUM:").place(x=10, y=40)
    matric_label = Label(Student_Auto, text=Matric).place(x=100, y=40)
    label3 = Label(Student_Auto, text="PROGRAMME:").place(x=10, y=70)
    course_label = Label(Student_Auto, text=Programme).place(x=100, y=70)
    label4 = Label(Student_Auto, text="LEVEL:").place(x=10, y=100)
    level_label = Label(Student_Auto, text=Level).place(x=60, y=100)
    label5 = Label(Student_Auto, text="COURSE CODE").place(x=10, y=150)
    label6 = Label(Student_Auto, text="COURSE UNIT").place(x=90, y=150)
    label7 = Label(Student_Auto, text="SCORE").place(x=180, y=150)
    label8 = Label(Student_Auto, text="GRADE").place(x=260, y=150)
    label9 = Label(Student_Auto, text="GRADE POINT").place(x=340, y=150)
    label10 = Label(Student_Auto, text="CREDIT POINT").place(x=420, y=150)

    # BEGINNING OF RESULT CALCULATION

    #function to get the credit points and the course units required to calculate the average GP
    
    def Average(P,Q): 
        totalUnit=0
        totalCreditPoint=0
        totalUnit += P
        totalCreditPoint += Q
        AverageGp = Q/P
        return AverageGp


    #DICTIONARY HOLDING GRADE EQUIVALENTS
    c_point ={'F':0, 'E':1, 'D':2, 'C':3, 'B':4, 'A':5}

    # function to allocate letter grade
    def letter_grade():
        credit_p = {0 - 39: 'F', 40 - 44: 'E', 45 - 49: 'D', 50 - 59: 'C', 60 - 69: 'B', 70 - 100: 'A'}
        for i in range(int(n)):
            if 70 <= get_score < 101:
                scoreRange = 70 - 100
                cp = credit_p[scoreRange]
            elif 60 <= get_score < 70:
                scoreRange = 60 - 69
                cp = credit_p[scoreRange]
            elif 50 <= get_score < 60:
                scoreRange = 50 - 59
                cp = credit_p[scoreRange]
            elif 45 <= get_score < 50:
                scoreRange = 45 - 49
                cp = credit_p[scoreRange]
            elif 40 <= get_score < 45:
                scoreRange = 40 - 44
                cp = credit_p[scoreRange]
            else:
                scoreRange = 0 - 39
                cp = credit_p[scoreRange]

            return cp
    d = 20
    m = 200
    for i in range(int(n)):
        get_course = coursecodes[i].get()
        get_unit = courseunits[i].get()
        get_score = scores[i].get()
        credit=letter_grade()
        grade_point= c_point[credit]
        credit_point = grade_point*get_unit
        coursecodelabel = Label(Student_Auto, text=get_course).place(x=d, y=m)
        d += 90
        courseunitlabel = Label(Student_Auto, text=get_unit).place(x=d, y=m)
        d += 90
        score = Label(Student_Auto, text=get_score).place(x=d, y=m)
        d += 90
        grade = Label(Student_Auto, text=credit).place(x=d, y=m)
        d += 90
        gradepointlabel = Label(Student_Auto, text=grade_point).place(x=d, y=m)
        d += 90
        creditpointlabel = Label(Student_Auto, text=credit_point).place(x=d, y=m)
        d -= 450
        m += 30

        # sum up all units and credit points
        currentGp = Average(get_unit,credit_point)
   

    #To display the AVERAGE GP
    label20 = Label(CGPA, text = 'Current').place(x=10, y=20 )
    label21 = Label(CGPA, text= currentGp).place(x=100, y=20)

    close_window2 = Button(Gpa, text="Back", command=Gpa.destroy, bg="dark gray", fg="white").pack(fill="both", side=BOTTOM)

close_window = Button(nextWin, text='Close App', command=nextWin.quit, bg="dark gray", fg="white").pack(fill="both", side=BOTTOM)

nextWin.mainloop()
