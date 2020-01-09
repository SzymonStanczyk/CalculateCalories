def calculator(var1, var2, height, weight, age, activity):

    list = [var1, var2]

    height = int(height)
    weight = int(weight)
    age = int(age)


    if ((var1 == 1 and var2 == 0) or (var1 == 0 and var2 == 1)) and \
            (height >= 20 and height <= 250 and weight >= 15 and weight <= 200 and age >= 0 and age <= 120) in list:

        if activity == "No physical activity":
            act = 1
        elif activity == "Low physical activity":
            act = 1.2
        elif activity == "Average physical activity":
            act = 1.4
        elif activity == "High physical activity":
            act = 1.6
        elif activity == "Very high physical activity":
            act = 1.8

        simplykcal = int(24 * weight * act)

        if var1 == 1 in list:
            BMR = 9.99 * weight + 6.25 * height - 4.92*age + 5
            EAT = 270 * act
            NEAT = 400
            TEF = 0.1*(BMR + EAT + NEAT)
            kcal = BMR + EAT + NEAT + TEF
        elif var2 == 1 in list:
            BMR = 9.99 * weight + 6.25 * height - 4.92*age - 161
            EAT = 270 * act
            NEAT = 400
            TEF = 0.1*(BMR + EAT + NEAT)
            kcal = BMR + EAT + NEAT + TEF


        result.config(text="Simply calculate: "+ str(int(simplykcal)) + " kcal \n"
                           +"Accurate calculation: "+ str(int(kcal)) + " kcal", bg='#66ff66', font='Helvetica 12 bold')

    else:
        result.config(text="Something is wrong", bg='#ff4d4d', font='Helvetica 12 bold')


import tkinter as tk

HEIGHT = 400
WIDTH = 300

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frameText = tk.Frame(root, bd=5)
frameText.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')

welcome = tk.Frame(root)
welcome.place(relx=0.5, rely=0, relwidth=1, relheight=0.1, anchor='n')
welcometext = tk.Label(welcome, text="Welcome to the caloric demand calculator", fg="#666666",
                           font='Helvetica 11 bold', bg='#e0e0d1')
welcometext.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.9, anchor='n')

sex = tk.Label(frame, text="Sex:")
sex.place(relx=0, rely=0, relwidth=0.5, relheight=0.1)

var1 = tk.IntVar()
check = tk.Checkbutton(frame, text="Male", variable=var1)
check.place(relx=0.5, rely=0, relwidth=0.25, relheight=0.1)

var2 = tk.IntVar()
check = tk.Checkbutton(frame, text="Female", variable=var2)
check.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.1)

height = tk.Label(frame, text="Height [cm]:")
height.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.1)

height = tk.Entry(frame, font=('Tahoma', 12))
height.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.1)

weight = tk.Label(frame, text="Weight [kg]:")
weight.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.1)

weight = tk.Entry(frame, font=('Tahoma', 12))
weight.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.1)

age = tk.Label(frame, text="Age [years]:")
age.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.1)

age = tk.Entry(frame, font=('Tahoma', 12))
age.place(relx=0.5, rely=0.3, relwidth=0.5, relheight=0.1)

activitytext = tk.Label(frame, text="Activity:")
activitytext.place(relx=0, rely=0.4, relwidth=0.5, relheight=0.25)

activity = tk.Listbox(frame)
activity.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.25)
activity.insert(1, "No physical activity")
activity.insert(2, "Low physical activity")
activity.insert(3, "Average physical activity")
activity.insert(4, "High physical activity")
activity.insert(5, "Very high physical activity")

result = tk.Label(frame, text=" ")
result.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

button = tk.Button(frame, text="Calculate", font=('Tahoma', 10),
                       command=lambda: calculator(var1.get(), var2.get(), height.get(),
                                                  weight.get(), age.get(), activity.get(activity.curselection())))
button.place(relx=0.35, rely=0.675, relheight=0.1, relwidth=0.3)

root.mainloop()