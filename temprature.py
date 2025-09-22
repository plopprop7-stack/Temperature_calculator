import tkinter as tk

def convert_celsius_to_fahrenhiet():
    
    try:
        celsius = float(celsius_entry.get())
        fahrenhiet = (9 * celsius)/5 + 32
        fahrenhiet2ult_label.config(text=f"{celsius}°C is {fahrenhiet:.2f}°F")
        fahrenhiet_entry.delete(0, tk.END)  # Clear the other input field
        celsius1_entry.delete(0, tk.END)  # Clear the other input field
        kelvin_entry.delete(0, tk.END)  # Clear the other input field
        kelvinx_entry.delete(0, tk.END)  # Clear the other input field
        fahrenhiet2_entry.delete(0, tk.END)  # Clear the other input field
    except ValueError:
        fahrenhiet2ult_label.config(text="Please enter a valid number for celsius.")
def convert_fahrenhiet_to_celsius():
    
    try:
        fahrenhiet = float(fahrenhiet_entry.get())
        celsius = (fahrenhiet - 32) * 5/9
        fahrenhiet2ult_label.config(text=f"{fahrenhiet}°F fahrenhiet is {celsius:.2f} °C")
        celsius_entry.delete(0, tk.END)  # Clear the other input field
        celsius1_entry.delete(0, tk.END)  # Clear the other input field
        kelvin_entry.delete(0, tk.END)  # Clear the other input field
        kelvinx_entry.delete(0, tk.END)  # Clear the other input field
        fahrenhiet2_entry.delete(0, tk.END)  # Clear the other input field
    except ValueError:
        fahrenhiet2ult_label.config(text="Please enter a valid number for fahrenhiet.")
def convert_celsius_to_kelvin():
    
    try:
        celsius1 = float(celsius1_entry.get())
        kelvin = celsius1 + 273.15
        fahrenhiet2ult_label.config(text=f"{celsius1}°C is {kelvin:.2f} K")
        fahrenhiet_entry.delete(0, tk.END)  # Clear the other input field
        celsius_entry.delete(0, tk.END)  # Clear the other input field
        kelvin_entry.delete(0, tk.END)  # Clear the other input field
        kelvinx_entry.delete(0, tk.END)  # Clear the other input field
        fahrenhiet2_entry.delete(0, tk.END)  # Clear the other input field
    except ValueError:
        fahrenhiet2ult_label.config(text="Please enter a valid number for celsius.")
def convert_kelvin_to_celsius():
    
    try:
        kelvin = float(kelvin_entry.get())
        celsius0 = kelvin - 273.15
        fahrenhiet2ult_label.config(text=f"{kelvin} K is {celsius0:.2f}°C")
        fahrenhiet_entry.delete(0, tk.END)  # Clear the other input field
        celsius_entry.delete(0, tk.END)  # Clear the other input field
        celsius1_entry.delete(0, tk.END)  # Clear the other input field
        kelvinx_entry.delete(0, tk.END)  # Clear the other input field
        fahrenhiet2_entry.delete(0, tk.END)  # Clear the other input field
    except ValueError:
        fahrenhiet2ult_label.config(text="Please enter a valid number for kelvin.")
def convert_fahrenhiet_to_kelvin():
    
    try:
        fahrenhiet2 = float(fahrenhiet2_entry.get())
        res = (fahrenhiet2 - 32) * 5/9
        kelvin2 = res + 273.15
        fahrenhiet2ult_label.config(text=f"{fahrenhiet2}°F is {kelvin2:.2f} K")
        fahrenhiet_entry.delete(0, tk.END)  # Clear the other input field
        celsius_entry.delete(0, tk.END)  # Clear the other input field
        kelvin_entry.delete(0, tk.END)  # Clear the other input field
        kelvinx_entry.delete(0, tk.END)  # Clear the other input field
        celsius1_entry.delete(0, tk.END)  # Clear the other input field
    except ValueError:
        fahrenhiet2ult_label.config(text="Please enter a valid number for fahrenhiet.")

