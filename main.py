from tkinter import * #For GUI
import random #Randomiser
from PIL import Image, ImageTk #For images
from tkinter import messagebox #For error box

names = [] #List
asked = [] #List
score = 0

def random_order():  # Makes the order of the questions random
    global qnum #The number assigned to the question
    qnum = random.randint(1, 10)  # Choses an integer between 1 and 10 randomly (integer corresponds to question number)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        random_order()


class Quiz1:  # The title page

    def __init__(self, parent):
        background_color = 'lightgrey'  # Background color of the text

        self.main_title = Label(window, text='Car Quiz', font=('Times',
                                '55', 'bold'), bg=background_color)  # Code for title of the quiz
        self.main_title.place(x=520, y=100)  # Location of title

        self.var1 = IntVar()

        self.user_instruction = Label(window,
                text='Please Enter Your Username Below:', font=('Times'
                , '18', 'bold'), bg=background_color)  # Code for instructions for user
        self.user_instruction.place(x=450, y=300)  # Location of the instruction

        self.name_entry = Entry(window)  # Code for name entry box
        self.name_entry.place(x=600, y=400)  # Location of entry box

        self.start_button = Button(window, text='START',
                                   font=('Helvetica', ' 13', 'bold'),
                                   bg='forestgreen',
                                   command=self.name_storer)  # Code for start button to go to next page
        self.start_button.place(x=642, y=450)  # Location of start button

    def name_storer(self):
        name = self.name_entry.get()
        if name == '':
            messagebox.showerror('Name is required!!',
                                 'Please enter your name!') #Error message if entrybox left blank
        elif len(name) > 15:
            messagebox.showerror('an error has occurred!',
                                 'Username is too long, max 15 letter') #Error message if username length > 15
        elif len(name) < 3:
            messagebox.showerror('an error has occurred!',
                                 'Username is too short, min 3 letters') #Error message if username length < 3
        elif name.isnumeric():
            messagebox.showerror('an error has occurred!',
                                 'Name can only consist of letters!') #Error message if username consists of numbers
        elif not name.isalpha():
            messagebox.showerror('an error has occurred!',
                                 'No Symbols Please! Please Try Again!') #Error message if username consists of special characters
        else:
            names.append(name)
            print (names)
            self.main_title.destroy()  # Destroys the widget
            self.user_instruction.destroy()  # Destroys the widget
            self.name_entry.destroy()  # Destroys the widget
            self.start_button.destroy()  # Destroys the widget
            quiz_questions(window)


