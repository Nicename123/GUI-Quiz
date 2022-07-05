from tkinter import *
import random
from PIL import Image, ImageTk

names = []
asked = []
score = 0



def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class Quiz1:
    
    def __init__(self,parent):
        background_color="lightgrey"
        
        self.main_title=Label(window, text="Car Quiz", font=("Times", "55","bold"),bg=background_color)
        self.main_title.place(x=520, y=100)
        
        self.var1=IntVar()

        self.user_instruction=Label(window, text="Please Enter Your Username Below:", font=("Times", "18","bold"),bg=background_color)
        self.user_instruction.place(x=450, y=300)

        self.name_entry=Entry(window)
        self.name_entry.place(x=600, y=400)

        self.start_button=Button(window, text="START", font=("Helvetica"," 13", "bold"),bg="forestgreen",command=self.name_collection)
        self.start_button.place(x=642, y=450)

    def name_collection(self):
        name=self.name_entry.get()
        names.append(name)
        print(names)
        self.main_title.destroy()
        self.user_instruction.destroy()
        self.name_entry.destroy()
        self.start_button.destroy()
        Quiz(window)


class Quiz:

   def __init__(self, parent):
       background_color="deepskyblue1"
       
       self.qna={
           1: [ 
               "Which car company sold the most cars in 2020 worldwide?",
               'Ford',
               'Mazda',
               'Toyota',
               'Nissan',
               'Toyota',
               3,
               ], 
           2: [ 
               "Which car company has the car model Portofino?",
               'Ferrari',
               'Lotus',
               'Porsche',
               'Skoda',
               'Ferrari',
               1,
               ], 
           3: [ 
               "What car company is worth the most?",
               'Toyota',
               'Tesla',
               'Ferrari',
               'Audi', 
               'Tesla',
               2,
               ], 
           4: [ 
               "Which f1 team has won the constrcutors championship of all time?",
               'Williams',
               'Mercedes',
               'Ferrari',
               'Red Bull', 
               'Ferrari',
               3,
               ], 
           5: [ 
               "How many cars are there in NZ (millions)?",
               '4.40',
               '5.30',
               '3.60',
               '4.20',
               '4.40',
               1,
               ], 
           6: [ 
               "Which is NOT a car company not owned by Volkswagen",
               'Audi',
               'Mercedes',
               'Porsche',
               'Bentley',
               'Mercedes',
               2,
               ],
           7: [ 
               "Which car company did Enzo Ferrari found?",
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
               "What year did NASCAR first start",
               '1950',
               '1949',
               '1953',
               '2016',
               '1949',
               2,
               ],
           10: [ 
               "Which famous Pixar movie released in 2006",
               'Toy Story',
               'Cars',
               'Brave',
               'Up',
               'Cars',
               2, 
               ],
            }
       
       
       randomiser()
       
       self.question_label=Label(window, text = self.qna[qnum][0], font =( "Tw Cen MT","18","bold"))
       self.question_label.place(x=50, y=50)  

       self.var1=IntVar()

       self.rb1 = Radiobutton(window, text = self.qna[qnum][1], font=("Helvetica", "30"), bg="red", value=1, variable=self.var1)
       self.rb1.place(x=600, y=400)

       self.rb2 = Radiobutton(window, text = self.qna[qnum][2], font=("Helvetica", "30"), bg="blue", value=2, variable=self.var1)
       self.rb2.place(x=200, y=400)

       self.rb3 = Radiobutton(window, text = self.qna[qnum][3], font=("Helvetica", "30"), bg="yellow", value=3, variable=self.var1)
       self.rb3.place(x=600, y=200)

       self.rb4 = Radiobutton(window, text = self.qna[qnum][4], font=("Helvetica", "30"), bg="limegreen", value=4, variable=self.var1)
       self.rb4.place(x=200, y=200)

       self.confirm_button = Button(window, text="Confrim",bg="forestgreen",command=self.quiz_score)
       self.confirm_button.place(x=525, y=500)
       self.score_display  = Label(window, text ='score')
       self.score_display.place(x=550, y=550)
    
       self.leave = Button(window, text='Leave', font=('Helvetica', '13', 'bold'), bg='red', command=self.final_page)
       self.leave.place(x=900, y=10)   
   
   def qna_setup(self):
       randomiser()
       self.var1.set(0)
       self.question_label.config(text=self.qna[qnum][0])
       self.rb1.config(text=self.qna[qnum][1])
       self.rb2.config(text=self.qna[qnum][2])
       self.rb3.config(text=self.qna[qnum][3])
       self.rb4.config(text=self.qna[qnum][4])
       
   def quiz_score(self):
       global score
       score_display = self.score_display
       choice = self.var1.get()
       if len(asked) > 9:
            if choice == self.qna[qnum][6]:
                score += 1
                score_display.configure(text=score)
                self.confirm_button.config(text='Confirm')
                self.final_page()
            else:
                score += 0
                score_display.configure(text='The correct answer was: '+ self.qna[qnum][5])
                self.confirm_button.config(text='confirm')
       else:
            if choice == 0:
                self.confirm_button.config(text="Try Again, you didn't select an option")
                choice = self.var1.get()
            else:
                if choice == self.qna[qnum][6]:
                    score += 1
                    score_display.configure(text=score)
                    self.confirm_button.config(text='confirm')
                    self.qna_setup()
                else:

                    score += 0
                    score_display.configure(text='The correct answer was: '+ self.qna[qnum][5])
                    self.confirm_button.config(text='Confirmn')
                    self.qna_setup()

   def final_page(self):
        window.destroy()
        name = names[0]

        open_end_object = end()


class end:

    def __init__(self):
        background_color = 'forrestgreen'
        global fwindow
        fwindow = Tk()
        fwindow.title('Exit Box')
        fwindow.geometry('700x600')

        self.end_frame = Frame(fwindow, width=700, height=600,
                               bg=background_color)
        self.end_frame.grid(row=1)

        self.end_heading = Label(fwindow,
                                 text='Well done, you have completed the quiz '
                                 , font=('Tw Cen Mt', 22, 'bold'),
                                 bg=background_color)
        self.end_heading.place(x=80, y=50)

        self.exit_button = Button(
            fwindow,
            text='Exit',
            width=10,
            bg='lightblue',
            font=('Tw Cen Mt', 12, 'bold'),
            command=self.close_end,
            )
        self.exit_button.place(x=260, y=200)

        self.list_label = Label(fwindow, text='Feel free to try again',
                                font=('Tw Cen Mt', 12, 'bold'),
                                width=40, bg=background_color)
        self.list_label.place(x=110, y=100)

    def close_end(self):
        self.end_frame.destroy()
        self.end_heading.destroy()
        self.exit_button.destroy()
        self.list_label.destroy()
        fwindow.destroy()
        
                

#Code for image
if __name__== "__main__":
    window = Tk()
    window.title("Car Quiz")
    window.geometry("600x600")
    bg_image = Image.open("car.jpg")
    bg_image = bg_image.resize((1000,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Quiz1(window)

    window.mainloop()