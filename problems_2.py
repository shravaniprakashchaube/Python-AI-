"""
s = 'anup patil'
#print(s[::-1])
for i in range(-1, -len(s)-1, -1):
    print(s[i],end='')
----------------------------
s = 'anup patil'
# reverse the words present in the string
words = s.split()
#print(words) # list
#print([word[::-1] for word in words])
rev = [word[::-1] for word in words]
print(' '.join(rev))
----------------------------
p = ['sachin','tendulkar']
# convert list[str] to string
print('--'.join(p))
-------------------------
s = 'sachin tendulkar' #{'s': 1, 'a': 2, 'c': 1, 'h': 1, 'i': 1, 'n': 2, ' ': 1, 't': 1, 'e': 1, 'd': 1, 'u': 1, 'l': 1, 'k': 1, 'r': 1}}
frequency = {}
for i in s:
  if i in frequency:
    frequency[i] += 1
  else:
    frequency[i] = 1
print(frequency)
---------------------------------------------
text = "sachin tendulkar"

char_count = {ch: text.count(ch) for ch in text}

print(char_count)
------------------------------------------
text = "sachin tendulkar"
#print(text.count('a'))
char_count = {ch: text.count(ch) for ch in text}

print(char_count)
----------------------------------------
num = '111100001111'# convert 1 to 0 and vice versa
b = num.replace("1", "x").replace("0", "1").replace("x", "0")
print(b)
# solution 2
output = ''
for i in num:
    if i == '1':
        output += '0'
    else:
        output += '1'
print(output)
----------------------------------
"""
import tkinter as Tkinter
from datetime import datetime
counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter
			# To manage the intial delay. 
            if counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string
	
            label['text'] = display
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
            label.after(1000, count)
            counter += 1
	
	# Triggering the start of the counter. 
    count()
	

# start function of the stopwatch 
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
	

# Stop function of the stopwatch 
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False
	

# Reset function of the stopwatch 
def Reset(label):
	global counter
	counter = 0
	# If reset is pressed after pressing stop. 
	if not running:
		reset['state'] = 'disabled'
		label['text'] = '00:00:00'
	# If reset is pressed while the stopwatch is running. 
	else:
		label['text'] = '00:00:00'


root = Tkinter.Tk()
root.title("Stopwatch")

# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text='Ready!', fg='black', font='Verdana 30 bold')
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()
