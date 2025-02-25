import random
from tkinter import *

# Initialize score
score = 0


def onenter():
    global score

    # Get the user's input and convert to integer
    ans = inp.get()
    num = random.randint(1, 10)  # Generate a random number
    print(num)  # Debugging purpose
    if ans.isdigit():  # Ensure input is a number
        ans = int(ans)
    else:
        label2.config(text="Invalid Input")
        return


    if ans == num:
        score += 1
        label2.config(text=f'{score}/10')  # Update score label

        # Check if game is over
        if score == 10:
            label2.config(text="You Won! Exiting...")
            window.after(2000, window.destroy)  # Exit after 2 seconds
    else:
        label2.config(text="Game Over")
        btn.config(state="disabled")  # Disable button
        inp.config(state="disabled")  # Disable input
        window.after(2000, window.destroy)  # Exit after 2 seconds


# Create main window
window = Tk()
window.title("Guessing Game")

Label(window, text="Guess a number between 1 and 10").grid(column=1, row=0)

inp = Entry(window)
inp.grid(column=1, row=1)

btn = Button(window, text="Submit", command=onenter)
btn.grid(column=1, row=2)

label2 = Label(window, text=f'{score}/10')
label2.grid(column=1, row=3)

window.mainloop()
