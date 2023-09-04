'''
Name: Raj Shah
Desciption: This is a GUI based program using tkinter that is programmed to be
a random guessing game where the user tries to guess the number. See
'How to Play' when program is running for more details.

'''

# Import modules
from tkinter import *
from tkinter import messagebox
from random import randint

# Create the window and window title
window = Tk()
window.title("Number Mastermind")
window.geometry('990x700')


# ↓ MAIN GAME LOGIC - NUMBER BUTTONS AND INPUT BOX ↓

# Create input box and increment for every button when clicked - see line 321 & 391
def NumberButton0():
    global input_box
    input_box += '0'
    input_box_placement.configure(text = input_box)

def NumberButton1():
    global input_box
    input_box += '1'
    input_box_placement.configure(text = input_box)
     
def NumberButton2():
    global input_box
    input_box += '2'
    input_box_placement.configure(text = input_box)

def NumberButton3():
    global input_box
    input_box += '3'
    input_box_placement.configure(text = input_box)
     
def NumberButton4():
    global input_box
    input_box += '4'
    input_box_placement.configure(text = input_box)
     
def NumberButton5():
    global input_box
    input_box += '5'
    input_box_placement.configure(text = input_box)
     
def NumberButton6():
    global input_box
    input_box += '6'
    input_box_placement.configure(text = input_box)
     
def NumberButton7():
    global input_box
    input_box += '7'
    input_box_placement.configure(text = input_box)
     
def NumberButton8():
    global input_box
    input_box += '8'
    input_box_placement.configure(text = input_box)
    
def NumberButton9():
    global input_box
    input_box += '9'
    input_box_placement.configure(text = input_box)

def BackspaceInput():
    global input_box
    input_box = input_box[:-1]
    input_box_placement.configure(text = input_box)
    
# Define "lowest", "maximum" and "guesses" variables.
# (see lines 434-435 for "secret number" and "amount of current guesses" variables)
lowest_random_num = 0
maximum_random_num = 9
max_guesses = 3