class quiz_questions:  # Main page (actual quiz page)

    def __init__(self, parent):

        self.qna = {  # Questions that will be asked
                      # Q1
                      # Q2
                      # Q3
                      # Q4
                      # Q5
                      # Q6
                      # Q7
                      # Q8
                      # Q9
                      # Q10
            1: [
                'Which car company sold the most cars in 2020 worldwide?'
                    ,
                'Ford',
                'Mazda',
                'Toyota',
                'Nissan',
                'Toyota',
                3,
                ],
            2: [
                'Which car company has the car model Portofino?',
                'Ferrari',
                'Lotus',
                'Porsche',
                'Skoda',
                'Ferrari',
                1,
                ],
            3: [
                'What car company is worth the most?',
                'Toyota',
                'Tesla',
                'Ferrari',
                'Audi',
                'Tesla',
                2,
                ],
            4: [
                'Which Formula 1 team has won the most Constrcutors Championships?'
                    ,
                'Williams',
                'Mercedes',
                'Ferrari',
                'Red Bull',
                'Ferrari',
                3,
                ],
            5: [
                'How many cars are there in NZ (millions)?',
                '4.40',
                '5.30',
                '3.60',
                '4.20',
                '4.40',
                1,
                ],
            6: [
                'Which is NOT a car company not owned by Volkswagen',
                'Audi',
                'Mercedes',
                'Porsche',
                'Bentley',
                'Mercedes',
                2,
                ],
            7: [
                'Which car company did Enzo Ferrari found?',
                'Toyota',
                'Tesla',
                'Ferrari',
                'Audi',
                'Ferrari',
                3,
                ],
            8: [
                "What color is Mr Bean's car?",
                'Green',
                'Yellow',
                'Blue',
                'Red',
                'Green',
                1,
                ],
            9: [
                'What year did NASCAR first start',
                '1950',
                '1949',
                '1953',
                '2016',
                '1949',
                2,
                ],
            10: [
                'Which famous Pixar movie released in 2006',
                'Toy Story',
                'Cars',
                'Brave',
                'Up',
                'Cars',
                2,
                ],
            }


        random_order()

        self.question_label = Label(window, text=self.qna[qnum][0],
                                    font=('Tw Cen MT', '18', 'bold'))  # Code for the question that'll be asked
        self.question_label.place(x=50, y=50)  # Code for location

        self.var1 = IntVar()

        self.rb1 = Radiobutton(  # Code for option 1 button
            window,
            text=self.qna[qnum][1],
            font=('Helvetica', '30'),
            bg='red',
            value=1,
            variable=self.var1,
            )
        self.rb1.place(x=600, y=400)  # Code for location

        self.rb2 = Radiobutton(  # Code for option 2 button
            window,
            text=self.qna[qnum][2],
            font=('Helvetica', '30'),
            bg='blue',
            value=2,
            variable=self.var1,
            )
        self.rb2.place(x=200, y=400)  # Code for location

        self.rb3 = Radiobutton(  # Code for option 3 button
            window,
            text=self.qna[qnum][3],
            font=('Helvetica', '30'),
            bg='yellow',
            value=3,
            variable=self.var1,
            )
        self.rb3.place(x=600, y=200)  # Code for location

        self.rb4 = Radiobutton(  # Code for option 4 button
            window,
            text=self.qna[qnum][4],
            font=('Helvetica', '30'),
            bg='limegreen',
            value=4,
            variable=self.var1,
            )
        self.rb4.place(x=200, y=200)  # Code for location

        self.confirm_button = Button(window, text='Confrim',
                bg='forestgreen', command=self.score_mechanics)  # Code for confirm button to confirmm user's chosen answer
        self.confirm_button.place(x=525, y=500)  # Code for location
        self.score_display = Label(window, text='score')  # Label that displays' the user's score
        self.score_display.place(x=550, y=550)  # Code for location

        self.leave = Button(window, text='X', font=('Helvetica', '13',
                            'bold'), bg='red', command=self.final_page)  # Button for the user
        self.leave.place(x=900, y=10)  # Code for location


    def qna_setup(self):
        random_order()
        self.var1.set(0)
        self.question_label.config(text=self.qna[qnum][0])
        self.rb1.config(text=self.qna[qnum][1])
        self.rb2.config(text=self.qna[qnum][2])
        self.rb3.config(text=self.qna[qnum][3])
        self.rb4.config(text=self.qna[qnum][4])

    def score_mechanics(self):
        global score
        score_display = self.score_display
        choice = self.var1.get() #Gets what answer the user chose
        if len(asked) > 9: #To work out if it is the fianl question, so the final page can open
            if choice == self.qna[qnum][6]: #Checks if it is the right answer
               score += 1 #Increases the score by 1 point if question is answered correctly
               score_display.configure(text=score) #Changes the number on the score displayer
               self.confirm_button.config(text='Confirm') #Changes the confirm button's text back to confirm
               self.final_page() #To open final page after 10 questions, or user leaves
            else:
                score += 0 #If answered incorrectly, score does not change
                score_display.configure(text='The correct answer was: ' + self.qna[qnum][5]) #Lets the user know the right answer
                self.confirm_button.config(text='confirm') #Changes the confirm button's text back to confirm
        else:
            if choice == 0: #If no option selected
                self.confirm_button.config(text="Try Again, you didn't select an option") #Helps user diagnose the error
                choice = self.var1.get() #Gets what answer the user chose
            else:
                if choice == self.qna[qnum][6]: #Checks if it is the right answer
                    score += 1 #Increases the score by 1 point
                    score_display.configure(text=score) #Changes the number on the score displayer
                    self.confirm_button.config(text='confirm') #Changes the confirm button's text back to confirm
                    self.qna_setup() #Next question is asked
                else:
                    score += 0 #If answered incorrectly
                    score_display.configure(text='The correct answer was: ' + self.qna[qnum][5]) #Lets the user know the right answer
                    self.confirm_button.config(text='Confirmn') #Changes the confirm button's text back to confirm
                    self.qna_setup() #Next question is asked

    def final_page(self):
        window.destroy() #Destroys the window
        name = names[0]
        open_final_object = final()

class final:
   
    def __init__(self):
        background_color = 'deepskyblue1'  # Background color of the page
        global fwindow
        fwindow = Tk()
        fwindow.title('Exit Box')  # Window title
        fwindow.geometry('600x600')  # Window size

        self.final_frame = Frame(fwindow, width=700, height=600,
                                 bg=background_color)
        self.final_frame.grid(row=1)

        self.final_heading = Label(fwindow,
                                   text='Well done, you have completed the quiz '
                                   , font=('Tw Cen Mt', 22, 'bold'),
                                   bg=background_color)  # Code for main heading of the page
        self.final_heading.place(x=15, y=40)  # Location of the heading

        self.exit_button = Button(  # Code for the exit button
            fwindow,
            text='Exit',
            width=10,
            bg='red',
            font=('Tw Cen Mt', 12, 'bold'),
            command=self.close_final,
            )
        self.exit_button.place(x=260, y=200)  # Location of the button

        self.restart_label = Label(fwindow,
                                   text='Feel free to try again' +  str(names), #Adresses user by inputted username
                                   font=('Tw Cen Mt', 12, 'bold'),
                                   width=40, bg=background_color)  # Code for label to try again
        self.restart_label.place(x=110, y=80)  # Location of the label

        self.final_score = Label(fwindow, 
                                 text='Your final score is ' + str(score), #Tells user fianl score
                                 font=('Tw Cen Mt', 12,
                                 'bold'), width=40, bg=background_color)  # Code for quiz summary
        self.final_score.place(x=115, y=125)  # Location of the label


    def close_final(self):  # Destroys all the widgets
        self.final_frame.destroy()
        self.final_heading.destroy()
        self.exit_button.destroy()
        self.restart_label.destroy()
        fwindow.destroy()


# Code for image

if __name__ == '__main__':
    window = Tk()
    window.title('Car Quiz')
    window.geometry('600x600')
    bg_image = Image.open('car.jpg')
    bg_image = bg_image.resize((1000, 600), Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label = Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Quiz1(window)
    window.mainloop()
