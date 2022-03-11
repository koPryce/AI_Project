from tkinter import *
from pyswip import Prolog

# Prolog
prolog = Prolog()

prolog.consult("AI_Project.pl")


# Commands
def add_fact():
    # Inner Commands
    def ethnicity():
        conditionbtn.destroy()
        ethnicitybtn.destroy()
        ethnicitylbl.grid(row=0, column=0)
        ethnicitytb.grid(row=0, column=1)
        esubmitbtn = Button(condition_window, text="Submit", command=sendEToDatabase)
        esubmitbtn.grid(row=1, column=0)
        backbtn = Button(condition_window, text="Go Back", command=readd_fact)
        backbtn.grid(row=1, column=1)

    def sendCToDatabase():
        cond = conditiontb.get()
        if cond[0].isupper():
            prolog.assertz("underlying_condition('" + cond + "')")
        else:
            prolog.assertz("underlying_condition(" + cond + ")")

    def sendEToDatabase():
        eth = ethnicitytb.get()
        if eth[0].isupper():
            prolog.assertz("ethnicity('" + eth + "')")
        else:
            prolog.assertz("ethnicity(" + eth + ")")

    def condition():
        conditionbtn.destroy()
        ethnicitybtn.destroy()
        conditionlbl.grid(row=0, column=0)
        conditiontb.grid(row=0, column=1)
        csubmitbtn = Button(condition_window, text="Submit", command=sendCToDatabase)
        csubmitbtn.grid(row=1, column=0)
        backbtn = Button(condition_window, text="Go Back", command=readd_fact)
        backbtn.grid(row=1, column=1)

    def readd_fact():
        condition_window.destroy()
        add_fact()

    # Window
    condition_window = Toplevel()
    condition_window.title('Add Condition Fact')
    condition_window.iconbitmap('./favicon.ico')
    condition_window.configure(bg="#353535")
    condition_window.geometry("850x600")

    # Labels
    conditionlbl = Label(condition_window, text="Enter an underlying condition")
    ethnicitylbl = Label(condition_window, text="Enter a risky ethnicity")

    # Text Boxes
    conditiontb = Entry(condition_window, width=50)
    ethnicitytb = Entry(condition_window, width=50)
    # Buttons
    conditionbtn = Button(condition_window, text="Add an underlying condition", command=condition)
    ethnicitybtn = Button(condition_window, text="Add an at risk ethnicity", command=ethnicity)

    conditionbtn.grid(row=0, column=0)
    ethnicitybtn.grid(row=1, column=0)


