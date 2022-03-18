from tkinter import *
from pyswip import Prolog
from tkinter import messagebox

# Used to connect to the Prolog Knowledge Base
prolog = Prolog()
prolog.consult("AI_Project.pl")

mild = 0
severe = 0
owupoint = 0
dpoint = 0
opoint = 0


# Commands
# This command adds facts entered by the user into the knowledge base
def add_fact():
    # Inner Commands
    # This function brings up the widgets necessary to enter a risky ethnicity
    def ethnicity():
        conditionbtn.destroy()
        ethnicitybtn.destroy()
        ethnicitylbl.grid(row=0, column=0)
        ethnicitytb.grid(row=0, column=1)
        esubmitbtn = Button(condition_window, text="Submit", command=sendEToDatabase)
        esubmitbtn.grid(row=1, column=0)
        backbtn = Button(condition_window, text="Go Back", command=read_fact)
        backbtn.grid(row=1, column=1)

    def sendCToDatabase():
        cond = conditiontb.get().capitalize()
        prolog.assertz(
            "underlying_condition('" + cond + "')")  # Adds the underlying condition entered into the knowledge base

        check = list(prolog.query("underlying_condition('" + cond + "')"))
        if len(check) == 0:
            messagebox.showerror("Error", "Underlying condition was not added.", parent=condition_window)
        else:
            messagebox.showinfo("Success", "Underlying condition was successfully added.", parent=condition_window)

    def sendEToDatabase():
        eth = ethnicitytb.get().capitalize()
        prolog.assertz("ethnicity('" + eth + "')")  # Adds the ethnicity entered into the knowledge base

        check = list(prolog.query("ethnicity('" + eth + "')"))
        if len(check) == 0:
            messagebox.showerror("Error", "Ethnicity was not added.", parent=condition_window)
        else:
            messagebox.showinfo("Success", "Ethnicity was successfully added.", parent=condition_window)

    # This function brings up the widgets necessary to enter an underlying condition
    def condition():
        conditionbtn.destroy()
        ethnicitybtn.destroy()
        conditionlbl.grid(row=0, column=0)
        conditiontb.grid(row=0, column=1)
        csubmitbtn = Button(condition_window, text="Submit", command=sendCToDatabase)
        csubmitbtn.grid(row=1, column=0)
        backbtn = Button(condition_window, text="Go Back", command=read_fact)
        backbtn.grid(row=1, column=1)

    # Allows the user to go back to choose whether to enter an at risk ethnicity or an underlying condition
    def read_fact():
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


