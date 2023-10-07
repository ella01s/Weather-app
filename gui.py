# Author: Emmanuella Solomon
# Date: 07/10/23
# Description: GUI for the weather application

import tkinter as tk
from weather_api import fetch_weather_data

# Create a main application window
root = tk.Tk()
root.title("Weather App")

#load image
weather_image = tk.PhotoImage(file='images/overcast.png')

# Define a dictionary to map weather descriptions to image file paths
weather_image_mapping = {
    "light rain": 'images/light_rain.png',
    "moderate rain": 'images/moderate_rain.png',
    "broken clouds": 'images/broken_clouds.png',
    "clear sky": 'images/clear_sky.png',
    "scattered clouds": 'images/scattered_clouds.png',
    "few clouds": 'images/few_clouds.png',
    "heavy intensity rain": 'images/heavy_rain.png',
    "overcast clouds" : 'images/overcast.png'
}

# Create labels 
temperature_label = tk.Label(root, text="Temperature: ")
description_label = tk.Label(root, text="Weather Description: ")
image_label = tk.Label(root, image = weather_image)


# Place labels on the window
temperature_label.pack()
description_label.pack()
image_label.pack()

# Define a dictionary to map weather descriptions to image file paths
weather_image_mapping = {
    "Light rain": 'images/light_rain.png',
    "Moderate rain": 'images/moderate_rain.png',
    "Broken clouds": 'images/broken_clouds.png',
    "Clear sky": 'images/clear_sky.png',
    "Scattered clouds": 'images/scattered_clouds.png',
    "Few clouds": 'images/few_clouds.png',
    "Heavy intensity rain": 'images/heavy_rain.png',
    "overcast clouds" : 'images/overcast.png',
}

def update_weather_data():
    # Fetch new weather data using fetch_weather_data function
    weather_data = fetch_weather_data()
    
    if weather_data:
        # Update weather labels
        temperature_label.config(text=f"Temperature: {weather_data['temperature']} K")
        
        # Check the weather description
        weather_description = weather_data['description']
        
        # Update the description label
        description_label.config(text=f"Weather Description: {weather_description}")
        
        # Use the dictionary to get the corresponding image path, or a default path if not found
        image_path = weather_image_mapping.get(weather_description, 'images/default_image.png')
        
        # Create the PhotoImage object
        weather_image = tk.PhotoImage(file=image_path)
        
        # Update the image in the GUI
        image_label.config(image=weather_image)
        image_label.photo = weather_image  # This line is necessary to prevent garbage collection
        
    else:
        # If the weather data can't be fetched
        temperature_label.config(text="Temperature: N/A")
        description_label.config(text="Weather Description: N/A")


# Update weather button
update_button = tk.Button(root, text="Update Weather", command=update_weather_data)
update_button.pack()

# Start the main event loop
root.mainloop()