# Create main game - generate random number and allow user to try and guess it.
def EnterInput():
    global final_guess
    global input_box
    final_guess = input_box
    
    input_box = ''
    input_box_placement.configure(text = input_box)
    
    global lblNumberGuesses
    global lblMaxGuesses
    
    global amount_of_current_guesses
    global secret_number
    global willContinue
    
    willContinue = False
    
    # Check if the input is an integer, not a string (" ").
    try:
        while amount_of_current_guesses < max_guesses and int(final_guess) >= \
              lowest_random_num and int(final_guess) <= maximum_random_num:
            
            # Check if final guess is greater than secret number.
            if int(final_guess) > secret_number:
                lblHint = Label(window, text = ' ' * 55 + \
                        "The secret number is less than " + \
                        final_guess + ". Please try again." + \
                        ' ' * 100, font = ("Calibri", 18), fg = 'orange')
                lblHint.place(x = 0, y = 390) # *new concept* see note above. 
                amount_of_current_guesses += 1
                willContinue = True
                
                # Create "Number of Guesses" label.
                lblNumberGuesses = Label(window, text = "Number of Guesses: " \
                    + str(amount_of_current_guesses), font = ("Calibri", 20), \
                    fg = 'purple')

                lblNumberGuesses.place(x = 30, y = 145)
                
                break
            
            # Check if final guess is less than secret number.
            elif int(final_guess) < secret_number:
                lblHint = Label(window, text = ' ' * 50 + "The secret number \
is greater than " + final_guess + ". Please try again." + ' ' * 100, \
                            font = ("Calibri", 18), fg = 'dark blue')
                lblHint.place(x = 0, y = 390)
                amount_of_current_guesses += 1
                willContinue = True
                
                # Update "Number of Guesses" label.
                lblNumberGuesses = Label(window, text = "Number of Guesses: " \
                    + str(amount_of_current_guesses), font = ("Calibri", 20), \
                                         fg = 'purple')
   
                lblNumberGuesses.place(x = 30, y = 145)
                
                break
            
            # Check if final guess is equal to secret number. 
            else:
                lblHint = Label(window, text = ' ' * 67 + "Your guess was \
correct. You won! :)" + ' ' * 100, font = ("Calibri", 18), fg = 'green')
                lblHint.place(x = 0, y = 392)
                amount_of_current_guesses_2 = amount_of_current_guesses + 1
                amount_of_current_guesses = max_guesses
                willContinue = False
                
                # Update "Number of Guesses" label.
                lblNumberGuesses = Label(window, text = "Number of Guesses: " \
                    + str(amount_of_current_guesses_2), font = \
                                         ("Calibri", 20), fg = 'purple')
    
                lblNumberGuesses.place(x = 30, y = 145)
                
                
                # ENABLE 'CHANGE' BUTTONS AND TEXT BOX - see lines 520-618
                btnChangeLowest = Button(window, text = 'Change Lowest \
Number', command = ChangeLowest, font = ('Calibri', 15), fg = 'orange')
                txtChangeLowest.configure(state = 'normal')

                btnChangeMaximum = Button(window, text = 'Change Maximum \
Number', command = ChangeMaximum, font = ('Calibri', 15), fg = 'dark blue')
                txtChangeMaximum.configure(state = 'normal')

                btnChangeMaxGuess = Button(window, text = 'Change Maximum \
Guesses', command = ChangeMaxGuess, font = ('Calibri', 15), fg = 'purple')
                txtChangeMaxGuess.configure(state = 'normal')
    
                btnChangeLowest.place(x = 70, y = 491.5)
                btnChangeMaximum.place(x = 385, y = 491.5)
                btnChangeMaxGuess.place(x = 710, y = 491.5)
    
    
                # DISABLE NUMBER, ENTER, BACKSPACE BUTTONS - see lines 360-385
                btn0 = Button(window, text = "0", command = NumberButton0, \
            state = DISABLED, font = ("Calibri", 25)) # *new concept* see note above. 
                btn1 = Button(window, text = "1", command = NumberButton1, \
                      state = DISABLED, font = ("Calibri", 25))
                btn2 = Button(window, text = "2", command = NumberButton2, \
                      state = DISABLED, font = ("Calibri", 25))
                btn3 = Button(window, text = "3", command = NumberButton3, \
                      state = DISABLED, font = ("Calibri", 25))
                btn4 = Button(window, text = "4", command = NumberButton4, \
                      state = DISABLED, font = ("Calibri", 25))
                btn5 = Button(window, text = "5", command = NumberButton5, \
                      state = DISABLED, font = ("Calibri", 25))
                btn6 = Button(window, text = "6", command = NumberButton6, \
                      state = DISABLED, font = ("Calibri", 25))
                btn7 = Button(window, text = "7", command = NumberButton7, \
                      state = DISABLED, font = ("Calibri", 25))
                btn8 = Button(window, text = "8", command = NumberButton8, \
                      state = DISABLED, font = ("Calibri", 25))
                btn9 = Button(window, text = "9", command = NumberButton9, \
                      state = DISABLED, font = ("Calibri", 25))

                btnBackspace = Button(window, text = "BACKSPACE", command = \
                    BackspaceInput, state = DISABLED, font = ("Calibri", 20))
                btnEnter = Button(window, text = "ENTER", command = \
                    EnterInput, state = DISABLED, font = ("Calibri Bold", 25))
    
                btn0.place(x = 15, y = 265)
                btn1.place(x = 108, y = 265)
                btn2.place(x = 201, y = 265)
                btn3.place(x = 293, y = 265)
                btn4.place(x = 386, y = 265)
                btn5.place(x = 479, y = 265)
                btn6.place(x = 572, y = 265)
                btn7.place(x = 665, y = 265)
                btn8.place(x = 757, y = 265)
                btn9.place(x = 850, y = 265)
                btnBackspace.place(x = 396, y = 315)
                btnEnter.place(x = 414, y = 352)
                
                break
        
        # Check if they've reached the max guesses.
        if willContinue == True and amount_of_current_guesses == max_guesses \
           and int(final_guess) >= lowest_random_num and int(final_guess) \
           <= maximum_random_num:
            
            lblHint = Label(window, text = ' ' * 45 + "You've reached the \
maximum amount of guesses. You lost! :(" + ' ' * 100, font = ("Calibri", 18), \
                            fg = 'red')
            lblHint.place(x = 0, y = 390)
            
            
            # ENABLE 'CHANGE' BUTTONS AND TEXT BOX - see lines 520-618
            btnChangeLowest = Button(window, text = 'Change Lowest \
Number', command = ChangeLowest, font = ('Calibri', 15), fg = 'orange')
            txtChangeLowest.configure(state = 'normal')

            btnChangeMaximum = Button(window, text = 'Change Maximum \
Number', command = ChangeMaximum, font = ('Calibri', 15), fg = 'dark blue')
            txtChangeMaximum.configure(state = 'normal')

            btnChangeMaxGuess = Button(window, text = 'Change Maximum \
Guesses', command = ChangeMaxGuess, font = ('Calibri', 15), fg = 'purple')
            txtChangeMaxGuess.configure(state = 'normal')
    
            btnChangeLowest.place(x = 70, y = 491.5)
            btnChangeMaximum.place(x = 385, y = 491.5)
            btnChangeMaxGuess.place(x = 710, y = 491.5)
    
    
            # DISABLE NUMBER, ENTER, BACKSPACE BUTTONS - see lines 360-385
            btn0 = Button(window, text = "0", command = NumberButton0, \
                        state = DISABLED, font = ("Calibri", 25))
            btn1 = Button(window, text = "1", command = NumberButton1, \
                        state = DISABLED, font = ("Calibri", 25))
            btn2 = Button(window, text = "2", command = NumberButton2, \
                      state = DISABLED, font = ("Calibri", 25))
            btn3 = Button(window, text = "3", command = NumberButton3, \
                      state = DISABLED, font = ("Calibri", 25))
            btn4 = Button(window, text = "4", command = NumberButton4, \
                      state = DISABLED, font = ("Calibri", 25))
            btn5 = Button(window, text = "5", command = NumberButton5, \
                      state = DISABLED, font = ("Calibri", 25))
            btn6 = Button(window, text = "6", command = NumberButton6, \
                      state = DISABLED, font = ("Calibri", 25))
            btn7 = Button(window, text = "7", command = NumberButton7, \
                      state = DISABLED, font = ("Calibri", 25))
            btn8 = Button(window, text = "8", command = NumberButton8, \
                      state = DISABLED, font = ("Calibri", 25))
            btn9 = Button(window, text = "9", command = NumberButton9, \
                      state = DISABLED, font = ("Calibri", 25))

            btnBackspace = Button(window, text = "BACKSPACE", command = \
                    BackspaceInput, state = DISABLED, font = ("Calibri", 20))
            btnEnter = Button(window, text = "ENTER", command = \
                    EnterInput, state = DISABLED, font = ("Calibri Bold", 25))
    
            btn0.place(x = 15, y = 265)
            btn1.place(x = 108, y = 265)
            btn2.place(x = 201, y = 265)
            btn3.place(x = 293, y = 265)
            btn4.place(x = 386, y = 265)
            btn5.place(x = 479, y = 265)
            btn6.place(x = 572, y = 265)
            btn7.place(x = 665, y = 265)
            btn8.place(x = 757, y = 265)
            btn9.place(x = 850, y = 265)
            btnBackspace.place(x = 396, y = 315)
            btnEnter.place(x = 414, y = 352)    
            
        
        # Check if input is in between lowest and highest random number.
        elif int(final_guess) < lowest_random_num or int(final_guess) > \
           maximum_random_num:
            
            lblHint = Label(window, text = ' ' * 64 + 'Please enter a valid \
input between ' + str(lowest_random_num) + '-' + str(maximum_random_num) \
                    + '.' + ' ' * 50, font = ("Calibri", 18), fg = 'red')
            lblHint.place(x = 0, y = 390)
    
    # Ensure incorrect input doesn't break code, instead prints warning message.
    except:          
        lblHint = Label(window, text = ' ' * 64 + 'Please enter a valid input \
between ' + str(lowest_random_num) + '-' + str(maximum_random_num) \
                    + '.' + ' ' * 100, font = ("Calibri", 18), fg = 'red')
        lblHint.place(x = 0, y = 390)

