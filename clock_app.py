import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
import time
import math

class Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

    def show(self):
        self.controller.show_page(self)

class Page1(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        label = tk.Label(self, text="HOME")
        label.pack(pady=10, padx=10)
        
        clock_button = ttk.Button(self, text="Clock", command=lambda: controller.show_page(Page2))
        clock_button.pack()
        clock_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER) 
        dclock_button = ttk.Button(self, text="Digital Clock", command=lambda: controller.show_page(Page3))
        dclock_button.pack()
        dclock_button.place(relx=0.5, rely=0.45, anchor=tk.CENTER) 
        timer_button = ttk.Button(self, text="Timer", command=lambda: controller.show_page(Page4))
        timer_button.pack()
        timer_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 
        
class Page2(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_page(Page1))
        back_button.pack(side="bottom", pady=5) 
        back_button.pack()
       
        
    # Create a canvas for the clock
        self.canvas = tk.Canvas(self, width=400, height=400, bg="black")
        self.canvas.pack()
        
        # Load the clock background image
        bg = tk.PhotoImage(file='dial_400 (1).png')
        self.canvas.create_image(200, 200, image=bg)
        self.bg = bg
        
        # Create clock hands
        self.center_x = 200
        self.center_y = 200
        self.seconds_hand_len = 95
        self.minutes_hand_len = 80
        self.hours_hand_len = 60
        
        self.seconds_hand = self.canvas.create_line(
            self.center_x, self.center_y, 
            self.center_x, self.center_y, 
            width=1.5, fill='red'
        )
        
        self.minutes_hand = self.canvas.create_line(
            self.center_x, self.center_y, 
            self.center_x, self.center_y, 
            width=2, fill='white'
        )
        
        self.hours_hand = self.canvas.create_line(
            self.center_x, self.center_y, 
            self.center_x, self.center_y, 
            width=4, fill='white'
        )
        
        # Update the clock
        self.update_clock()
    
    def update_clock(self):
        hours = int(time.strftime("%I"))
        minutes = int(time.strftime("%M"))
        seconds = int(time.strftime("%S"))

        # Updating seconds hand
        seconds_x = self.seconds_hand_len * math.sin(math.radians(seconds * 6)) + self.center_x
        seconds_y = -1 * self.seconds_hand_len * math.cos(math.radians(seconds * 6)) + self.center_y
        self.canvas.coords(self.seconds_hand, self.center_x, self.center_y, seconds_x, seconds_y)

        # Updating minutes hand
        minutes_x = self.minutes_hand_len * math.sin(math.radians(minutes * 6)) + self.center_x
        minutes_y = -1 * self.minutes_hand_len * math.cos(math.radians(minutes * 6)) + self.center_y
        self.canvas.coords(self.minutes_hand, self.center_x, self.center_y, minutes_x, minutes_y)

        # Updating hours hand
        hours_x = self.hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + self.center_x
        hours_y = -1 * self.hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + self.center_y
        self.canvas.coords(self.hours_hand, self.center_x, self.center_y, hours_x, hours_y)

        self.after(1000, self.update_clock)
    
        

class Page3(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_page(Page1))
        back_button.pack(side="bottom", pady=5) 
        back_button.pack()
        
        clock_label = tk.Label(self, text="00:00:00", font="Helvetica 72 bold")
        clock_label.pack()
        clock_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER) 

        def update_clock():
            hours = time.strftime("%I")
            minutes = time.strftime("%M")
            seconds = time.strftime("%S")
            am_or_pm = time.strftime("%p")
            time_show = hours + ":" + minutes + ":" + seconds + am_or_pm
            clock_label.config(text=time_show)
            clock_label.after(1000, update_clock)

        update_clock()

# Global variables
end_time = None
paused = False

class Page4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        # Label for countdown display
        self.countdown_label = tk.Label(self, text="00:00:00", font=("Helvetica", 36))
        self.countdown_label.pack(pady=20)
        back_button = ttk.Button(self, text="Back", command=lambda: controller.show_page(Page1))
        back_button.pack(side="bottom", pady=5) 
        back_button.pack()
        
        # Entry fields for setting the countdown time
        self.hours_label = tk.Label(self, text="Hours:")
        self.hours_label.pack()
        self.hours_entry = tk.Entry(self)
        self.hours_entry.pack()
        
        self.minutes_label = tk.Label(self, text="Minutes:")
        self.minutes_label.pack()
        self.minutes_entry = tk.Entry(self)
        self.minutes_entry.pack()
        
        self.seconds_label = tk.Label(self, text="Seconds:")
        self.seconds_label.pack()
        self.seconds_entry = tk.Entry(self)
        self.seconds_entry.pack()
        
        # Buttons for control
        self.start_button = tk.Button(self, text="Start Countdown", command=self.start_countdown)
        self.start_button.pack()
        self.stop_button = tk.Button(self, text="Stop Countdown", command=self.stop_countdown)
        self.stop_button.pack()
        self.resume_button = tk.Button(self, text="Resume Countdown", command=self.resume_countdown)
        self.resume_button.pack()
        self.reset_button = tk.Button(self, text="Reset Countdown", command=self.reset_countdown)
        self.reset_button.pack()

    # Function to update the countdown label
    def update_countdown(self):
        global end_time
        global paused
        
        if not paused:
            remaining_time = end_time - datetime.now()
            if remaining_time.total_seconds() <= 0:
                self.countdown_label.config(text="Time's up!")
                messagebox.showinfo("Countdown Timer", "Time's up!")
            else:
                self.countdown_label.config(text=str(remaining_time).split(".")[0])
                self.after(1000, self.update_countdown)  # Update every 1000 milliseconds (1 second)

    # Function to start the countdown
    def start_countdown(self):
        global end_time
        global paused
        
        hours = int(self.hours_entry.get() or 0)
        minutes = int(self.minutes_entry.get() or 0)
        seconds = int(self.seconds_entry.get() or 0)  # Default to 0 if no input
        end_time = datetime.now() + timedelta(hours=hours, minutes=minutes, seconds=seconds)
        paused = False
        self.update_countdown()

    # Function to stop the countdown
    def stop_countdown(self):
        global paused
        paused = True

    # Function to resume the countdown
    def resume_countdown(self):
        global paused
        paused = False
        self.update_countdown()

    # Function to reset the countdown
    def reset_countdown(self):
        global end_time
        global paused
        end_time = None
        paused = False
        self.countdown_label.config(text="")

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Three Page App")
        self.geometry("550x450")

        # Create a frame to hold the pages
        self.page_container = tk.Frame(self)
        self.page_container.pack(fill="both", expand=True)

        # Create the pages
        page1 = Page1(self.page_container, self)
        page2 = Page2(self.page_container, self)
        page3 = Page3(self.page_container, self)
        page4 = Page4(self.page_container, self)

        self.pages = {
            Page1: page1,
            Page2: page2,
            Page3: page3,
            Page4: page4
        }

        self.show_page(Page1)

    def show_page(self, page_class):
        # Hide all pages
        for page in self.pages.values():
            page.pack_forget()

        # Show the selected page
        page = self.pages.get(page_class)
        if page:
            page.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