def add_patient():
    global gender
    global ans
    global clicked

    # Inner Commands
    def add_patient_to_prolog():
        pname = name.get().capitalize()
        page = age.get()
        pheight1 = height1.get()
        pheight2 = height2.get()
        ptemp = str(float("{0:.2f}".format((int(temp.get()) * 1.8) + 32)))
        pethnicity = selected.get().capitalize()
        pgender = gender.get()
        pweight = weight.get()
        pdfb = ans.get()

        if pdfb == "yes":
            psys = systolic.get()
            pdia = diastolic.get()
            prolog.assertz("patientw('" + pname + "', " + page + "," + pheight1 + "," + pheight2 + "," + ptemp + ",'"
                           + pethnicity + "'," + pgender + "," + pweight + "," + pdfb + "," + psys + "," + pdia + ")")
            # c = list(prolog.query("get_patientw('" + pname + "',B,C,D,E,F,G,H,I,J,K)"))
            #
            # print(c)
        else:
            prolog.assertz("patientn('" + pname + "', " + page + "," + pheight1 + "," + pheight2 + "," + ptemp + ",'"
                           + pethnicity + "'," + pgender + "," + pweight + "," + pdfb + ")")
            # c = list(prolog.query("get_patientn('" + pname + "',B,C,D,E,F,G,H,I)"))
            #
            # print(c)

        conditions = []
        length = len(CONDITIONS)
        for con in range(length):
            if variables[con].get() == "On":
                conditions.append(str(CONDITIONS[con]).capitalize())

        for f in (conditions):
            prolog.assertz("punderlying('" + pname + "','" + f + "')")
            c = list(prolog.query("get_punderlying('" + pname + "',B)"))
            print(c)

    def display_pressure(frame, val):
        global systolic
        global diastolic
        global syslbl
        global dialbl

        if radio_buttons[val]['text'] == "Yes":
            syslbl = Label(frame, text="Systolic Pressure")
            dialbl = Label(frame, text="Diastolic Pressure")
            systolic = Entry(frame, width=30)
            diastolic = Entry(frame, width=30)
            syslbl.grid(row=9, column=0)
            dialbl.grid(row=10, column=0)
            systolic.grid(row=9, column=1, columnspan=2)
            diastolic.grid(row=10, column=1, columnspan=2)

        if radio_buttons[val]['text'] == "No":
            if syslbl.winfo_exists() and dialbl.winfo_exists() and systolic.winfo_exists() and diastolic.winfo_exists() == 1:
                syslbl.grid_forget()
                dialbl.destroy()
                systolic.destroy()
                diastolic.destroy()

    # Window
    patient_window = Toplevel()
    patient_window.title('Add Patient Fact')
    patient_window.iconbitmap('./favicon.ico')
    patient_window.configure(bg="#353535")
    patient_window.geometry("850x600")

    # Frame
    patient_frame = LabelFrame(patient_window, text="Condition Details", padx=40, pady=40, borderwidth=10,
                               bg="#fff")
    patient_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

    # Labels
    Label(patient_frame, text="Name").grid(row=0, column=0)
    Label(patient_frame, text="Age").grid(row=1, column=0)
    Label(patient_frame, text="Temperature (in Celsius)").grid(row=2, column=0)
    Label(patient_frame, text="Height (Ft)").grid(row=3, column=0)
    Label(patient_frame, text="Height (In)").grid(row=4, column=0)
    Label(patient_frame, text="Ethnicity").grid(row=5, column=0)
    Label(patient_frame, text="Gender").grid(row=6, column=0)
    Label(patient_frame, text="Experienced dizziness, fainting or blurry vision?").grid(row=7, column=0)
    Label(patient_frame, text="Weight").grid(row=8, column=0)
    Label(patient_frame, text="Underlying condition").grid(row=11, column=0)

    # Text Boxes
    name = Entry(patient_frame, width=30)
    age = Entry(patient_frame, width=30)
    temp = Entry(patient_frame, width=30)
    height1 = Entry(patient_frame, width=30)
    height2 = Entry(patient_frame, width=30)
    weight = Entry(patient_frame, width=30)

    name.grid(row=0, column=1, columnspan=2)
    age.grid(row=1, column=1, columnspan=2)
    temp.grid(row=2, column=1, columnspan=2)
    height1.grid(row=3, column=1, columnspan=2)
    height2.grid(row=4, column=1, columnspan=2)
    weight.grid(row=8, column=1, columnspan=2)

    # Dropdown Menu
    selected = StringVar()
    ETHNICITY = [e['X'] for e in list(prolog.query("ethnicity(X)"))]
    selected.set(ETHNICITY[0])
    ethnicities = OptionMenu(patient_frame, selected, *ETHNICITY)
    ethnicities.grid(row=5, column=1, columnspan=2)

    # Checkbox
    CONDITIONS = [c['X'] for c in list(prolog.query("underlying_condition(X)"))]
    names = []
    variables = []
    for x in range(len(CONDITIONS)):
        names.append("cb" + str(x))
        variables.append(StringVar(value="clicked"+str(x)))
    k = 0
    i = 11
    j = 1
    for c in range(len(CONDITIONS)):
        variables[k] = StringVar()
        names[k] = Checkbutton(patient_frame, text=CONDITIONS[k], variable=variables[k], onvalue="On", offvalue="Off")
        if j % 4 == 0:
            i += 1
            j = 1
        names[k].grid(row=i, column=j)
        names[k].deselect()
        k += 1
        j += 1

    # Radio Button
    gender = StringVar()
    gender.set("male")
    Radiobutton(patient_frame, text="Male", variable=gender, value="male").grid(row=6, column=1)
    Radiobutton(patient_frame, text="Female", variable=gender, value="female").grid(row=6, column=2)

    ans = StringVar()
    ans.set("no")
    ansbtn1 = Radiobutton(patient_frame, text="Yes", variable=ans, value="yes",
                          command=lambda: display_pressure(patient_frame, 0))
    ansbtn1.grid(row=7, column=1)
    ansbtn2 = Radiobutton(patient_frame, text="No", variable=ans, value="no",
                          command=lambda: display_pressure(patient_frame, 1))
    ansbtn2.grid(row=7, column=2)

    radio_buttons = [ansbtn1, ansbtn2]

    # Submit Button
    Button(patient_frame, text="Submit", justify=CENTER, command=add_patient_to_prolog).grid(row=20, column=0)


# Main Window
main_window = Tk()
main_window.title('MOH Expert System')
main_window.iconbitmap('./favicon.ico')
main_window.configure(bg="#353535")
main_window.geometry("900x600")

# Frames
main_frame = LabelFrame(main_window, text="Main Window", padx=40, pady=40, borderwidth=10, bg="#fff")
main_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

info_frame = LabelFrame(main_window, text=" ", padx=40, pady=40, borderwidth=10, bg="#fff")
info_frame.grid(row=0, column=1, padx=(20, 80), pady=100)

# Buttons
Button(main_frame, text="Add Condition/Ethnicity Fact", command=add_fact).grid(row=0, column=0, pady=10, padx=100,
                                                                               ipadx=26)
Button(main_frame, text="Add Patient Fact", command=add_patient).grid(row=2, column=0, pady=10, padx=100)
Button(main_frame, text="Diagnose Patient").grid(row=4, column=0, pady=10, padx=100, ipadx=33)
Button(main_frame, text="Display Statistics").grid(row=5, column=0, pady=10, padx=100, ipadx=33)

# Labels
Label(info_frame, text="This is an expert system developed to assist the Ministry of Health(MOH) in diagnosing the "
                       "COVID-19 virus. It will also display relevant statistics. Please select an option from the "
                       "list provided.", wraplength=150, justify=CENTER, bg="#fff").pack()

mainloop()