# Define input box variable as empty text
for i in range(max_guesses):
    input_box = ''

# ↓ LABELS & DIVIDERS ↓

# Title label and divider label
lblTitle = Label(window, text = " Number Mastermind: Guess the Code!", font = \
                 ("Calibri Light", 60), fg = 'dark blue')
lblDivider1 = Label(window, text = "*" * 162)

# "Guess a number" label - will update later (see lines 552-558)
lblGuess = Label(window, text = "Guess a number between " + \
            str(lowest_random_num) + " to " + \
            str(maximum_random_num), font = ("Calibri Bold", 25), fg = 'green')

# Max Guesses label - will update later (see lines 614-616)
lblMaxGuesses = Label(window, text = "Maximum Guesses: " + \
                        str(max_guesses), font = ("Calibri", 20), fg = 'purple')

# Divider label
lblDivider2 = Label(window, text = "*" * 162)


# ↓ LABEL & DIVIDER GRIDS ↓

# Title and divider label grids.
lblTitle.place(x = 0, y = 0)
lblDivider1.place(x = 0, y = 77)
 
# Guess label grid.
lblGuess.place(x = 280, y = 100)

# Max Guesses label grid.
lblMaxGuesses.place(x = 655, y = 145)

# Divider label grid
lblDivider2.place(x = 0, y = 180)


