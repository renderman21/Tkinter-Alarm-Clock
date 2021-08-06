from tkinter import *
import time
from datetime import *

class Clock(object):

	def gui(self):

		#Initiate clock
		self.clock = Tk()
		self.clock.wm_title("Alarm Clock")
		self.clock.geometry("500x500")
		self.title_text = Label(self.clock,text = "Alarm Clock", fg = "black", font = 50)
		self.title_text.place(x=200, y=0)

		#Icon 
		self.icon = PhotoImage(file='images/clock.png')
		self.clock.iconphoto(False,self.icon)

		#Set variables
		self.Hours = IntVar()
		self.Minutes = IntVar()
		self.Seconds = IntVar()
		self.Expected_time = StringVar()
		self.Timer = StringVar()

		#Input of time
		self.set_time_hour = Entry(self.clock, textvariable=self.Hours)
		self.set_time_hour.place(x= 50, y= 100, height =  50, width = 50)
		self.set_time_minute = Entry(self.clock, textvariable=self.Minutes)
		self.set_time_minute.place(x= 200, y =100, height= 50, width = 50)
		self.set_time_sec = Entry(self.clock,textvariable=self.Seconds)
		self.set_time_sec.place(x=350,y=100, height=50, width = 50)

		#Display the time and the expected time to alarm
		self.show_countdown = Entry(self.clock, textvariable=self.Timer,width = 10)
		self.show_countdown.place (x=200, y = 330, height = 30) 
		self.show_expected_time = Entry(self.clock, textvariable=self.Expected_time, width = 10)
		self.show_expected_time.place (x=200, y= 400, height = 30)

		#Display text
		self.countdown_text = Label(self.clock, text='Time Remaining')
		self.countdown_text.place(x =200, y = 310)
		self.expected_time_text = Label(self.clock, text = 'Time to alarm')
		self.expected_time_text.place(x=200, y=380)
		self.hours_text = Label(self.clock, text='Hours')
		self.hours_text.place(x=50,y=80) 
		self.minutes_text = Label(self.clock, text='Minutes')
		self.minutes_text.place(x=200,y=80)
		self.seconds_text = Label(self.clock, text='Seconds')
		self.seconds_text.place(x=350,y=80)

		#Buttons
		self.start_timer = Button(self.clock, text='Start Timer', command = self.retrieved_time, width =10)
		self.start_timer.place(x=200, y = 200)
		self.stop_timer = Button(self.clock, text='Stop Timer', command= self.reset, width =10)
		self.stop_timer.place(x = 200, y =250)

		#Main loop
		self.clock.update()
		self.clock.mainloop()

	def retrieved_time(self):
		try:
			#Get time 
			self.set_hour = self.Hours.get()
			self.set_minute = self.Minutes.get()
			self.set_second = self.Seconds.get()

			#Checks if the input are zero
			if self.set_hour or self.set_minute or self.set_second > 0:
				#Disable button
				self.start_timer.config(state='disabled')
				
				self.time_computation(self.set_hour, self.set_minute, self.set_second)

		except Exception:
			#When user input wrong variables
			self.error_window = Toplevel()
			self.error_window.wm_title('Error')
			self.error_window.geometry('250x150')
			self.error_icon = PhotoImage(file='images/error.png')
			self.error_window.iconphoto(False, self.error_icon)

			self.error_window.grab_set()

			self.error_message = Label(self.error_window, text = 'Please put numbers',font = 40)
			self.error_message.place(x = 40, y =0)

			self.close_button = Button(self.error_window, text='Close', command = self.error_window.destroy,width=20)
			self.close_button.place(x=30, y = 80)
	
	def time_computation (self,set_hour, set_minute, set_second):

		# Getting current time and calculate expected time
		self.current_time = datetime.now()
		self.set_timer = timedelta(hours=self.set_hour,minutes=self.set_minute,seconds=self.set_second)
		self.added_time = self.current_time + self.set_timer
		self.expected_time_alarm = self.added_time.strftime('%H:%M:%S')
		self.Expected_time.set(self.expected_time_alarm)

		self.countdown()


	def countdown(self):

		#Decrease countdown
		self.set_timer -= timedelta(seconds=1)
		self.counter = self.clock.after(1000,self.countdown)
		self.Timer.set(self.set_timer)
		
		#Condition if the timer is met with 0
		if self.set_timer == timedelta(hours=0,minutes=0,seconds=0):
			self.reset()
			self.pop_up()

	def reset(self):
		#Stops the countdown
		self.clock.after_cancel(self.counter)

		#Reset variables
		self.Hours.set(0)
		self.Minutes.set(0)
		self.Seconds.set(0)
		self.Timer.set('')
		self.Expected_time.set('')

		#Reset button state
		self.start_timer.config(state="normal")

	def pop_up(self):
		#New window
		self.alarm_window = Toplevel()
		self.alarm_window.wm_title('Alarm')
		self.alarm_window.geometry('250x150')

		#Disable interaction of the lower window
		self.alarm_window.grab_set()


		self.icon_alarm = PhotoImage(file='images/clock.png')
		self.alarm_window.iconphoto(False,self.icon_alarm)

		self.words = Label(self.alarm_window, text = 'Times up!',font = 40)
		self.words.place(x = 85, y =0)

		self.close_button = Button(self.alarm_window, text='Close', command = self.alarm_window.destroy,width=20)
		self.close_button.place(x=30, y = 80)


if __name__ == "__main__": 
	start = Clock()
	start.gui()