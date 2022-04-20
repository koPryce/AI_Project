from tkinter import *
from pyswip import Prolog
from tkinter import messagebox, ttk
from functools import partial

# Used to connect to the Prolog Knowledge Base
prolog = Prolog()
prolog.consult("AI_Project.pl")

regular = 0
mild = 0
severe = 0
owupoint = 0
dpoint = 0
opoint = 0


# Commands
# This command adds facts entered by the user into the knowledge base
def add_fact():
    # Inner Commands
    # This function brings up the widgets necessary to enter an at risk ethnicity
    def ethnicity():
        conditionbtn.destroy()
        ethnicitybtn.destroy()
        locationbtn.destroy()
        ethnicitylbl.grid(row=0, column=0)
        ethnicitytb.grid(row=0, column=1)
        esubmitbtn = Button(condition_window, text="Submit", command=sendEToDatabase)
        esubmitbtn.grid(row=1, column=0, padx=5, pady=9)
        backbtn = Button(condition_window, text="Go Back", command=read_fact)
        backbtn.grid(row=1, column=1)

    # This function brings up the widgets necessary to enter an underlying condition
    def condition():
        conditionbtn.destroy()
        ethnicitybtn.destroy()
        locationbtn.destroy()
        conditionlbl.grid(row=0, column=0)
        conditiontb.grid(row=0, column=1)
        csubmitbtn = Button(condition_window, text="Submit", command=sendCToDatabase)
        csubmitbtn.grid(row=1, column=0, padx=5, pady=9)
        backbtn = Button(condition_window, text="Go Back", command=read_fact)
        backbtn.grid(row=1, column=1)

    # This function brings up the widgets necessary to enter an at risk location
    def location():
        conditionbtn.destroy()
        ethnicitybtn.destroy()
        locationbtn.destroy()
        locationlbl.grid(row=0, column=0)
        locationtb.grid(row=0, column=1)
        lsubmitbtn = Button(condition_window, text="Submit", command=sendLToDatabase)
        lsubmitbtn.grid(row=1, column=0, padx=5, pady=9)
        backbtn = Button(condition_window, text="Go Back", command=read_fact)
        backbtn.grid(row=1, column=1)

    # This function sends the underlying_condition to the knowledge base
    def sendCToDatabase():
        cond = conditiontb.get().capitalize()
        search = list(prolog.query(
            "get_condition(X)"))
        if any(c['X'] == cond for c in search):  # Checks if the underlying condition was already entered
            messagebox.showinfo("Already Entered", "This underlying condition was already entered.",
                                parent=condition_window)
        elif cond == "":
            messagebox.showerror("Error", "Text Field is empty. Enter a condition.", parent=condition_window)
        else:
            prolog.assertz(
                "underlying_condition('" + cond + "')")  # Adds the underlying condition entered into the knowledge base
            check = list(prolog.query(
                "get_condition(X)"))  # Checks if the underlying condition is in the knowledge base.
            if not any(c['X'] == cond for c in check):
                messagebox.showerror("Error", "Underlying condition was not added.", parent=condition_window)
            else:
                conditiontb.delete(0, END)
                messagebox.showinfo("Success", "Underlying condition was successfully added.", parent=condition_window)

    # This function sends the ethnicity to the knowledge base
    def sendEToDatabase():
        eth = ethnicitytb.get().capitalize()
        search = list(prolog.query(
            "get_ethnicity(X)"))
        if any(e['X'] == eth for e in search):  # Checks if the ethnicity was already entered
            messagebox.showinfo("Already Entered", "This ethnicity was already entered.", parent=condition_window)
        elif eth == "":
            messagebox.showerror("Error", "Text Field is empty. Enter an ethnicity.", parent=condition_window)
        else:
            prolog.assertz(
                "ethnicity('" + eth + "')")  # Adds the ethnicity entered into the knowledge base
            check = list(prolog.query(
                "get_ethnicity(X)"))  # Checks if the ethnicity is in the knowledge base.
            if not any(e['X'] == eth for e in check):
                messagebox.showerror("Error", "Ethnicity was not added.", parent=condition_window)
            else:
                ethnicitytb.delete(0, END)
                messagebox.showinfo("Success", "Ethnicity was successfully added.", parent=condition_window)

    # This function sends the location to the knowledge base
    def sendLToDatabase():
        loc = locationtb.get().capitalize()
        search = list(prolog.query(
                "get_location(X)"))
        if any(l['X'] == loc for l in search):  # Checks if the location was already entered
            messagebox.showinfo("Already Entered", "This location was already entered.", parent=condition_window)
        elif loc == "":
            messagebox.showerror("Error", "Text Field is empty. Enter a location.", parent=condition_window)
        else:
            prolog.assertz(
                "location('" + loc + "')")  # Adds the location entered into the knowledge base
            check = list(prolog.query(
                "get_location(X)"))  # Checks if the location is in the knowledge base.
            if not any(l['X'] == loc for l in check):
                messagebox.showerror("Error", "Location was not added.", parent=condition_window)
            else:
                locationtb.delete(0, END)
                messagebox.showinfo("Success", "Location was successfully added.", parent=condition_window)

    # Allows the user to go back to choose whether to enter an at risk ethnicity, at risk location or an underlying condition
    def read_fact():
        condition_window.destroy()
        add_fact()

    # Window
    condition_window = Toplevel()
    condition_window.title('Add Condition Fact')
    condition_window.iconbitmap('./favicon.ico')
    condition_window.configure(bg="#353535")
    condition_window.geometry("500x150")
    condition_window.resizable(False, False)

    # Labels
    backlbl = Label(condition_window, text="<--Back to Main", padx=37, bg="#30D5C8")
    backlbl.bind("<Enter>", partial(configureColor, backlbl, "blue"))
    backlbl.bind("<Leave>", partial(configureColor, backlbl, "black"))
    backlbl.bind("<Button-1>", lambda e: goBack(condition_window))
    conditionlbl = Label(condition_window, text="Enter an underlying condition")
    ethnicitylbl = Label(condition_window, text="Enter an at risk ethnicity")
    locationlbl = Label(condition_window, text="Enter an at risk location")

    # Text Boxes
    conditiontb = Entry(condition_window, width=50)
    ethnicitytb = Entry(condition_window, width=50)
    locationtb = Entry(condition_window, width=50)

    # Buttons
    conditionbtn = Button(condition_window, text="Add an underlying condition", command=condition, padx=5)
    ethnicitybtn = Button(condition_window, text="Add an at risk ethnicity", command=ethnicity, padx=20)
    locationbtn = Button(condition_window, text="Add an at risk location", command=location, padx=20)

    conditionbtn.grid(row=0, column=0, padx=5, pady=7)
    ethnicitybtn.grid(row=1, column=0, padx=5, pady=7)
    locationbtn.grid(row=2, column=0, padx=5, pady=7)
    backlbl.grid(row=3, column=0, pady=7)


