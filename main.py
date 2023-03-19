from tkinter import *
from tkinter import messagebox



# ----------------Function for calculating BMI-----------------
def calculate_bmi():
    age = int(age_tf.get())
    kg = int(weight_tf.get())
    m = int(height_tf.get()) / 100

    if age < 10 or m <= 0 or m > 3 or kg <= 0 or kg > 500:
        messagebox.showinfo('bmi - your result', "Invalid input data")

    else:
        bmi = kg / (m ** 2)
        bmi = round(bmi, 1)

    if age < 45:

        if bmi < 18.5:
            messagebox.showinfo('bmi - your result', f'BMI = {bmi} corresponds to underweight')

        elif (bmi > 18.5) and (bmi < 24.9):
            messagebox.showinfo('bmi - your result', f'BMI = {bmi} corresponds to normal weight')

        elif (bmi > 24.9) and (bmi < 29.9):
            messagebox.showinfo('bmi - your result', f'BMI = {bmi} corresponds to overweight')

        else:
            messagebox.showinfo('bmi - your result', f'BMI = {bmi} corresponds to obesity')

    else:

        if bmi < 22:
            messagebox.showinfo('bmi - your result', f'BMI = {bmi} corresponds to underweight')

        elif (bmi > 22) and (bmi < 27):
            messagebox.showinfo('bmi - your result', f'BMI = {bmi} corresponds to normal weight')

        elif (bmi > 27) and (bmi < 32):
            messagebox.showinfo('bmi - your result', f'BMI = {bmi} corresponds to overweight')

        else:
            messagebox.showinfo('bmi - your result', f'BMI = {bmi} corresponds to obesity')



# ------------------creating a dialog box-------------------
window = Tk()
window.title('Body weight calculator (BMI)')
window.geometry('400x200')

frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

age_lb = Label(frame, text="Enter your age  ")
age_lb.grid(row=2, column=1)

height_lb = Label(frame, text="Enter your height (cm)  ")
height_lb.grid(row=3, column=1)

weight_lb = Label(frame, text="Enter your weight (kg)  ")
weight_lb.grid(row=4, column=1)

age_tf = Entry(frame)
age_tf.grid(row=2, column=2, pady=5)

height_tf = Entry(frame)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(frame)
weight_tf.grid(row=4, column=2, pady=5)


# ----------------binding button presses and functions-----------------
cal_btn = Button(frame, text='Calculate BMI', command=calculate_bmi)
cal_btn.grid(row=5, column=2)


window.mainloop()


