import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="holiday_package"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    trip_type = package_var.get()
    packs = int(packs_entry.get())
    
    #  the price below is to defined the value from your selections
    prices = {
        "Trip A": 460,
        "Trip B": 660,
        "Trip C": 540,
  
    }
    
    # Calculate the total price. This will be derived from your selection (Package, Pack).
total_price = (prices[trip_type] * packs)
    
    # To insert your Data to your database, As for this example, you have 3 attributes. (2 Attributes from your selection (Package, Pack) and another attributes that derived from your attributes (price))
    sql = "INSERT INTO package (Package_Type, Package_Pack, Package_Price) VALUES (%s, %s, %s)"
    val = (trip_type, packs, total_price)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back The output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python. 
    output_label.config(text=f"Trip: {trip_type}, Packs: {packs}, Total Price: RM{total_price}")


# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Trip Planner")
root.geometry('600x600')


# Page Title
label = tk.Label(root, text='Calculate your Package Price', font=("Impact", "15"))
label.pack(ipadx=10, ipady=10)

# Prices List by using textbox
prices_text = tk.Text(root, height=15, width=45)
prices_text.pack(pady=20)

# The defined list by using pricebox
prices_text.insert(tk.END, "Package & Prices:\n\n")
prices_text.insert(tk.END, "Package A A: Pulau Redang 3Days, 2Night \nPrice: RM460\n\n")
prices_text.insert(tk.END, "Package B: Pulau Perhentian 4Days, 3Night \nPrice: RM660\n\n")
prices_text.insert(tk.END, "Package C: Pulau Kapas 4Days, 3Night \nPrice: RM540\n\n")
prices_text.configure(state='disabled')

# Trip Type Dropdown (Label)
packs_label = tk.Label(root, text="Choose Your Package")
packs_label.pack()

# Trip Type Dropdown
package_var = tk.StringVar(root)
package_var.set("Select Your Trip")  # Default value before your selection
trip_dropdown = tk.OptionMenu(root, package_var, "Trip A", "Trip B", "Trip C")
trip_dropdown.pack(pady=10)


# Packs Entry. Label and user can insert data thru entry
packs_label = tk.Label(root, text="Packs:")
packs_label.pack()
packs_entry = tk.Entry(root)
packs_entry.pack()

# Save Button
save_button = tk.Button(root, text="Calculate", command=collect_data)
save_button.pack(pady=10)

# Output Label & result
label = tk.Label(root, text='Price Package', font=("Times New Romans",12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
