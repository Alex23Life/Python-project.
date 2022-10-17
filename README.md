# Python-project.
 Learn foreign language or whatever you want with flash card program.

This program let you learn new words from foreign language. In this case it is English to French. But it could be whatever you want. 
Click left button to skip word and show another one. If you would like to see translation again click button in the middle.
And if you are sure you have learned the word, press button on the rignt to show new word and remove from list old one (the old word will no longer appear).

Short description of the content of the program.
For User interface was used tkinter package.
For work with data was used pandas packege.
To random words was used random module.

Program contain four function:
- next_card() Used for button on the right. 
Stoped background counting of window.after() func. Swith cards. Randomly selects and displays new word for three sec and then switch back to front card with 
translation.

-flip_card() Used in next_card() func.
switch back to front card with translation of the word.

- repeat_card() Used for button in the middle.
Displays translation for 3 sec with back card and swith back to front card.

- is_known() Used for button on the right.
Removed learnt word and displays new one for 3 sec then switched back to front card. 



Description how to create my programm:

Vizualization part:
-Create window( use Tk()) and customize it with pady, padx attributes ( use config() give space bettween frameworks and canvas). 
Use window.mainloop() to prevent disappearance of window as we run the program.
-Extract images from folder "images"(obviously😅) using PhotoImage() function.
-Create canvas( use Canvas() ) and customize it with width, height, highlightthickness, bg attributes.
Make background image ( create_image() ), create text on it( create_text() ), place it ( grid() ).
-Create buttons ( Button() ) using images that we extracted ( wrong.png, right.png and so on). 
After creating functions ( look below 👇) add "command" attribut to each button.

Before creating functions we should open existing data file:
Create two empty dictionary for futher work with them ( to_learn, current_card variables )
Open file ( use pandas.read_csv() ) create variable and transform it to dictionary ( data.to_dict() )
Use try, except, else blocks for escaping errors like "FileNotFoundError" in case if data file "words_to_learn.csv" still doesn't exist or has been removed.

Functions:
- next_card() - defenition above☝️.
Trying not to confuse you, here is some explanation for "window_flip_timer"( window.after(sec, func) )var. This variable give us three sec to look at word 
and then it run next_card() func. Used in func such as next_card(), repeat_card().
Use global to have access to varibale "current_card" and "window_flip_timer" to be able change it.

Returning to next_card() func. To prevent background counting i.e escape bag use window.after_cancel() func. 
Choose new word to learn from data file ( random.choice() ). 
Customize image and text of canvas ( canvas.itemeconfig() ) for our new word.
Add window_flip_timer() to start countdown and show translate of word after.

- flip_card():
Customize background image and text as well( canvas.itemconfig() )

- repeat_card():
As well as in next_card() func. add "window_flip_timer" var and use window.after_cancel() func.
Customze canvas to show word again ( use itemcongif() ).

- is_know():
Remove already known word from csv data file ( use data.remove() ) that was created before and save updated data.
Use next_card() func to repeat process of showing new word.