# This function takes the information entered by the user about the patient and stores it into the knowledge base
def add_patient():
    # global gender, ans

    # Inner Commands
    # Adds the information to Prolog
    def add_patient_to_prolog():
        global mild, diagnosis, severe, owupoint, dpoint, opoint

        ppoints = 0
        pname = name.get().capitalize()
        page = age.get()
        pheight1 = height1.get()
        pheight2 = height2.get()
        ptemp = temp.get()
        pethnicity = selected.get().capitalize()
        pgender = gender.get()
        pweight = weight.get()
        pdfb = ans.get()
        psys = None
        pdia = None
        passage = True

        if pdfb == "yes":
            psys = systolic.get()
            pdia = diastolic.get()  # The systolic and diastolic values are retrieved if they experience dizziness, fainting or blurry vision

        if pname == "":
            messagebox.showwarning("NO NAME", "No name was entered.", parent=patient_window)
        elif page == "":
            messagebox.showwarning("NO AGE", "No age was entered.", parent=patient_window)
        elif ptemp == "":
            messagebox.showwarning("NO TEMPERATURE", "No temperature was entered.", parent=patient_window)
        elif pheight1 == "":
            messagebox.showwarning("NO HEIGHT", "No height (in feet) was entered.", parent=patient_window)
        elif pheight2 == "":
            messagebox.showwarning("NO HEIGHT", "No height (in inches) was entered.", parent=patient_window)
        elif pweight == "":
            messagebox.showwarning("NO WEIGHT", "No weight (in Kg) was entered.", parent=patient_window)
        else:
            ptemp = str(float("{0:.2f}".format((int(ptemp) * 1.8) + 32)))
            if pdfb == "yes":
                psys = systolic.get()
                pdia = diastolic.get()  # The systolic and diastolic values are retrieved if they experience dizziness, fainting or blurry vision
                if psys == "":
                    messagebox.showwarning("NO SYSTOLIC PRESSURE", "No systolic pressure was entered was entered.",
                                           parent=patient_window)
                elif pdia == "":
                    messagebox.showwarning("NO DIASTOLIC PRESSURE", "No diastolic pressure was entered.",
                                           parent=patient_window)
                else:

                    prolog.assertz(
                        "patientw('" + pname + "', " + page + "," + pheight1 + "," + pheight2 + "," + ptemp + ",'"
                        + pethnicity + "'," + pgender + "," + pweight + "," + pdfb + "," + psys + "," + pdia + ")")

                    c = list(prolog.query("get_patientw('" + pname + "',B,C,D,E,F,G,H,I,J,K)"))
                    if len(c) == 0:
                        messagebox.showerror("Error", "Patient was not added.", parent=patient_window)
                    else:
                        messagebox.showinfo("Success", "Patient was added successfully.", parent=patient_window)
            else:
                prolog.assertz(
                    "patientn('" + pname + "', " + page + "," + pheight1 + "," + pheight2 + "," + ptemp + ",'"
                    + pethnicity + "'," + pgender + "," + pweight + "," + pdfb + ")")

                c = list(prolog.query("get_patientn('" + pname + "',B,C,D,E,F,G,H,I)"))
                if len(c) == 0:
                    messagebox.showerror("Error", "Patient was not added.", parent=patient_window)
                else:
                    messagebox.showinfo("Success", "Patient was added successfully.", parent=patient_window)

            # The underlying conditions selected by the user is added to prolog along with the name of the patient who
            # experienced them
            conditions = []
            length = len(CONDITIONS)
            for con in range(length):
                if variables[con].get() == "On":
                    conditions.append(str(
                        CONDITIONS[
                            con]).capitalize())  # This list stores the underlying conditions the patient experienced

            for f in conditions:
                prolog.assertz("punderlying('" + pname + "','" + f + "')")
            c = list(prolog.query("get_punderlying('" + pname + "',B)"))
            print("Conditions")
            print(c)
            print()

            # The symptoms selected by the user is added to prolog along with the name of the patient who experienced them
            symptoms = []
            underlying_conditions = []
            lot = False
            for sym in range(len(SYMPTOMS)):
                if svariables[sym].get() == "On":
                    symptoms.append(SYMPTOMS[sym])  # This list stores the symptoms the patient experiences
                    ppoints += int(POINTS[sym])
                    if SYMPTOMS[sym] == "Loss of Taste":
                        lot = True
            for under in range(len(CONDITIONS)):
                if variables[under].get() == "On":
                    underlying_conditions.append(CONDITIONS[under])

            for h in symptoms:
                prolog.assertz("psymptoms('" + pname + "','" + h + "')")

            c = list(prolog.query("get_psymptoms('" + pname + "',B)"))
            print("Symptoms")
            print(c)
            print()

            if 0 <= ppoints < 6:
                diagnosis = "Based on the provided information, " + pname + " likely does not have the COVID virus."
            elif 6 <= ppoints < 17:
                mild += 1
                if lot and len(underlying_conditions) > 0:
                    owupoint += 1
                    diagnosis = "Based on the provided information, " + pname + " likely has the Omicron variant of the COVID virus with underlying conditions."
                elif lot:
                    opoint += 1
                    diagnosis = "Based on the provided information, " + pname + " likely has the Omicron variant of the COVID virus."
                else:
                    diagnosis = "Based on the provided information, " + pname + " has mild symptoms of the COVID virus."
            elif ppoints >= 17:
                severe += 1
                if lot:
                    dpoint += 1
                    diagnosis = "Based on the provided information, " + pname + " likely has the Delta variant of the COVID virus."
                else:
                    diagnosis = "Based on the provided information, " + pname + " likely has the Regular Variant of the COVID virus."

            prolog.retractall("virusstats(_,_,_,_,_)")
            prolog.assertz(
                "virusstats(" + str(mild) + "," + str(severe) + "," + str(opoint) + "," + str(dpoint) + "," + str(
                    owupoint) + ")")
            prolog.assertz("patientstats('" + pname + "','" + diagnosis + "')")
            # c = list(prolog.query("patientstats('" + pname + "',B)"))
            # print(c)
            # c = list(prolog.query("virusstats(A,B,C,D,E)"))
            # print(c)



    # If the patient experienced dizziness, fainting or blurry vision, this function adds the option to enter the
    # systolic and diastolic pressures of the patient to the frame. If not, it removes the option.
    def display_pressure(frame, val):
        global systolic, diastolic, syslbl, dialbl

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
    Label(patient_frame, text="Weight (in Kg)").grid(row=5, column=0)
    Label(patient_frame, text="Gender").grid(row=6, column=0)
    Label(patient_frame, text="Ethnicity").grid(row=7, column=0)
    Label(patient_frame, text="Experienced dizziness, fainting or blurry vision?").grid(row=8, column=0)
    Label(patient_frame, text="Underlying condition").grid(row=11, column=0)
    symptom = Label(patient_frame, text="Symptoms")

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
    weight.grid(row=5, column=1, columnspan=2)

    # Dropdown Menu
    selected = StringVar()
    ETHNICITY = [e['X'] for e in list(
        prolog.query("ethnicity(X)"))]  # This list stores all the risky ethnicities stored in the knowledge base
    selected.set(ETHNICITY[0])
    ethnicities = OptionMenu(patient_frame, selected, *ETHNICITY)
    ethnicities.grid(row=7, column=1, columnspan=2)

    # Checkbox
    CONDITIONS = [c['X'] for c in list(prolog.query(
        "underlying_condition(X)"))]  # This list stores all the underlying conditions stored in the knowledge base
    names = []
    variables = []
    # Creates the names as well as the variables necessary for the creation of the checkboxes.
    for x in range(len(CONDITIONS)):
        names.append("cb" + str(x))
        variables.append(StringVar(value="clicked" + str(x)))
    k = 0
    i = 11
    j = 1
    for c in range(len(CONDITIONS)):
        variables[k] = StringVar()
        names[k] = Checkbutton(patient_frame, text=CONDITIONS[k], variable=variables[k], onvalue="On", offvalue="Off")
        if j % 5 == 0:
            i += 1
            j = 1
        names[k].grid(row=i, column=j)
        names[k].deselect()
        k += 1
        j += 1

    SYMPTOMS = [s['A'] for s in
                list(prolog.query("symptoms(A,B)"))]  # This list stores all the symptoms stored in the knowledge base
    POINTS = [p['B'] for p in list(prolog.query(
        "symptoms(A,B)"))]  # This list stores all the point corrresponding to each symptom stored in the knowledge base
    values = []
    svariables = []

    # Creates the names as well as the variables necessary for the creation of the checkboxes.
    for y in range(len(SYMPTOMS)):
        values.append("sym" + str(y))
        svariables.append(StringVar(value="option" + str(y)))

    l = 0
    u = i + 1
    e = 1
    symptom.grid(row=u, column=0)

    for s in range(len(SYMPTOMS)):
        svariables[l] = StringVar()
        values[l] = Checkbutton(patient_frame, text=SYMPTOMS[l], variable=svariables[l], onvalue="On", offvalue="Off")
        if e % 5 == 0:
            u += 1
            e = 1
        values[l].grid(row=u, column=e)
        values[l].deselect()
        l += 1
        e += 1

    # Radio Button
    gender = StringVar()
    gender.set("male")
    Radiobutton(patient_frame, text="Male", variable=gender, value="male").grid(row=6, column=1)
    Radiobutton(patient_frame, text="Female", variable=gender, value="female").grid(row=6, column=2)

    ans = StringVar()
    ans.set("no")
    ansbtn1 = Radiobutton(patient_frame, text="Yes", variable=ans, value="yes",
                          command=lambda: display_pressure(patient_frame, 0))
    ansbtn1.grid(row=8, column=1)
    ansbtn2 = Radiobutton(patient_frame, text="No", variable=ans, value="no",
                          command=lambda: display_pressure(patient_frame, 1))
    ansbtn2.grid(row=8, column=2)

    radio_buttons = [ansbtn1, ansbtn2]

    # Submit Button
    submit = Button(patient_frame, text="Submit", justify=CENTER, command=add_patient_to_prolog)
    submit.grid(row=u + 2, column=2)
    submit.rowconfigure(20, weight=1)
    submit.columnconfigure(2, weight=1)


