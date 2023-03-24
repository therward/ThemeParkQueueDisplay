# Created by therward, for personal use only

import requests
import json
import time
import os
import inspect
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1322

# Set up OLED display
serial = spi(device=0, port=0, bus_speed_hz=8000000)
device = ssd1322(serial, rotate=0, width=256, height=64)

# Load font file
font_path = "%s/font/Bold.ttf"
font_size = 12
font = ImageFont.truetype("%s/font/Bold.ttf" % (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), 12)

# URL to request queue times for the theme park. Change the number in the URL to change the theme park. Please note that this won't change the titles
# here are some quick access park numbers. More can be found at https://queue-times.com/parks
# 1 - Alton Towers
# 2 - Thorpe Park 
# 3 - Chessington World of Adventures
# 4 - Disneyland Park Paris
# 5 - Disney World - Epcot 
# 6 - Disney World - Magic Kingdom 
# 7 - Disney World - Hollywood Studios
# 8 - Disney World - Animal Kingdom
# 27 - LegoLand Windsor
# 38 - Six Flags Great America
# 50 - Cedar Point
# 51 - Europa Park
# 61 - Knott's Berry Farm 
# 64 - Islands Of Adventure At Universal Orlando
# 160 - Efteling
# 273 - BlackPool Pleasure Beach 

url = "https://queue-times.com/parks/1/queue_times.json"

# Display startup screen
img = Image.new("RGB", (256, 64), "black")
draw = ImageDraw.Draw(img)
title_text = "Alton Towers Queue Display - Version 1.8"
loading_text = "NOW LOADING"
created_by_text = " Created By Thomas Herward"
title_font = ImageFont.truetype("%s/font/Bold.ttf" % (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), 14)
loading_font = ImageFont.truetype("%s/font/Bold.ttf" % (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), 12)
created_by_font = ImageFont.truetype("%s/font/Bold.ttf" % (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))), 12)
title_width, title_height = draw.textsize(title_text, font=title_font)
loading_width, loading_height = draw.textsize(loading_text, font=loading_font)
created_by_width, created_by_height = draw.textsize(created_by_text, font=loading_font)
draw.text(((256 - title_width) / 2, (64 - title_height - loading_height - created_by_height) / 2), title_text, fill="white", font=title_font)
draw.text(((256 - loading_width) / 2, (64 - title_height - loading_height - created_by_height) / 2 + title_height), loading_text, fill="white", font=loading_font)
draw.text(((256 - created_by_width) / 2, (64 - title_height - loading_height - created_by_height) / 2 + title_height + loading_height + 10), created_by_text, fill="white", font=created_by_font)
device.display(img)
time.sleep(12)

# Loop until function is closed
while True:
    # Send HTTP GET request to API
    response = requests.get(url)
    # Parse JSON response into dictionary
    data = json.loads(response.text)
    # Clear display
    device.clear()
    
    # Display list of ride names and wait times on OLED display
    ride_list = []
    for land in data['lands']:
        for ride in land['rides']:
            name = ride['name']
            is_open = ride['is_open']
            if is_open:
                wait_time = ride['wait_time']
                ride_list.append(f"{name}: {wait_time} min")
            else:
                ride_list.append(f"{name} is closed.")

    # Create an image to draw on
    img = Image.new("RGB", (256, 64), "black")
    draw = ImageDraw.Draw(img)

    # Draw the title
    draw.text((0, 0), "Alton Towers Queue Times", fill="white", font=font)

    # Draw the current time in the top-right corner
    current_time = time.strftime("%H:%M")
    time_width, time_height = draw.textsize(current_time, font=font)
    draw.text((256 - time_width, 0), current_time, fill="white", font=font)
    
    # Display the first 4 rides on the screen
    y_offset = 16
    for ride in ride_list[:4]:
        draw.text((0, y_offset), ride, fill="white", font=font)
        y_offset += 10

    # Show the first set of rides for 5 seconds
    device.display(img)
    time.sleep(5)

    # Loop through all the rides and show 4 at a time
    for i in range(4, len(ride_list), 4):
        device.clear()
        
        # Create new image
        img = Image.new("RGB", (256, 64), "black")
        
        # Draw new title
        draw = ImageDraw.Draw(img)
        
        # Draw the title
        draw.text((0, 0), "Alton Towers Queue Times", fill="white", font=font)

        # Draw the current time in the top-right corner
        current_time = time.strftime("%H:%M")
        time_width, time_height = draw.textsize(current_time, font=font)
        draw.text((256 - time_width, 0), current_time, fill="white", font=font)

        # Display the next 4 rides on the screen
        y_offset = 16
        for ride in ride_list[i:i+4]:
            draw.text((0, y_offset), ride, fill="white", font=font)
            y_offset += 10

        # Show the next set of rides for 5 seconds
        device.display(img)
        time.sleep(5) 
