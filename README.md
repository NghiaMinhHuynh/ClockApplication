CLOCK APPLICATION

This Python-based application provides a Real-Time Clock and Countdown Timer with a user-friendly graphical user interface (GUI). It's built using the Tkinter library for the GUI and incorporates various functionalities for timekeeping and countdown timing.

Features

1. Page Navigation
Page 1 (HOME): Serves as the main menu, allowing users to navigate between the Clock, Digital Clock, and Timer functionalities.

2. Real-Time Clock
Page 2 (Clock): This page displays an analog clock with hour, minute, and second hands. The clock updates in real-time, showing the current time.

3. Digital Clock
Page 3 (Digital Clock): Displays the current time in a digital format (HH:MM:SS AM/PM) that updates in real-time.

4. Countdown Timer
Page 4 (Timer): Users can set and control a countdown timer using hours, minutes, and seconds input fields. The remaining time is displayed, and users can perform the following actions:
Start Countdown: Begin the countdown timer.
Stop Countdown: Pause the countdown timer.
Resume Countdown: Continue a paused countdown timer.
Reset Countdown: Reset the countdown timer.


Getting Started
To run this application, follow these steps:

Ensure you have Python installed on your system.

Install the required libraries (Tkinter should be included with Python):

Copy code
pip install pillow

Download the source code and any required assets (e.g., clock background image).

Run the application:
Copy code
python your_file_name.py


Usage

Launch the application, and you'll start on the main menu (Page 1 - HOME).
Click on "Clock" to view the analog clock (Page 2).
Click on "Digital Clock" to view the digital clock (Page 3).
Click on "Timer" to access the countdown timer (Page 4).


Clock Functionality

The analog clock (Page 2) displays the current time with hour, minute, and second hands.
The clock updates in real-time.


Digital Clock Functionality

The digital clock (Page 3) displays the current time in HH:MM:SS AM/PM format.
The time updates in real-time.


Countdown Timer Functionality

Access the countdown timer (Page 4) from the main menu.
Enter the desired countdown time in hours, minutes, and seconds using the input fields.
Click "Start Countdown" to initiate the timer.
You can pause the timer using "Stop Countdown."
To resume a paused timer, click "Resume Countdown."
Click "Reset Countdown" to clear the timer settings.

Dependencies
Python (3.x recommended)
Tkinter (usually included with Python)
Pillow (PIL) library for handling images

Credits
This application was created by Nghia Minh Huynh.

License
This project is licensed under the MIT License