# This function takes the information entered by the user about the patient and stores it into the knowledge base
def add_patient():
    # Inner Commands
    # Adds the information to Prolog
    def add_patient_to_prolog():
        global regular, mild, diagnosis, patient_advice, moh_advice, severe, owupoint, dpoint, opoint

        ppoints = 0
        pname = name.get().capitalize()
        page = age.get()
        pheight1 = height1.get()
        pheight2 = height2.get()
        ptemp = temp.get()
        pethnicity = selected.get().capitalize()
        pgender = gender.get().capitalize()
        pweight = weight.get()
        pexperience = ans.get().capitalize()
        plocation = location.get().capitalize()
        psys = None
        pdia = None
        passage = True

        if pexperience == "Yes":
            psys = systolic.get()
            pdia = diastolic.get()  # The systolic and diastolic values are retrieved if they experience dizziness, fainting or blurred vision

        if pname == "":
            messagebox.showwarning("NO NAME", "No name was entered.", parent=patient_window)
        elif page == "":
            messagebox.showwarning("NO AGE", "No age was entered.", parent=patient_window)
        elif not page.isdigit():
            messagebox.showwarning("AGE IS NOT A NUMBER", "A number wasn't entered for the age.", parent=patient_window)
        elif ptemp == "":
            messagebox.showwarning("NO TEMPERATURE", "No temperature was entered.", parent=patient_window)
        elif not ptemp.isdigit():
            messagebox.showwarning("TEMPERATURE IS NOT A NUMBER", "A number wasn't entered for the temperature.", parent=patient_window)
        elif pheight1 == "":
            messagebox.showwarning("NO HEIGHT", "No height (in feet) was entered.", parent=patient_window)
        elif not pheight1.isdigit():
            messagebox.showwarning("HEIGHT IS NOT A NUMBER", "A number wasn't entered for the height (in feet).", parent=patient_window)
        elif pheight2 == "":
            messagebox.showwarning("NO HEIGHT", "No height (in inches) was entered.", parent=patient_window)
        elif not pheight2.isdigit():
            messagebox.showwarning("HEIGHT IS NOT A NUMBER", "A number wasn't entered for the height (in inches).", parent=patient_window)
        elif pweight == "":
            messagebox.showwarning("NO WEIGHT", "No weight (in Kg) was entered.", parent=patient_window)
        elif not pweight.isdigit():
            messagebox.showwarning("WEIGHT IS NOT A NUMBER", "A number wasn't entered for weight (in Kg).", parent=patient_window)
        elif pethnicity == "(empty)":
            messagebox.showerror("Error", "Please enter an ethnicity before proceeding.",
                                 parent=patient_window)
        elif plocation == "(empty)":
            messagebox.showerror("Error", "Please enter a location before proceeding.",
                                 parent=patient_window)
        elif CONDITIONS[0] == "(empty)":
            messagebox.showerror("Error", "Please enter an underlying condition before proceeding.",
                                 parent=patient_window)
        else:
            if int(ptemp) >= 38:
                ppoints += 3
            pinfo2 = list(prolog.query("get_patient_info2('" + pname + "',B,C,D,E,F,G,H,I,J,K,L)"))
            pinfo1 = list(prolog.query("get_patient_info1('" + pname + "',B,C,D,E,F,G,H,I,J)"))
            ptemp = str(float(
                "{0:.2f}".format((int(ptemp) * 1.8) + 32)))  # The temperature is converted from celsius to fahrenheit
            if pexperience == "Yes":
                psys = systolic.get()
                pdia = diastolic.get()  # The systolic and diastolic values are retrieved if they experienced dizziness, fainting or blurred vision
                if psys == "":
                    messagebox.showwarning("NO SYSTOLIC PRESSURE", "No systolic pressure was entered was entered.",
                                           parent=patient_window)
                elif pdia == "":
                    messagebox.showwarning("NO DIASTOLIC PRESSURE", "No diastolic pressure was entered.",
                                           parent=patient_window)
                elif not psys.isdigit():
                    messagebox.showwarning("SYSTOLIC PRESSURE IS NOT A NUMBER", "A number wasn't entered for the systolic pressure", parent=patient_window)
                elif not pdia.isdigit():
                    messagebox.showwarning("DIASTOLIC PRESSURE IS NOT A NUMBER", "A number wasn't entered for the diastolic pressure", parent=patient_window)
                elif len(pinfo2) > 0:
                    messagebox.showinfo("Already Entered", "This patient was already entered.",
                                        parent=patient_window)
                else:
                    # Inserts the patient's information into the knowledge base if they experienced dizziness, fainting or blurred vision
                    prolog.assertz(
                        "patient_info2('" + pname + "', " + page + "," + pheight1 + "," + pheight2 + "," + ptemp + ",'"
                        + plocation + "','" + pethnicity + "','" + pgender + "'," + pweight + ",'" + pexperience + "'," + psys + "," + pdia + ")")

                    c = list(prolog.query("get_patient_info2('" + pname + "',B,C,D,E,F,G,H,I,J,K,L)"))
                    if len(c) == 0:
                        messagebox.showerror("Error", "Patient was not added.", parent=patient_window)
                    elif len(c) > 0:
                        messagebox.showinfo("Success", "Patient was added successfully.", parent=patient_window)
            else:
                if len(pinfo1) > 0:
                    messagebox.showinfo("Already Entered", "This patient was already entered.",
                                        parent=patient_window)
                else:
                    # Inserts the patient's information into the knowledge base if they didn't experience dizziness, fainting or blurred vision
                    prolog.assertz(
                        "patient_info1('" + pname + "', " + page + "," + pheight1 + "," + pheight2 + "," + ptemp + ",'"
                        + plocation + "','" + pethnicity + "','" + pgender + "'," + pweight + ",'" + pexperience + "')")

                    c = list(prolog.query("get_patient_info1('" + pname + "',B,C,D,E,F,G,H,I,J)"))
                    if len(c) == 0:
                        messagebox.showerror("Error", "Patient was not added.", parent=patient_window)
                    elif len(c) > 0:
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
                prolog.assertz("patient_condition('" + pname + "','" + f + "')")

            # The symptoms selected by the user is added to prolog along with the name of the patient who experienced them
            symptoms = []
            lot = False
            for sym in range(len(SYMPTOMS)):
                if svariables[sym].get() == "On":
                    symptoms.append(SYMPTOMS[sym])  # This list stores the symptoms the patient experiences
                    ppoints += int(POINTS[sym])
                    if SYMPTOMS[sym] == "Loss of Taste":
                        lot = True
            for h in symptoms:
                prolog.assertz("patient_symptoms('" + pname + "','" + h + "')")

            name.delete(0, END)
            age.delete(0, END)
            temp.delete(0, END)
            height1.delete(0, END)
            height2.delete(0, END)
            weight.delete(0, END)
            for de in range(len(CONDITIONS)):
                names[de].deselect()

            for de in range(len(SYMPTOMS)):
                values[de].deselect()
            if pexperience == "Yes":
                systolic.delete(0, END)
                diastolic.delete(0, END)

            if 0 <= ppoints < 6:
                diagnosis = "Based on the provided information, " + pname + " likely does not have the COVID virus"
                patient_advice = "None"
                moh_advice = "None"
            elif 6 <= ppoints < 17:
                mild += 1
                if lot and len(conditions) > 0:
                    owupoint += 1
                    diagnosis = "Based on the provided information, " + pname + " likely has the Omicron variant of the COVID virus with underlying conditions"
                    patient_advice = "Self quarantine. Clean your hands regularly. Call ahead before visiting your doctor."
                    moh_advice = "Do testing of the members of the household and immediate contacts of the patient and check if they have underlying conditions."
                elif lot:
                    opoint += 1
                    diagnosis = "Based on the provided information, " + pname + " likely has the Omicron variant of the COVID virus"
                    patient_advice = "Self quarantine. Clean your hands regularly."
                    moh_advice = "Do testing of the members of the household and immediate contacts of the patient."
                else:
                    diagnosis = "Based on the provided information, " + pname + " has mild symptoms of the COVID virus"
                    patient_advice = "Clean your hands regularly. Clean your house regularly. Avoid sharing personal household items."
                    moh_advice = "Send a reminder for them to revisit there doctor."
            elif ppoints >= 17:
                severe += 1
                if lot:
                    dpoint += 1
                    diagnosis = "Based on the provided information, " + pname + " likely has the Delta variant of the COVID virus"
                    patient_advice = "Self quarantine. Call ahead before visiting your doctor."
                    moh_advice = "Place the patient community under quarantine. Do testing of residents in the community."
                else:
                    regular += 1
                    diagnosis = "Based on the provided information, " + pname + " likely has the Regular Variant of the COVID virus"
                    patient_advice = "Get tested for the virus. Stay home unless seeking medical care. Monitor your symptoms."
                    moh_advice = "Send regular reminders to the patient."

            prolog.retractall("virusstats(_,_,_,_,_,_)")
            prolog.assertz(
                "virusstats(" + str(mild) + "," + str(severe) + ", " + str(
                    regular) + "," + str(dpoint) + "," + str(opoint) + "," + str(
                    owupoint) + ")")
            prolog.assertz(
                "patientstats('" + pname + "','" + diagnosis + "','" + patient_advice + "','" + moh_advice + "')")  # Adds the patient's diagnosis, advice and the advice to give the moh to the knowledge base.

    # If the patient experienced dizziness, fainting or blurred vision, this function adds the option to enter the
    # systolic and diastolic pressures of the patient to the frame. If not, it removes the option.
    def display_pressure(frame, val):
        global systolic, diastolic, syslbl, dialbl

        if radio_buttons[val]['text'] == "Yes":
            syslbl = Label(frame, text="Systolic Pressure")
            dialbl = Label(frame, text="Diastolic Pressure")
            systolic = Entry(frame, width=30)
            diastolic = Entry(frame, width=30)
            syslbl.grid(row=10, column=0)
            dialbl.grid(row=11, column=0)
            systolic.grid(row=10, column=1, columnspan=2)
            diastolic.grid(row=11, column=1, columnspan=2)

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
    patient_window.resizable(False, False)
    patient_window.geometry("1110x670+100+75")

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
    Label(patient_frame, text="Location").grid(row=8, column=0)
    Label(patient_frame, text="Experienced dizziness, fainting or blurred vision?").grid(row=9, column=0)
    Label(patient_frame, text="Underlying condition").grid(row=12, column=0)
    symptom = Label(patient_frame, text="Symptoms")
    backlbl = Label(patient_frame, text="<--Back to Main", bg="#30D5C8")
    backlbl.bind("<Enter>", partial(configureColor, backlbl, "blue"))
    backlbl.bind("<Leave>", partial(configureColor, backlbl, "black"))
    backlbl.bind("<Button-1>", lambda e: goBack(patient_window))

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
        prolog.query("get_ethnicity(X)"))]  # This list stores all the risky ethnicities stored in the knowledge base

    if len(ETHNICITY) > 1:
        ETHNICITY.pop(0)

    selected.set(ETHNICITY[0])
    ethnicities = OptionMenu(patient_frame, selected, *ETHNICITY)
    ethnicities.grid(row=7, column=1, columnspan=2)

    location = StringVar()
    LOCATION = [loc['X'] for loc in list(
        prolog.query("get_location(X)"))]  # This list stores all the risky locations stored in the knowledge base

    if len(LOCATION) > 1:
        LOCATION.pop(0)

    location.set(LOCATION[0])
    locations = OptionMenu(patient_frame, location, *LOCATION)
    locations.grid(row=8, column=1, columnspan=2)

    # Checkbox
    CONDITIONS = [c['X'] for c in list(prolog.query(
        "get_condition(X)"))]  # This list stores all the underlying conditions stored in the knowledge base
    names = []
    variables = []

    if len(CONDITIONS) > 1:
        CONDITIONS.pop(0)

    # Creates the names as well as the variables necessary for the creation of the checkboxes.
    for x in range(len(CONDITIONS)):
        names.append("cb" + str(x))
        variables.append(StringVar(value="clicked" + str(x)))
    k = 0
    i = 12
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
                list(prolog.query(
                    "symptoms(name(A),point(B))"))]  # This list stores all the symptoms stored in the knowledge base
    POINTS = [p['B'] for p in list(prolog.query(
        "symptoms(name(A),point(B))"))]  # This list stores all the point corresponding to each symptom stored in the knowledge base
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
    ansbtn1.grid(row=9, column=1)
    ansbtn2 = Radiobutton(patient_frame, text="No", variable=ans, value="no",
                          command=lambda: display_pressure(patient_frame, 1))
    ansbtn2.grid(row=9, column=2)

    radio_buttons = [ansbtn1, ansbtn2]

    # Submit Button
    submit = Button(patient_frame, text="Submit", justify=CENTER, command=add_patient_to_prolog, padx=10)
    submit.grid(row=u + 2, column=2, padx=5, pady=9)
    submit.rowconfigure(20, weight=1)
    submit.columnconfigure(2, weight=1)
    backlbl.grid(row=u + 3, column=0)