# Create number buttons (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, BACKSPACE, ENTER)
btn0 = Button(window, text = "0", command = NumberButton0, state = DISABLED, \
              font = ("Calibri", 25))
btn1 = Button(window, text = "1", command = NumberButton1, state = DISABLED, \
              font = ("Calibri", 25))
btn2 = Button(window, text = "2", command = NumberButton2, state = DISABLED, \
              font = ("Calibri", 25))
btn3 = Button(window, text = "3", command = NumberButton3, state = DISABLED, \
              font = ("Calibri", 25))
btn4 = Button(window, text = "4", command = NumberButton4, state = DISABLED, \
              font = ("Calibri", 25))
btn5 = Button(window, text = "5", command = NumberButton5, state = DISABLED, \
              font = ("Calibri", 25))
btn6 = Button(window, text = "6", command = NumberButton6, state = DISABLED,
              font = ("Calibri", 25))
btn7 = Button(window, text = "7", command = NumberButton7, state = DISABLED, \
              font = ("Calibri", 25))
btn8 = Button(window, text = "8", command = NumberButton8, state = DISABLED, \
              font = ("Calibri", 25))
btn9 = Button(window, text = "9", command = NumberButton9, state = DISABLED, \
              font = ("Calibri", 25))

btnBackspace = Button(window, text = "BACKSPACE", command = BackspaceInput, \
                      state = DISABLED, font = ("Calibri", 20))
btnEnter = Button(window, text = "ENTER", command = EnterInput, state = \
                  DISABLED, font = ("Calibri Bold", 25))


# ↓ NUMBER BUTTON GRIDS & INPUT BOX PLACEMENT ↓

# Input box placement
input_box_placement = Label(window, text = "", font = ("Calibri Bold", 50))
input_box_placement.place(x = 428, y = 191)

