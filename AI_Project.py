from tkinter import *
from pyswip import Prolog

# Prolog
prolog = Prolog()

prolog.consult("AI_Project.pl")


# Commands
def add_condition():
    global condition_window
    global conditionbtn
    global ethnicitybtn
    global conditionlbl
    global ethnicitylbl
    global conditiontb
    global ethnicitytb
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


def condition():
    conditionbtn.destroy()
    ethnicitybtn.destroy()
    conditionlbl.grid(row=0, column=0)
    conditiontb.grid(row=0, column=1)
    csubmitbtn = Button(condition_window, text="Submit", command=sendCToDatabase)
    csubmitbtn.grid(row=1, column=0)


def ethnicity():
    conditionbtn.destroy()
    ethnicitybtn.destroy()
    ethnicitylbl.grid(row=0, column=0)
    ethnicitytb.grid(row=0, column=1)
    esubmitbtn = Button(condition_window, text="Submit", command=sendEToDatabase)
    esubmitbtn.grid(row=1, column=0)


def sendCToDatabase():
    cond = conditiontb.get()
    if cond[0].isupper():
        prolog.assertz("underlying_condition('" + cond + "')")
    else:
        prolog.assertz("underlying_condition("+cond+")")

    c = list(prolog.query("underlying_condition(X)"))

    print(c)


def sendEToDatabase():
    eth = ethnicitytb.get()
    if eth[0].isupper():
        prolog.assertz("ethnicity('" + eth + "')")
    else:
        prolog.assertz("ethnicity(" + eth + ")")

    c = list(prolog.query("ethnicity(X)"))

    print(c)


def add_reg():
    # Window
    reg_window = Toplevel()
    reg_window.title('Add Regular Covid Virus Fact')
    reg_window.iconbitmap('./favicon.ico')
    reg_window.configure(bg="#353535")
    reg_window.geometry("850x600")

    # Frame
    reg_frame = LabelFrame(reg_window, text="Condition Details", padx=40, pady=40, borderwidth=10,
                           bg="#fff")
    reg_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

    # Labels
    Label(reg_frame, text="Name").grid(row=0, column=0)
    Label(reg_frame, text="Age").grid(row=1, column=0)
    Label(reg_frame, text="Temperature (in Celsius)").grid(row=2, column=0)
    Label(reg_frame, text="Height (Ft)").grid(row=3, column=0)
    Label(reg_frame, text="Height (In)").grid(row=4, column=0)
    Label(reg_frame, text="Ethnicity").grid(row=5, column=0)
    Label(reg_frame, text="Gender").grid(row=6, column=0)
    Label(reg_frame, text="Experienced dizziness, fainting or blurry vision?").grid(row=7, column=0)
    Label(reg_frame, text="Weight").grid(row=8, column=0)

    # Text Boxes
    name = Entry(reg_frame, width=30)
    age = Entry(reg_frame, width=30)
    temp = Entry(reg_frame, width=30)
    height1 = Entry(reg_frame, width=30)
    height2 = Entry(reg_frame, width=30)
    weight = Entry(reg_frame, width=30)

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
    ethnicities = OptionMenu(reg_frame, selected, *ETHNICITY)
    ethnicities.grid(row=5, column=1, columnspan=2)

    # Radio Button
    gender = StringVar()
    gender.set("Male")
    Radiobutton(reg_frame, text="Male", variable=gender, value="male").grid(row=6, column=1)
    Radiobutton(reg_frame, text="Female", variable=gender, value="female").grid(row=6, column=2)

    ans = StringVar()
    ans.set("no")
    Radiobutton(reg_frame, text="Yes", variable=ans, value="yes", command=lambda: display_pressure(reg_frame, ans.get())
                ).grid(row=7, column=1)
    Radiobutton(reg_frame, text="No", variable=ans, value="no", command=lambda: remove_pressure(ans.get())).grid(
        row=7, column=2)

    # Submit Button
    # Button(reg_frame, text="Submit", justify=CENTER).grid(row=, column=0)