# This function displays the statistics of the overall diagnosed patients
def display_statistics():
    pstatistics = [(st['A'], st['B'], st['C'], st['D'], st['E'], st['F']) for st in list(prolog.query(
        "virusstats(A, B, C, D, E, F)"))]  # Gets the statistics of the patients from the knowledge base.
    mosres = 0
    doores = 0
    i = 0
    for stats in pstatistics[0]:
        if i < 2:
            mosres += pstatistics[0][i]
        else:
            doores += pstatistics[0][i]
        i += 1

    if mosres > 0:
        pmild = float("{0:.1f}".format((pstatistics[0][0] / mosres) * 100))
        psevere = float("{0:.1f}".format((pstatistics[0][1] / mosres) * 100))
    else:
        pmild = float("{0:.1f}".format(pstatistics[0][0]))
        psevere = float("{0:.1f}".format(pstatistics[0][1]))

    if doores > 0:
        pdelta = float("{0:.1f}".format((pstatistics[0][3] / doores) * 100))
        pomicron = float("{0:.1f}".format((pstatistics[0][4] / doores) * 100))
        puomicron = float("{0:.1f}".format((pstatistics[0][5] / doores) * 100))
    else:
        pdelta = float("{0:.1f}".format(pstatistics[0][3]))
        pomicron = float("{0:.1f}".format(pstatistics[0][4]))
        puomicron = float("{0:.1f}".format(pstatistics[0][5]))

    # Window
    statistics_window = Toplevel()
    statistics_window.title('Display Statistics')
    statistics_window.iconbitmap('./favicon.ico')
    statistics_window.configure(bg="#353535")
    statistics_window.geometry("850x600+100+50")

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

    backlbl = Label(statistics_frame, text="<--Back to Main", bg="#30D5C8")
    backlbl.bind("<Enter>", partial(configureColor, backlbl, "blue"))
    backlbl.bind("<Leave>", partial(configureColor, backlbl, "black"))
    backlbl.bind("<Button-1>", lambda e: goBack(statistics_window))
    backlbl.pack(pady=10)


