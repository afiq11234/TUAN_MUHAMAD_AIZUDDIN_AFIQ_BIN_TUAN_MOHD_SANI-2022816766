#python
import tkinter as tk
from datetime import datetime
import random

def save():
    #user info
    name = name_entry.get()
    gender = gender_entry.get()
    date = dob_entry.get()

#create star
def create_star(canvas):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    size = random.randint(1, 3)
    canvas.create_oval(x, y, x+size, y+size, fill="white")

def twinkling_stars():
    root.title("Zodiac Sign Personality Determination")
    root.geometry("1280x1830")

root = tk.Tk()

# Placing the canvas to cover the whole window
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Labels for input fields
name_label=tk.Label(root ,text="ZODIAC SIGN", font=("castellar", 50), bg=("gold"))
name_label.pack()

name_label = tk.Label(root, text="Name:",font=('slab serif', 25), bg=("blue"))
name_label.pack(padx=10, pady=12)
name_entry = tk.Entry(root)
name_entry.pack(padx=5, pady=6)

gender_label = tk.Label(root, text="Gender:", font=('slab serif', 25), bg=("blue"))
gender_label.pack(padx=20, pady=22)
gender_entry = tk.Entry(root)
gender_entry.pack(padx=5, pady=6)

dob_label = tk.Label(root, text="Date of Birth (YYYY-MM-DD):", font=('slab serif', 25), bg=("blue"))
dob_label.pack(padx=26, pady=28)
dob_entry = tk.Entry(root)
dob_entry.pack(padx=5, pady=6)

for _ in range(100):
    create_star(canvas)

twinkling_stars()

# Function to calculate zodiac sign based on date of birth
def calculate_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
       return ("Wrong date")

# Function to determine personality based on zodiac sign
def determine_personality(zodiac_sign):
    if zodiac_sign == "Aries":
        return "brave, willful, enterprising humanitarism, productive, Confident and determined"
    elif zodiac_sign == "Taurus":
        return "practical, recourseful, energetic, tidy, confident, Patient and reliable"
    elif zodiac_sign == "Gemini":
        return "You are skillful, humorous, seductive, imaginative, curious, adaptable, and sociable."
    elif zodiac_sign == "Cancer":
        return "You are intelligent, crafty, strong_will, intuitive, emotional, and compassionate."
    elif zodiac_sign == "Leo":
        return "You are dominant, courageous, confident, ambitious, aristrocratic, idealistic and generous."
    elif zodiac_sign == "Virgo":
        return "You are efficient, calm, adaptable, altruistic, analytical, practical, and modest."
    elif zodiac_sign == "Libra":
        return "You are fair, wise, helpful, friendly and cooperative."
    elif zodiac_sign == "Scorpio":
        return "You are emotional, passionate, determined, and resourceful."
    elif zodiac_sign == "Sagittarius":
        return "You are fair-minded, funny, intellectual, adventurous, optimistic, and independent."
    elif zodiac_sign == "Capricorn":
        return "You are perservering, stoic, serious, responsible, disciplined, and ambitious."
    elif zodiac_sign == "Aquarius":
        return "You are generous, trustworthy, logical, independent, intellectual, and humanitarian."
    elif zodiac_sign == "Pisces":
        return "You are sensible, easy-going warm-hearted, compassionate, artistic, and intuitive."
    else:
        return ("Invalid zodiac sign.")

# Function to calculate age in years, months, and days
def calculate_age(dob):
    today = datetime.today()
    dob_entry = datetime.strptime(dob, '%Y-%m-%d')

    # Calculate age in years
    age_years = today.year - dob_entry.year
    if today.month < dob_entry.month or (today.month == dob_entry.month and today.day < dob_entry.day):
        age_years -= 1

    # Calculate age in months and days
    dob_month_day = datetime(today.year, dob_entry.month, dob_entry.day)
    if today < dob_month_day:
        age_months = today.month + 12 - dob_entry.month
    else:
        age_months = today.month - dob_entry.month

    age_days = (today - dob_month_day).days

    return f"Your age is: {age_years} years, {age_months} months, and {age_days} days"

def calculate_zodiac_and_personality():
    dob = dob_entry.get()
    dob_date = datetime.strptime(dob, "%Y-%m-%d")
    zodiac_sign = calculate_zodiac_sign(dob_date.day, dob_date.month)
    personality = determine_personality(zodiac_sign)
    age_result = calculate_age(dob)
    result_label.config(text=f"Zodiac Sign: {zodiac_sign}\nPersonality: {personality}\n{age_result}")

 # Display result in the terminal
    print(f"Name: {name_entry.get()}")
    print(f"Gender: {gender_entry.get()}")
    print(f"Zodiac Sign: {zodiac_sign}")
    print(f"Personality: {personality}")
    print(age_result)
    print("\n")

# Create a button to calculate zodiac sign and personality
calculate_button = tk.Button(root, text="Calculate", command=calculate_zodiac_and_personality)
calculate_button.pack()

save_button = tk.Button(root, text="save", command=save)
save_button.pack()

# Display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Function to clear all input fields
def clear_fields():
    name_entry.delete(0, 'end')
    gender_entry.delete(0, 'end')
    dob_entry.delete(0, 'end')
    result_label.config(text="")

# Create a button to clear input fields
clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack()

# Run the tkinter main loop
root.mainloop()