# Number button grids
btn0.place(x = 15, y = 265)
btn1.place(x = 108, y = 265)
btn2.place(x = 201, y = 265)
btn3.place(x = 293, y = 265)
btn4.place(x = 386, y = 265)
btn5.place(x = 479, y = 265)
btn6.place(x = 572, y = 265)
btn7.place(x = 665, y = 265)
btn8.place(x = 757, y = 265)
btn9.place(x = 850, y = 265)
btnBackspace.place(x = 396, y = 315)
btnEnter.place(x = 414, y = 352)


# ↓ HINT MESSAGE ↓

# Create hint message to inform user if they are close to guessing the number
# The hint message will change as the enter button is clicked (see lines 117-318)
lblHint = Label(window, text = ' ' * 200, font = ("Calibri", 18))
lblDivider3 = Label(window, text = "*" * 162)

# Hint message and divider grids
lblHint.place(x = 0, y = 390)
lblDivider3.place(x = 0, y = 415)
    

# ↓ START/RESTART GAME BUTTON ↓

# Define start/restart button (disable other buttons accordingly when clicked)
def Start_Restart():
    global amount_of_current_guesses
    global secret_number
    
    # change button text
    btnStart_Restart = Button(window, text = "Restart Game", command = \
                              Start_Restart, font = ("Calibri Bold", 25), fg = 'red')
    btnStart_Restart.place(x = 382, y = 440)
    
    # create/update variables
    amount_of_current_guesses = 0
    secret_number = randint(lowest_random_num, maximum_random_num)
    
    lblNumberGuesses = Label(window, text = "Number of Guesses: " \
            + str(amount_of_current_guesses), font = ("Calibri", 20), fg = 'purple')

    lblNumberGuesses.place(x = 30, y = 145)
    
    # update hint message (found line 413)
    lblHint = Label(window, text = " " * 78 + 'Please enter your guess.' \
                    + " " * 100, font = ("Calibri", 18), fg = 'sky blue')
    lblHint.place(x = 0, y = 390)
    
    # update warning message (found lines 532-581)
    lblWarningMessage = Label(window, text = ' ' * 200, font = ("Calibri", 15))
    lblWarningMessage.place(x = 0, y = 524)

    
    # DISABLE 'CHANGE' BUTTONS AND TEXT BOX - see lines 520-618 
    btnChangeLowest = Button(window, text = 'Change Lowest Number', \
            command = ChangeLowest, state = DISABLED, font = ('Calibri', 15))
    txtChangeLowest.configure(state = 'disabled')

    btnChangeMaximum = Button(window, text = 'Change Maximum Number', \
            command = ChangeMaximum, state = DISABLED, font = ('Calibri', 15))
    txtChangeMaximum.configure(state = 'disabled')

    btnChangeMaxGuess = Button(window, text = 'Change Maximum Guesses', \
            command = ChangeMaxGuess, state = DISABLED, font = ('Calibri', 15))
    txtChangeMaxGuess.configure(state = 'disabled')
    
    btnChangeLowest.place(x = 70, y = 491.5)
    btnChangeMaximum.place(x = 385, y = 491.5)
    btnChangeMaxGuess.place(x = 710, y = 491.5)
    txtChangeLowest.place(x = 10, y = 490)
    txtChangeMaximum.place(x = 325, y = 490)
    txtChangeMaxGuess.place(x = 650, y = 490)
    
    
    # ENABLE NUMBER, ENTER, BACKSPACE BUTTONS - see lines 360-385
    btn0 = Button(window, text = "0", command = NumberButton0, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn1 = Button(window, text = "1", command = NumberButton1, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn2 = Button(window, text = "2", command = NumberButton2, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn3 = Button(window, text = "3", command = NumberButton3, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn4 = Button(window, text = "4", command = NumberButton4, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn5 = Button(window, text = "5", command = NumberButton5, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn6 = Button(window, text = "6", command = NumberButton6, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn7 = Button(window, text = "7", command = NumberButton7, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn8 = Button(window, text = "8", command = NumberButton8, \
              font = ("Calibri", 25), fg = 'dark blue')
    btn9 = Button(window, text = "9", command = NumberButton9, \
              font = ("Calibri", 25), fg = 'dark blue')

    btnBackspace = Button(window, text = "BACKSPACE", command = BackspaceInput, \
                       font = ("Calibri", 20), fg = 'orange')
    btnEnter = Button(window, text = "ENTER", command = EnterInput, \
                      font = ("Calibri Bold", 25), fg = 'dark green')
    
    btn0.place(x = 15, y = 265)
    btn1.place(x = 108, y = 265)
    btn2.place(x = 201, y = 265)
    btn3.place(x = 293, y = 265)
    btn4.place(x = 386, y = 265)
    btn5.place(x = 479, y = 265)
    btn6.place(x = 572, y = 265)
    btn7.place(x = 665, y = 265)
    btn8.place(x = 757, y = 265)
    btn9.place(x = 850, y = 265)
    btnBackspace.place(x = 396, y = 315)
    btnEnter.place(x = 414, y = 352)


# Create start button, restart button (line 429) will appear once start is clicked 
btnStart_Restart = Button(window, text = "Start Game", command = Start_Restart, \
                          font = ("Calibri Bold", 25), fg = 'green')
btnStart_Restart.place(x = 387, y = 440)


# ↓ ALLOW USER TO CHANGE LOWEST NUMBER, MAXIMUM NUMBER & MAX GUESSES ↓

# Define every button and perform its respective action
def ChangeLowest():
    global lowest_random_num
    global maximum_random_num
    
    # Check to see if the input is valid.
    try:
        if int(txtChangeLowest.get()) > maximum_random_num or \
           int(txtChangeLowest.get()) < -9999 or int(txtChangeLowest.get()) < 0:
            
            lblWarningMessage = Label(window, text = ' ' * 29 + "Please enter \
a valid input (max. 4 characters). Lowest Number must be less than \
Maximum Number." + ' ' * 100, font = ("Calibri", 15), fg = 'red')
            lblWarningMessage.place(x = 0, y = 524)
        
        else:
            lowest_random_num = int(txtChangeLowest.get())
            lblWarningMessage = Label(window, text = ' ' * 800, \
                                      font = ("Calibri", 15))
            lblWarningMessage.place(x = 0, y = 524)
    
    # Ensure incorrect input doesn't break code, instead prints warning message.
    except:
        lblWarningMessage = Label(window, text = ' ' * 85 + "Please enter \
a valid integer input." + ' ' * 100, \
                                  font = ("Calibri", 15), fg = 'red')
        lblWarningMessage.place(x = 0, y = 524)
    
    
    # Change "Guesses" button.
    lblGuess = Label(window, text = "Guess a number between " + \
                    str(lowest_random_num) + " to " + str(maximum_random_num) + \
                    ' ' * 50, font = ("Calibri Bold", 25), fg = 'green')
    lblGuess.place(x = 280, y = 100)
    
def ChangeMaximum():
    global maximum_random_num
    global lowest_random_num
    
    # Check to see if the input is valid. 
    try:
        if int(txtChangeMaximum.get()) < lowest_random_num or \
               int(txtChangeMaximum.get()) > 9999 or int(txtChangeMaximum.get()) < 0:
            
            lblWarningMessage = Label(window, text = ' ' * 26 + "Please enter \
a valid input (max. 4 characters). Maximum Number must be greater \
than Lowest Number." + ' ' * 100, font = ("Calibri", 15), fg = 'red')
            lblWarningMessage.place(x = 0, y = 524)
        
        else:
            maximum_random_num = int(txtChangeMaximum.get())
            lblWarningMessage = Label(window, text = ' ' * 900, \
                                      font = ("Calibri", 15))
            lblWarningMessage.place(x = 0, y = 524)
    
    # Ensure incorrect input doesn't break code, instead prints warning message.
    except:
        lblWarningMessage = Label(window, text = ' ' * 85 + "Please enter \
a valid integer input." + ' ' * 100, font = ("Calibri", 15), fg = 'red')
        lblWarningMessage.place(x = 0, y = 524)
    
    
    # Change "Guesses" button.
    lblGuess = Label(window, text = "Guess a number between " + \
            str(lowest_random_num) + " to " + str(maximum_random_num) + \
                     ' ' * 50, font = ("Calibri Bold", 25), fg = 'green')
    lblGuess.place(x = 280, y = 100)

def ChangeMaxGuess():
    global max_guesses
    
    # Check to see if the input is valid.
    try:
        if int(txtChangeMaxGuess.get()) > 9999 or int(txtChangeMaxGuess.get()) <= 0:
            lblWarningMessage = Label(window, text = ' ' * 75 + "Please enter \
a valid input (max. 4 characters)." + ' ' * 100, font = ("Calibri", 15), fg = 'red')
            lblWarningMessage.place(x = 0, y = 524)
            
        else:
            max_guesses = int(txtChangeMaxGuess.get())
            lblWarningMessage = Label(window, text = ' ' * 900, \
                                      font = ("Calibri", 15))
            lblWarningMessage.place(x = 0, y = 524)
    
    # Ensure incorrect input doesn't break code, instead prints warning message.
    except:
        lblWarningMessage = Label(window, text = ' ' * 85 + "Please enter \
a valid integer input." + ' ' * 100, font = ("Calibri", 15), fg = 'red')
        lblWarningMessage.place(x = 0, y = 524)
        
    
    # Change "Max Guesses" button.
    lblMaxGuesses = Label(window, text = "Maximum Guesses: " + \
            str(max_guesses) + ' ' * 50, font = ("Calibri", 20), fg = 'purple')
    lblMaxGuesses.place(x = 655, y = 145)


# ↓ LOWEST NUMBER, HIGHEST NUMBER & MAX GUESSES ↓

# Create "change lowest number" button and textbox
txtChangeLowest = Entry(window, width = 5)
btnChangeLowest = Button(window, text = 'Change Lowest Number', \
                command = ChangeLowest, font = ('Calibri', 15), fg = 'orange')

# Create "change maximum number" button and textbox
txtChangeMaximum = Entry(window, width = 5)
btnChangeMaximum = Button(window, text = 'Change Maximum Number', \
                command = ChangeMaximum, font = ('Calibri', 15), fg = 'dark blue')

# Create "change max guesses" button and textbox
txtChangeMaxGuess = Entry(window, width = 5)
btnChangeMaxGuess = Button(window, text = 'Change Maximum Guesses', \
                command = ChangeMaxGuess, font = ('Calibri', 15), fg = 'purple')


# ↓ LOWEST NUMBER, HIGHEST NUMBER & MAX GUESSES GRIDS ↓

# "Lowest number" button and textbox grids
txtChangeLowest.place(x = 10, y = 490)
btnChangeLowest.place(x = 70, y = 491.5)

# "Maximum number" button and textbox grids
txtChangeMaximum.place(x = 325, y = 490)
btnChangeMaximum.place(x = 385, y = 491.5)

# "Max guesses" button and textbox grids
txtChangeMaxGuess.place(x = 650, y = 490)
btnChangeMaxGuess.place(x = 710, y = 491.5)


# ↓ HOW TO PLAY BUTTON ↓

# Show messagebox when clicked
def MessageBox():
    messagebox.showinfo('How to Play', " Start the game and choose a number \
between 1-9, this range can be changed later. Use the number buttons to \
enter your guess, the game will tell you if your number is greater, lower or \
equal to the secret number. If you guess the secret number correctly in less \
attempts than the maximum guesses, you win! Otherwise, you can try again and \
adjust the maximum number, lowest number, and maximum guesses! Have Fun!")

# Create Help button
btnHelp = Button(window, text = 'How to Play', command = MessageBox, \
                 font = ('Calibri', 25), fg = 'blue')
btnHelp.place(x = 389, y = 590)

window.mainloop()