# This function is used to display the diagnosis of a specific patient.
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
        patient_location = None
        patient_experience = None
        patient_systolic = None
        patient_diastolic = None
        pat_name = patient_name.get().capitalize()

        patient_name.destroy()
        patientlbl.destroy()
        display.destroy()

        patient_info2 = list(prolog.query("get_patient_info2('" + pat_name + "',B,C,D,E,F,G,H,I,J,K,L)"))
        patient_info1 = list(prolog.query("get_patient_info1('" + pat_name + "',B,C,D,E,F,G,H,I,J)"))

        if len(patient_info2) > 0:
            patient_age = patient_info2[0]['B']
            patient_height1 = patient_info2[0]['C']
            patient_height2 = patient_info2[0]['D']
            patient_temp = patient_info2[0]['E']
            patient_location = patient_info2[0]['F'].capitalize()
            patient_ethnicity = patient_info2[0]['G'].capitalize()
            patient_gender = patient_info2[0]['H'].capitalize()
            patient_weight = patient_info2[0]['I']
            patient_experience = patient_info2[0]['J'].capitalize()
            patient_systolic = patient_info2[0]['K']
            patient_diastolic = patient_info2[0]['L']

            patient_height = ((float(patient_height1) * 0.3048) + (float(patient_height2) * 0.0254))

            bmi = float("{0:.2f}".format(patient_weight / (patient_height ** 2)))

            Label(subdiagnosis_frame, text="Name: " + pat_name, justify=CENTER, bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame, text="Age: " + str(patient_age) + " years old", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Gender: " + patient_gender, justify=CENTER, bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame, text="Ethnicity: " + patient_ethnicity, justify=CENTER, bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame, text="Location: " + str(patient_location), justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Temperature: " + str(patient_temp) + "°F", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Height: " + str(patient_height) + "m", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Weight: " + str(patient_weight) + "kg", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="BMI: " + str(bmi), justify=CENTER, bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame, text="Systolic Pressure: " + str(patient_systolic) + " mm Hg", justify=CENTER,
                  bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame, text="Diastolic Pressure: " + str(patient_diastolic) + " mm Hg", justify=CENTER,
                  bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame,
                  text="Experienced dizziness, fainting or blurred vision: " + patient_experience, justify=CENTER,
                  bg="#fff").pack(pady=10)

            if bmi < 18.5:
                Label(subdiagnosis_frame,
                      text="Based on this person's bmi, they are underweight", justify=CENTER,
                      bg="#fff").pack(pady=10)
            elif 18.5 < bmi < 24.9:
                Label(subdiagnosis_frame,
                      text="Based on this person's bmi, they are healthy", justify=CENTER,
                      bg="#fff").pack(pady=10)
            elif 25.0 < bmi < 29.9:
                Label(subdiagnosis_frame,
                      text="Based on this person's bmi, they are overweight", justify=CENTER,
                      bg="#fff").pack(pady=10)
            else:
                Label(subdiagnosis_frame,
                      text="Based on this person's bmi, they are obese", justify=CENTER,
                      bg="#fff").pack(pady=10)

            if patient_systolic < 90 or patient_diastolic < 60:
                Label(subdiagnosis_frame, text="Patient has low blood pressure", justify=CENTER, bg="#fff").pack(
                    pady=10)

            condition_list = [c['X'] for c in list(prolog.query("get_patient_condition('" + pat_name + "',X)"))]

            symptoms_list = [s['X'] for s in list(prolog.query("get_patient_symptoms('" + pat_name + "',X)"))]

            condition_tb = Text(subdiagnosis_frame, height=10, width=50)
            condition_tb.config(state="normal")
            for c in condition_list:
                condition_tb.insert(INSERT, str(c) + "\n")

            condition_tb.config(state=DISABLED)
            condition_tb.pack(pady=10)

            symptoms_tb = Text(subdiagnosis_frame, height=10, width=50)
            symptoms_tb.config(state="normal")
            for s in symptoms_list:
                symptoms_tb.insert(INSERT, str(s) + "\n")

            symptoms_tb.config(state=DISABLED)
            symptoms_tb.pack(pady=10)

            patient_diagnosis = [d['X'] for d in list(prolog.query("get_patientstats('" + pat_name + "',X,Y,Z)"))]
            patientadvice = [p['Y'] for p in list(prolog.query("get_patientstats('" + pat_name + "',X,Y,Z)"))]
            mohadvice = [m['Z'] for m in list(prolog.query("get_patientstats('" + pat_name + "',X,Y,Z)"))]

            Label(subdiagnosis_frame, text="Diagnosis: " + patient_diagnosis[0] + ".", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Advice to Patient: " + patientadvice[0], justify=CENTER,
                  bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Advice to MOH: " + mohadvice[0], justify=CENTER, bg="#fff").pack(
                pady=10)

        elif len(patient_info1) > 0:
            patient_age = patient_info1[0]['B']
            patient_height1 = patient_info1[0]['C']
            patient_height2 = patient_info1[0]['D']
            patient_temp = patient_info1[0]['E']
            patient_location = patient_info1[0]['F'].capitalize()
            patient_ethnicity = patient_info1[0]['G'].capitalize()
            patient_gender = patient_info1[0]['H'].capitalize()
            patient_weight = patient_info1[0]['I']
            patient_experience = patient_info1[0]['J'].capitalize()

            patient_height = ((float(patient_height1) * 0.3048) + (float(patient_height2) * 0.0254))

            bmi = float("{0:.2f}".format(patient_weight / (patient_height ** 2)))

            Label(subdiagnosis_frame, text="Name: " + pat_name, justify=CENTER, bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame, text="Age: " + str(patient_age) + " years old", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Gender: " + patient_gender, justify=CENTER, bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame, text="Ethnicity: " + patient_ethnicity, justify=CENTER, bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame, text="Location: " + str(patient_location), justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Temperature: " + str(patient_temp) + "°F", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Height: " + str(patient_height) + "m", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Weight: " + str(patient_weight) + "kg", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="BMI: " + str(bmi), justify=CENTER, bg="#fff").pack(pady=10)
            Label(subdiagnosis_frame,
                  text="Experienced dizziness, fainting or blurred vision: " + patient_experience, justify=CENTER,
                  bg="#fff").pack(pady=10)

            if bmi < 18.5:
                Label(subdiagnosis_frame,
                      text="Based on this person's bmi, they are underweight", justify=CENTER,
                      bg="#fff").pack(pady=10)
            elif 18.5 < bmi < 24.9:
                Label(subdiagnosis_frame,
                      text="Based on this person's bmi, they are healthy", justify=CENTER,
                      bg="#fff").pack(pady=10)
            elif 25.0 < bmi < 29.9:
                Label(subdiagnosis_frame,
                      text="Based on this person's bmi, they are overweight", justify=CENTER,
                      bg="#fff").pack(pady=10)
            else:
                Label(subdiagnosis_frame,
                      text="Based on this person's bmi, they are obese", justify=CENTER,
                      bg="#fff").pack(pady=10)

            condition_list = [c['X'] for c in list(prolog.query("get_patient_condition('" + pat_name + "',X)"))]

            symptoms_list = [s['X'] for s in list(prolog.query("get_patient_symptoms('" + pat_name + "',X)"))]

            condition_tb = Text(subdiagnosis_frame, height=10, width=50)
            condition_tb.config(state="normal")
            for c in condition_list:
                condition_tb.insert(INSERT, str(c) + "\n")

            condition_tb.config(state=DISABLED)
            condition_tb.pack(pady=10)

            symptoms_tb = Text(subdiagnosis_frame, height=10, width=50)
            symptoms_tb.config(state="normal")
            for s in symptoms_list:
                symptoms_tb.insert(INSERT, str(s) + "\n")

            symptoms_tb.config(state=DISABLED)
            symptoms_tb.pack(pady=10)

            patient_diagnosis = [d['X'] for d in list(prolog.query("get_patientstats('" + pat_name + "',X,Y,Z)"))]
            patientadvice = [p['Y'] for p in list(prolog.query("get_patientstats('" + pat_name + "',X,Y,Z)"))]
            mohadvice = [m['Z'] for m in list(prolog.query("get_patientstats('" + pat_name + "',X,Y,Z)"))]

            Label(subdiagnosis_frame, text="Diagnosis: " + patient_diagnosis[0] + ".", justify=CENTER, bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Advice to Patient: " + patientadvice[0] + ".", justify=CENTER,
                  bg="#fff").pack(
                pady=10)
            Label(subdiagnosis_frame, text="Advice to MOH: " + mohadvice[0] + ".", justify=CENTER, bg="#fff").pack(
                pady=10)

        elif len(patient_info1) == 0 and len(patient_info2) == 0:
            messagebox.showerror("Error", "Patient does not exist.", parent=diagnosis_window)

    # Window
    diagnosis_window = Toplevel()
    diagnosis_window.title('Patient Diagnosis')
    diagnosis_window.iconbitmap('./favicon.ico')
    diagnosis_window.configure(bg="#353535")
    diagnosis_window.geometry("850x600+100+50")

    # Main Frame
    diagnosis_frame = LabelFrame(diagnosis_window, text="Condition Details", padx=40, pady=40, borderwidth=10,
                                 bg="#fff")
    diagnosis_frame.pack(fill=BOTH, expand=1)

    # Label
    backlbl = Label(diagnosis_frame, text="<--Back to Main", bg="#30D5C8")
    backlbl.bind("<Enter>", partial(configureColor, backlbl, "blue"))
    backlbl.bind("<Leave>", partial(configureColor, backlbl, "black"))
    backlbl.bind("<Button-1>", lambda e: goBack(diagnosis_window))
    backlbl.pack()

    # Canvas
    canvas = Canvas(diagnosis_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Scrollbar
    scrollbar = ttk.Scrollbar(diagnosis_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Sub Frame
    subdiagnosis_frame = Frame(canvas)

    # Sub Window
    canvas.create_window((0, 0), window=subdiagnosis_frame, anchor=NW)

    # Label
    patientlbl = Label(subdiagnosis_frame, text="Enter the patient's name ")
    patientlbl.grid(row=0, column=0)

    # Text Box
    patient_name = Entry(subdiagnosis_frame, width=30)
    patient_name.grid(row=0, column=1, columnspan=2)

    # Button
    display = Button(subdiagnosis_frame, text="Display Patient", justify=CENTER, command=retrieve_patient, bd=4)
    display.grid(row=1, column=2, padx=5, pady=9)
    display.rowconfigure(20, weight=1)
    display.columnconfigure(2, weight=1)


def configureColor(widget, color, event):
    widget.configure(foreground=color)


def goBack(frame):
    main_window.attributes("-topmost", True)
    frame.destroy()
    main_window.attributes("-topmost", False)


# Main Window
main_window = Tk()
main_window.title('MOH Expert System')
main_window.iconbitmap('./favicon.ico')
main_window.configure(bg="#353535")
main_window.resizable(False, False)
main_window.geometry("980x600+100+50")

# Frames
main_frame = LabelFrame(main_window, text="Main Window", padx=40, pady=40, borderwidth=10, bg="#fff")
main_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

info_frame = LabelFrame(main_window, text=" ", padx=40, pady=40, borderwidth=10, bg="#fff")
info_frame.grid(row=0, column=1, padx=(20, 80), pady=100)

# Buttons
Button(main_frame, text="Add Condition/Ethnicity/Location Fact", command=add_fact).grid(row=0, column=0, pady=10,
                                                                                        padx=100,
                                                                                        ipadx=26)
Button(main_frame, text="Add Patient Fact", command=add_patient, padx=85).grid(row=2, column=0, pady=10, padx=100)
Button(main_frame, text="Diagnose Patient", command=diagnose_patient, padx=52).grid(row=4, column=0, pady=10, padx=100,
                                                                                    ipadx=33)
Button(main_frame, text="Display Statistics", command=display_statistics, padx=52).grid(row=5, column=0, pady=10,
                                                                                        padx=100,
                                                                                        ipadx=33)

# Labels
Label(info_frame, text="This is an expert system developed to assist the Ministry of Health(MOH) in diagnosing the "
                       "COVID-19 virus. It will also display relevant statistics. Please select an option from the "
                       "list provided.", wraplength=150, justify=CENTER, bg="#fff").pack()

mainloop()
