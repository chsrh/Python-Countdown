# import the time module
import time

# define the countdown function
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Fire in the hole!')

# input time in seconds
t = input("Enter the time (s): ")

# function call
countdown(int(t))
