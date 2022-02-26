from tkinter import *
import tkinter.messagebox


# Commands
def add_condition():
    global conditionbtn
    global ethnicitybtn
    global conditionlbl
    global ethnicitylbl
    global conditiontb
    global ethnicitytb
    global submitbtn
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
    submitbtn = Button(condition_window, text="Submit")

    conditionbtn.grid(row=0, column=0)
    ethnicitybtn.grid(row=1, column=0)


def condition():
    conditionbtn.destroy()
    ethnicitybtn.destroy()
    conditionlbl.grid(row=0, column=0)
    conditiontb.grid(row=0, column=1)
    submitbtn.grid(row=1, column=0)


def ethnicity():
    conditionbtn.destroy()
    ethnicitybtn.destroy()
    ethnicitylbl.grid(row=0, column=0)
    ethnicitytb.grid(row=0, column=1)
    submitbtn.grid(row=1, column=0)


def add_reg():
    # # Frame
    # condition_frame = LabelFrame(condition_window, text="Condition Details", padx=40, pady=40, borderwidth=10,
    #                              bg="#fff")
    # condition_frame.grid(row=0, column=0, padx=(80, 20), pady=100)
    #
    # # Labels
    # Label(condition_window, text="Name").grid(row=0, column=0)
    # Label(condition_window, text="Age").grid(row=1, column=0)
    # Label(condition_window, text="Temperature (in Celsius)").grid(row=2, column=0)
    # Label(condition_window, text="Height (Ft)").grid(row=3, column=0)
    # Label(condition_window, text="Height (In)").grid(row=4, column=0)
    #
    # # Text Boxes
    # name = Entry(condition_window, width=30)
    # age = Entry(condition_window, width=30)
    # temp = Entry(condition_window, width=30)
    # height1 = Entry(condition_window, width=30)
    # height2 = Entry(condition_window, width=30)
    #
    # name.grid(row=0, column=1, columnspan=2)
    # age.grid(row=1, column=1, columnspan=2)
    # temp.grid(row=2, column=1, columnspan=2)
    # height1.grid(row=3, column=1, columnspan=2)
    # height2.grid(row=4, column=1, columnspan=2)
    # # Submit Button
    # # Button(condition_window, text="Submit", justify=CENTER).grid(row=4, column=0)
    return


# Main Window
main_window = Tk()
main_window.title('MOH Expert System')
main_window.iconbitmap('./favicon.ico')
main_window.configure(bg="#353535")
main_window.geometry("850x600")

# Frames
main_frame = LabelFrame(main_window, text="Main Window", padx=40, pady=40, borderwidth=10, bg="#fff")
main_frame.grid(row=0, column=0, padx=(80, 20), pady=100)

info_frame = LabelFrame(main_window, text=" ", padx=40, pady=40, borderwidth=10, bg="#fff")
info_frame.grid(row=0, column=1, padx=(20, 80), pady=100)

# Buttons
Button(main_frame, text="Add Condition Fact", command=add_condition).grid(row=0, column=0, pady=10, padx=100, ipadx=26)
Button(main_frame, text="Add Delta Variant Fact").grid(row=1, column=0, pady=10, padx=100, ipadx=20)
Button(main_frame, text="Add Regular COVID virus Fact").grid(row=2, column=0, pady=10, padx=100)
Button(main_frame, text="Add Omicron Fact").grid(row=3, column=0, pady=10, padx=100, ipadx=29)
Button(main_frame, text="Diagnose Patient").grid(row=4, column=0, pady=10, padx=100, ipadx=33)
Button(main_frame, text="Display Statistics").grid(row=5, column=0, pady=10, padx=100, ipadx=33)

# Labels
Label(info_frame, text="This is an expert system developed to assist the Ministry of Health(MOH) in diagnosing the "
                       "COVID-19 virus. It will also display relevant statistics. Please select an option from the "
                       "list provided.", wraplength=150, justify=CENTER, bg="#fff").pack()

mainloop()
