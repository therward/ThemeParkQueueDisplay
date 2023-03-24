# ThemeParkQueueDisplay
Python script to show theme park queue times onto an external display



# Resources

To make my version of the Theme Park Queue Display, i used the following items. However the script can be amended to suppot most screens.The script can also be used with any raspberry pi, however i reccomend the zero w due to its small size. Having a raspberry pi with built in wifi (W models) is also useful to reduce the amount of wires and space it uses with no need for dongles. 

 + Screen - SSD1322/ER-OLEDM032 display 
 + Reaspberry Pi Zero W
 + Wires / power supply for the raspberry pi 




# Video Demo

[![Watch demostration video here](https://img.youtube.com/vi/czwCQ_4MPFk/0.jpg)](https://www.youtube.com/watch?v=czwCQ_4MPFk)

# Upcoming Features

+ Stop displaying ride queue times when the park is shut and instead display "{park name} is now closed"
+ Give the option to display the weather on the display onces its cycled through the queue times (This will be optional)
+ Show the park opening hours to the left of the clock 
+ When disconnected from WIFI - to display a message "Device is disconnected from WIFI"
+ Implement an Energy Saving mode that stops calling the API during the night or after park opening hours
+ Add animations instead of the display blinking
+ Auto Update

Futher down the road:
 
+ Add a web interface, allowing users to customise the park shown and the type of rides (Family / thrill / area based). The interface would also allow customisation on font type / size and also allow the user to select when eco mode starts. 

# Report a bug 

If there is an bug you have spotted, please create a GitHub issue and i will try to include a fix on the next version. Please note i am unable to
release a script to support all screen versions, make sure that your bug is not due to forgetting to ammend the code to support your screen. 