def display_pressure(frame, val):
    global syslbl
    global dialbl
    global systolic
    global diastolic

    syslbl = Label(frame, text="Systolic Pressure")
    dialbl = Label(frame, text="Diastolic Pressure")
    systolic = Entry(frame, width=30)
    diastolic = Entry(frame, width=30)
    if val == "yes":
        syslbl.grid(row=9, column=0)
        dialbl.grid(row=10, column=0)
        systolic.grid(row=9, column=1, columnspan=2)
        diastolic.grid(row=10, column=1, columnspan=2)


def remove_pressure(val):
    if val == "no":
        syslbl.destroy()
        dialbl.destroy()
        systolic.destroy()
        diastolic.destroy()


def add_delta():
    # Window
    delta_window = Toplevel()
    delta_window.title('Add Delta Variant Fact')
    delta_window.iconbitmap('./favicon.ico')
    delta_window.configure(bg="#353535")
    delta_window.geometry("850x600")

    # Frame
    delta_frame = LabelFrame(delta_window, text="Condition Details", padx=40, pady=40, borderwidth=10,
                             bg="#fff")
    delta_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

    # Labels
    Label(delta_frame, text="Name").grid(row=0, column=0)
    Label(delta_frame, text="Age").grid(row=1, column=0)
    Label(delta_frame, text="Temperature (in Celsius)").grid(row=2, column=0)
    Label(delta_frame, text="Height (Ft)").grid(row=3, column=0)
    Label(delta_frame, text="Height (In)").grid(row=4, column=0)
    Label(delta_frame, text="Ethnicity").grid(row=5, column=0)
    Label(delta_frame, text="Gender").grid(row=6, column=0)
    Label(delta_frame, text="Experienced dizziness, fainting or blurry vision?").grid(row=7, column=0)
    Label(delta_frame, text="Weight").grid(row=8, column=0)

    # Text Boxes
    name = Entry(delta_frame, width=30)
    age = Entry(delta_frame, width=30)
    temp = Entry(delta_frame, width=30)
    height1 = Entry(delta_frame, width=30)
    height2 = Entry(delta_frame, width=30)
    weight = Entry(delta_frame, width=30)

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
    ethnicities = OptionMenu(delta_frame, selected, *ETHNICITY)
    ethnicities.grid(row=5, column=1, columnspan=2)

    # Radio Button
    gender = StringVar()
    gender.set("Male")
    Radiobutton(delta_frame, text="Male", variable=gender, value="male").grid(row=6, column=1)
    Radiobutton(delta_frame, text="Female", variable=gender, value="female").grid(row=6, column=2)

    ans = StringVar()
    ans.set("no")
    Radiobutton(delta_frame, text="Yes", variable=ans, value="yes", command=lambda: display_pressure(delta_frame,
                                                                                                     ans.get())
                ).grid(row=7, column=1)
    Radiobutton(delta_frame, text="No", variable=ans, value="no", command=lambda: remove_pressure(ans.get())).grid(
        row=7, column=2)

    # Submit Button
    # Button(delta_frame, text="Submit", justify=CENTER).grid(row=, column=0)