def display_statistics():
    pstatistics = [(st['A'], st['B'], st['C'], st['D'], st['E']) for st in list(prolog.query("virusstats(A,B,C,D,E)"))]
    mosres = 0
    doores = 0
    i = 0
    for stats in pstatistics[0]:
        if i < 2:
            mosres += pstatistics[0][i]
        else:
            doores += pstatistics[0][i]
        print("Total for severe/mild: " + str(mosres))
        print("Total for COVID TYPE: " + str(doores))
        print()
        i += 1

    if mosres > 0:
        pmild = float("{0:.1f}".format((pstatistics[0][0] / mosres) * 100))
        psevere = float("{0:.1f}".format((pstatistics[0][1] / mosres) * 100))
    else:
        pmild = float("{0:.1f}".format(pstatistics[0][0]))
        psevere = float("{0:.1f}".format(pstatistics[0][1]))

    if doores > 0:
        pdelta = float("{0:.1f}".format((pstatistics[0][2] / doores) * 100))
        pomicron = float("{0:.1f}".format((pstatistics[0][3] / doores) * 100))
        puomicron = float("{0:.1f}".format((pstatistics[0][4] / doores) * 100))
    else:
        pdelta = float("{0:.1f}".format(pstatistics[0][2]))
        pomicron = float("{0:.1f}".format(pstatistics[0][3]))
        puomicron = float("{0:.1f}".format(pstatistics[0][4]))

    # Window
    statistics_window = Toplevel()
    statistics_window.title('Display Statistics')
    statistics_window.iconbitmap('./favicon.ico')
    statistics_window.configure(bg="#353535")
    statistics_window.geometry("850x600")

    # Frame
    statistics_frame = LabelFrame(statistics_window, text="Condition Details", padx=40, pady=40, borderwidth=10,
                                  bg="#fff")
    statistics_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

    # Labels
    Label(statistics_frame, text="The patients with mild symptoms: " + str(pmild) + "%",
          justify=CENTER, bg="#fff").pack(pady=10)
    Label(statistics_frame, text="The patients with severe symptoms: " + str(psevere) + "%",
          justify=CENTER, bg="#fff").pack(pady=10)
    Label(statistics_frame, text="The patients with the Delta Variant: " + str(pdelta) + "%",
          justify=CENTER, bg="#fff").pack(pady=10)
    Label(statistics_frame, text="The patients with the Omicron Variant: " + str(pomicron) + "%",
          justify=CENTER, bg="#fff").pack(pady=10)
    Label(statistics_frame, text="The patients with the Omicron Variant with underlying conditions: " +
                                 str(puomicron) + "%", justify=CENTER, bg="#fff").pack(pady=10)


