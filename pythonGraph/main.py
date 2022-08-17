import matplotlib.pyplot as plt
from tkinter import *
import time


# Input function
def inp():
    inp.input = int(entry.get())
    wd.destroy()
    formula.y = [inp.input]
    formula(inp.input)


# Cancel function
def cancel():
    exit()


# Formula calculations
def formula(n):
    if ((n % 1) == 0) & (n >= 1):
        if n != 1:
            formula.counter += 1
            formula.x.append(formula.counter)
            if (n % 2) != 0:
                ans = 3*n+1
            else:
                ans = n/2
            formula.y.append(int(ans))
            formula(ans)
        else:
            return
    else:
        print("error")
        exit()


# Variables
i = 0
inp.input = 0
formula.counter = 0
formula.x = [1]
formula.y = [inp.input]

# Input window
wd = Tk()
wd.geometry('300x140')
wd.title('Input Number')

entry = Entry()
entry.config(font=('Arial', 50), fg='#282828', bg='#FFFFFF', width=10)
entry.pack(padx=10, pady=(10, 0))

cancel = Button(wd, text="cancel", command=cancel)
cancel.pack(side=BOTTOM, padx=10, pady=(0, 5), fill=BOTH)

submit = Button(wd, text="submit", command=inp)
submit.pack(side=BOTTOM, padx=10, pady=(0, 0), fill=BOTH)

wd.mainloop()

# Customizing the graph window
fig = plt.figure(facecolor='#FFE3E3')
plt.xlabel('Amount of steps')
plt.title('Collatz Conjecture')

# Inserting Graph
plt.plot(formula.x, formula.y, color='#96656A', zorder=1)

time.sleep(1)

# Inserting Scatter Points for extra clarity
for _ in range(len(formula.x)):
    plt.scatter(formula.x[i], formula.y[i], s=25, zorder=2, color='#dda3b2', facecolor='#FFDDDD')
    plt.pause(0.001)
    i += 1

# Viewing the graph
plt.show()