def add_omicron():
    # Window
    omicron_window = Toplevel()
    omicron_window.title('Add Omicron Variant Fact')
    omicron_window.iconbitmap('./favicon.ico')
    omicron_window.configure(bg="#353535")
    omicron_window.geometry("850x600")

    # Frame
    omicron_frame = LabelFrame(omicron_window, text="Condition Details", padx=40, pady=40, borderwidth=10,
                               bg="#fff")
    omicron_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

    # Labels
    Label(omicron_frame, text="Name").grid(row=0, column=0)
    Label(omicron_frame, text="Age").grid(row=1, column=0)
    Label(omicron_frame, text="Temperature (in Celsius)").grid(row=2, column=0)
    Label(omicron_frame, text="Height (Ft)").grid(row=3, column=0)
    Label(omicron_frame, text="Height (In)").grid(row=4, column=0)
    Label(omicron_frame, text="Underlying condition").grid(row=5, column=0)
    Label(omicron_frame, text="Ethnicity").grid(row=6, column=0)
    Label(omicron_frame, text="Gender").grid(row=7, column=0)
    Label(omicron_frame, text="Experienced dizziness, fainting or blurry vision?").grid(row=8, column=0)
    Label(omicron_frame, text="Weight").grid(row=9, column=0)

    # Text Boxes
    name = Entry(omicron_frame, width=30)
    age = Entry(omicron_frame, width=30)
    temp = Entry(omicron_frame, width=30)
    height1 = Entry(omicron_frame, width=30)
    height2 = Entry(omicron_frame, width=30)
    weight = Entry(omicron_frame, width=30)

    name.grid(row=0, column=1, columnspan=2)
    age.grid(row=1, column=1, columnspan=2)
    temp.grid(row=2, column=1, columnspan=2)
    height1.grid(row=3, column=1, columnspan=2)
    height2.grid(row=4, column=1, columnspan=2)
    weight.grid(row=9, column=1, columnspan=2)

    # Dropdown List
    clicked = StringVar()
    CONDITIONS = [c['X'] for c in list(prolog.query("underlying_condition(X)"))]
    clicked.set(CONDITIONS[0])
    underlying = OptionMenu(omicron_frame, clicked, *CONDITIONS)
    underlying.grid(row=5, column=1, columnspan=2)

    selected = StringVar()
    ETHNICITY = [e['X'] for e in list(prolog.query("ethnicity(X)"))]
    selected.set(ETHNICITY[0])
    ethnicities = OptionMenu(omicron_frame, selected, *ETHNICITY)
    ethnicities.grid(row=6, column=1, columnspan=2)

    # Radio Button
    gender = StringVar()
    gender.set("Male")
    Radiobutton(omicron_frame, text="Male", variable=gender, value="male").grid(row=6, column=1)
    Radiobutton(omicron_frame, text="Female", variable=gender, value="female").grid(row=6, column=2)

    ans = StringVar()
    ans.set("no")
    Radiobutton(omicron_frame, text="Yes", variable=ans, value="yes", command=lambda: display_pressure(omicron_frame,
                                                                                                       ans.get())
                ).grid(row=7, column=1)
    Radiobutton(omicron_frame, text="No", variable=ans, value="no", command=lambda: remove_pressure(ans.get())).grid(
        row=7, column=2)

    # Submit Button
    # Button(omicron_frame, text="Submit", justify=CENTER).grid(row=, column=0)


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
Button(main_frame, text="Add Condition/Ethnicity Fact", command=add_condition).grid(row=0, column=0, pady=10, padx=100,
                                                                                    ipadx=26)
Button(main_frame, text="Add Delta Variant Fact", command=add_delta).grid(row=1, column=0, pady=10, padx=100, ipadx=20)
Button(main_frame, text="Add Regular COVID Virus Fact", command=add_reg).grid(row=2, column=0, pady=10, padx=100)
Button(main_frame, text="Add Omicron Variant Fact", command=add_omicron).grid(row=3, column=0, pady=10, padx=100,
                                                                              ipadx=29)
Button(main_frame, text="Diagnose Patient").grid(row=4, column=0, pady=10, padx=100, ipadx=33)
Button(main_frame, text="Display Statistics").grid(row=5, column=0, pady=10, padx=100, ipadx=33)

# Labels
Label(info_frame, text="This is an expert system developed to assist the Ministry of Health(MOH) in diagnosing the "
                       "COVID-19 virus. It will also display relevant statistics. Please select an option from the "
                       "list provided.", wraplength=150, justify=CENTER, bg="#fff").pack()

mainloop()