def diagnose_patient():
    # Inner Commands
    def retrieve_patient():
        patient_age = None
        patient_height1 = None
        patient_height2 = None
        patient_temp = None
        patient_ethnicity = None
        patient_gender = None
        patient_weight = None
        patient_experience = None
        patient_systolic = None
        patient_diastolic = None
        pat_name = patient_name.get().capitalize()

        patient_name.destroy()
        patientlbl.destroy()
        display.destroy()

        patient_info1 = list(prolog.query("get_patientw('" + pat_name + "',B,C,D,E,F,G,H,I,J,K)"))
        patient_info2 = list(prolog.query("get_patientn('" + pat_name + "',B,C,D,E,F,G,H,I)"))

        if len(patient_info1) > 0:
            patient_age = patient_info1[0]['B']
            patient_height1 = patient_info1[0]['C']
            patient_height2 = patient_info1[0]['D']
            patient_temp = patient_info1[0]['E']
            patient_ethnicity = patient_info1[0]['F']
            patient_gender = patient_info1[0]['G']
            patient_weight = patient_info1[0]['H']
            patient_experience = patient_info1[0]['I']
            patient_systolic = patient_info1[0]['J']
            patient_diastolic = patient_info1[0]['K']
            print(patient_age)
            print(patient_height1)
            print(patient_height2)
            print(patient_temp)
            print(patient_ethnicity)
            print(patient_gender)
            print(patient_weight)
            print(patient_experience)
            print(patient_systolic)
            print(patient_diastolic)
        elif len(patient_info2) > 0:
            patient_age = patient_info2[0]['B']
            patient_height1 = patient_info2[0]['C']
            patient_height2 = patient_info2[0]['D']
            patient_temp = patient_info2[0]['E']
            patient_ethnicity = patient_info2[0]['F']
            patient_gender = patient_info2[0]['G']
            patient_weight = patient_info2[0]['H']
            patient_experience = patient_info2[0]['I']
            print(patient_age)
            print(patient_height1)
            print(patient_height2)
            print(patient_temp)
            print(patient_ethnicity)
            print(patient_gender)
            print(patient_weight)
            print(patient_experience)
        elif len(patient_info1) == 0 and len(patient_info2) == 0:
            messagebox.showerror("Error", "Patient does not exist.", parent=diagnosis_window)

        bmi = patient_weight/(((patient_height1 * 0.3048) + (patient_height2 * 0.0254)) ** 2)


    # Window
    diagnosis_window = Toplevel()
    diagnosis_window.title('Patient Diagnosis')
    diagnosis_window.iconbitmap('./favicon.ico')
    diagnosis_window.configure(bg="#353535")
    diagnosis_window.geometry("850x600")

    # Frame
    diagnosis_frame = LabelFrame(diagnosis_window, text="Condition Details", padx=40, pady=40, borderwidth=10,
                                 bg="#fff")
    diagnosis_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

    # Label
    patientlbl = Label(diagnosis_frame, text="Enter the patient's name ")
    patientlbl.grid(row=0, column=0)

    # Text Box
    patient_name = Entry(diagnosis_frame, width=30)
    patient_name.grid(row=0, column=1, columnspan=2)

    # Button
    display = Button(diagnosis_frame, text="Display Patient", justify=CENTER, command=retrieve_patient)
    display.grid(row=1, column=2)
    display.rowconfigure(20, weight=1)
    display.columnconfigure(2, weight=1)


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
Button(main_frame, text="Diagnose Patient", command=diagnose_patient).grid(row=4, column=0, pady=10, padx=100, ipadx=33)
Button(main_frame, text="Display Statistics", command=display_statistics).grid(row=5, column=0, pady=10, padx=100,
                                                                               ipadx=33)

# Labels
Label(info_frame, text="This is an expert system developed to assist the Ministry of Health(MOH) in diagnosing the "
                       "COVID-19 virus. It will also display relevant statistics. Please select an option from the "
                       "list provided.", wraplength=150, justify=CENTER, bg="#fff").pack()

mainloop()
