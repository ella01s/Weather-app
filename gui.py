# Author: Emmanuella Solomon
# Date: 07/10/23
# Description: GUI for the weather application

import tkinter as tk
from weather_api import fetch_weather_data

# Create a main application window
root = tk.Tk()
root.title("Weather App")

# Create labels 
temperature_label = tk.Label(root, text="Temperature: ")
description_label = tk.Label(root, text="Weather Description: ")

# Place labels on the window
temperature_label.pack()
description_label.pack()

# Function to update weather data
def update_weather_data():
    # Fetch new weather data using fetch_weather_data function
    weather_data = fetch_weather_data()
    
    if weather_data:
        # Update weather labels
        temperature_label.config(text=f"Temperature: {weather_data['temperature']} K")
        description_label.config(text=f"Weather Description: {weather_data['description']}")
    else:
        # If the weather data cant be fetched
        temperature_label.config(text="Temperature: N/A")
        description_label.config(text="Weather Description: N/A")

# Update weather button
update_button = tk.Button(root, text="Update Weather", command=update_weather_data)
update_button.pack()

# Start the main event loop
root.mainloop()