from tkinter import *

# simple result display

n = 0

# To create fields for student courses
def addentry():
    global n
    n = myCourses.get()

    z = 10
    p = 280
    for i in range(int(n)):
        cc=StringVar()
        coursecodes.append(cc)
        newEntry = Entry(nextWin, textvariable=cc, width=8)
        newEntry.place(x=z, y=p)
        z += 120
        cu = IntVar()
        courseunits.append(cu)
        nextEntry = Entry(nextWin, textvariable=cu, width=6)
        nextEntry.place(x=z, y=p)
        z += 120
        sc = IntVar()
        scores.append(sc)
        scoreEntry = Entry(nextWin, textvariable=sc, width=6)
        scoreEntry.place(x=z, y=p)
        z -= 240
        p += 30

    button2 = Button(text="Compute Result", command=displayResult)
    button2.place(x=z, y=p)

# Beginning of the tkinter main window
nextWin = Tk()
nextWin.title("Result Sheet")
nextWin.geometry("640x640")

SchInfolabel = Label(nextWin, text="Student Result Sheet", font=("arial", 20, "bold")).pack()
sessionLabel = Label(nextWin, text="2017/2018", font=('arial', 10, 'bold')).pack()

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
name = Label(nextWin, text='Name').place(x=10, y=100)
matric = Label(nextWin, text='Matric num').place(x=10, y=130)
dept = Label(nextWin, text='Programme').place(x=10, y=160)
level = Label(nextWin, text='Level').place(x=10, y=190)
coursecode = Label(nextWin, text='Course Code').place(x=10, y=250)
courseUnit = Label(nextWin, text="Course Unit").place(x=100, y=250)
Score = Label(nextWin, text="Score").place(x=230, y=250)


# creating entry fields
name_entry = Entry(nextWin, textvariable=names, width=70).place(x=100, y=100)
matric_entry = Entry(nextWin, textvariable=matricnum, width=70).place(x=100, y=130)
dept_entry = Entry(nextWin, textvariable=depart, width=70).place(x=100, y=160)
level_entry = Entry(nextWin, textvariable=levels, width=70).place(x=100, y=190)
numCourse = Label(nextWin, text="Total number of courses").place(x=200, y=220)
entry1 = Entry(nextWin, textvariable=myCourses, width=5)
entry1.place(x=350, y=220)

addbutton = Button(nextWin, text="Add Courses", command=addentry).place(x=450, y=220)


# This function fetches all information given on the previous window and displays them on the new window
def displayResult():
    # creating a new window on the existing window
    Gpa = Toplevel(nextWin)
    Gpa.title("Gpacalc")
    Gpa.geometry("640x640+120+120")
    prev = Label(Gpa, text="Student Result Sheet", font=("arial", 20, "bold")).pack()
    prev2 = Label(Gpa, text="2017/2018", font=('arial', 10, 'bold')).pack()
    Name = names.get()
    Matric = matricnum.get()
    Level = levels.get()
    Programme = depart.get()

    # LABELS THAT WILL APPEAR ON THE NEW WINDOW
    label1 = Label(Gpa, text="NAME:").place(x=10, y=100)
    namelabel = Label(Gpa, text=Name).place(x=60, y=100)
    label2 = Label(Gpa, text="MATRIC NUM:").place(x=10, y=130)
    matriclabel = Label(Gpa, text=Matric).place(x=60, y=130)
    label3 = Label(Gpa, text="PROGRAMME:").place(x=10, y=160)
    courselabel = Label(Gpa, text=Programme).place(x=100, y=160)
    label4 = Label(Gpa, text="LEVEL:").place(x=10, y=190)
    levellabel = Label(Gpa, text=Level).place(x=60, y=190)
    label5 = Label(Gpa, text="COURSE CODE").place(x=10, y=240)
    label6 = Label(Gpa, text="COURSE UNIT").place(x=90, y=240)
    label7 = Label(Gpa, text="SCORE").place(x=180, y=240)
    label8 = Label(Gpa, text="GRADE").place(x=260, y=240)
    label9 = Label(Gpa, text="GRADE POINT").place(x=340, y=240)
    label10 = Label(Gpa, text="CREDIT POINT").place(x=420, y=240)

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
                scoreRange = 0 - 40
                cp = credit_p[scoreRange]

            return cp

    c_point ={'F':0, 'E':1, 'D':2, 'C':3, 'B':4, 'A':5}
    d = 20
    m = 290
    for i in range(int(n)):
        get_course = coursecodes[i].get()
        get_unit = courseunits[i].get()
        get_score = scores[i].get()
        credit=letter_grade()
        grade_point= c_point[credit]
        credit_point = grade_point*get_unit
        coursecodelabel = Label(Gpa, text=get_course).place(x=d, y=m)
        d += 90
        courseunitlabel = Label(Gpa, text=get_unit).place(x=d, y=m)
        d += 90
        score = Label(Gpa, text=get_score).place(x=d, y=m)
        d += 90
        grade = Label(Gpa, text=credit).place(x=d, y=m)
        d += 90
        gradepointlabel = Label(Gpa, text=grade_point).place(x=d, y=m)
        d += 90
        creditpointlabel = Label(Gpa, text=credit_point).place(x=d, y=m)
        d -= 450
        m += 30




    closewin2 = Button(Gpa, text="Back", command=Gpa.destroy).pack(side=BOTTOM)


closewin1 = Button(nextWin, text='Close App', command=nextWin.destroy).pack(side=BOTTOM)

nextWin.mainloop()