def convert_kelvin_to_fahrenhiet():
    
    try:
        kelvinx = float(kelvinx_entry.get())
        res1 = kelvinx - 273.15
        fahrenhietx = (9 * res1)/5 + 32
        fahrenhiet2ult_label.config(text=f"{kelvinx} K is {fahrenhietx:.2f}°F")
        fahrenhiet_entry.delete(0, tk.END)  # Clear the other input field
        celsius_entry.delete(0, tk.END)  # Clear the other input field
        kelvin_entry.delete(0, tk.END)  # Clear the other input field
        fahrenhiet2_entry.delete(0, tk.END)  # Clear the other input field
        celsius1_entry.delete(0, tk.END)  # Clear the other input field
    except ValueError:
        fahrenhiet2ult_label.config(text="Please enter a valid number for kelvin.")

# Create the main application window
app = tk.Tk()
app.title("Temprature Calculator")
app.geometry("1000x320")  # Set the window size

# Create and place a title label
title_label = tk.Label(app, text="Temprature calculator", font=("Arial", 16))
title_label.pack(pady=10)

# Frame for celsius to fahrenheit conversion
celsius_frame = tk.Frame(app)
celsius_frame.pack(pady=5)
tk.Label(celsius_frame, text="Celsius:").pack(side=tk.LEFT)
celsius_entry = tk.Entry(celsius_frame, width=15)
celsius_entry.pack(side=tk.LEFT, padx=5)
tk.Button(celsius_frame, text="Convert to Fahrenhiet", command=convert_celsius_to_fahrenhiet).pack(side=tk.LEFT)

# Frame for fahrenhiet to celsius conversion
fahrenhiet_frame = tk.Frame(app)
fahrenhiet_frame.pack(pady=5)
tk.Label(fahrenhiet_frame, text="Fahrenhiet:").pack(side=tk.LEFT)
fahrenhiet_entry = tk.Entry(fahrenhiet_frame, width=15)
fahrenhiet_entry.pack(side=tk.LEFT, padx=5)
tk.Button(fahrenhiet_frame, text="Convert to Celsius", command=convert_fahrenhiet_to_celsius).pack(side=tk.LEFT)

# Frame for celsius to kelvin conversion
celsius1_frame = tk.Frame(app)
celsius1_frame.pack(pady=5)
tk.Label(celsius1_frame, text="Celsius:").pack(side=tk.LEFT)
celsius1_entry = tk.Entry(celsius1_frame, width=15)
celsius1_entry.pack(side=tk.LEFT, padx=5)
tk.Button(celsius1_frame, text="Convert to kelvin", command=convert_celsius_to_kelvin).pack(side=tk.LEFT)

# Frame for kelvin to celsius conversion
kelvin_frame = tk.Frame(app)
kelvin_frame.pack(pady=5)
tk.Label(kelvin_frame, text="Kelvin:").pack(side=tk.LEFT)
kelvin_entry = tk.Entry(kelvin_frame, width=15)
kelvin_entry.pack(side=tk.LEFT, padx=5)
tk.Button(kelvin_frame, text="Convert to Celsius", command=convert_kelvin_to_celsius).pack(side=tk.LEFT)

# Frame for fahrenhiet to kelvin conversion
fahrenhiet2_frame = tk.Frame(app)
fahrenhiet2_frame.pack(pady=5)
tk.Label(fahrenhiet2_frame, text="Fahrenhiet:").pack(side=tk.LEFT)
fahrenhiet2_entry = tk.Entry(fahrenhiet2_frame, width=15)
fahrenhiet2_entry.pack(side=tk.LEFT, padx=5)
tk.Button(fahrenhiet2_frame, text="Convert to kelvin", command=convert_fahrenhiet_to_kelvin).pack(side=tk.LEFT)

# Frame for kelvin to fahrenhiet conversion
kelvinx_frame = tk.Frame(app)
kelvinx_frame.pack(pady=5)
tk.Label(kelvinx_frame, text="Kelvin:").pack(side=tk.LEFT)
kelvinx_entry = tk.Entry(kelvinx_frame, width=15)
kelvinx_entry.pack(side=tk.LEFT, padx=5)
tk.Button(kelvinx_frame, text="Convert to fahrenhiet", command=convert_kelvin_to_fahrenhiet).pack(side=tk.LEFT)

# Label to display the fahrenhiet2ult
fahrenhiet2ult_label = tk.Label(app, text="Enter a value and click a button.", font=("Arial", 12))
fahrenhiet2ult_label.pack(pady=10)

# Run the application
app.mainloop()

#COMPLETED