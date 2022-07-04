from tkinter import *
import random
from PIL import Image, ImageTk

names = []
global questions_answers
asked =[]

questions_answers={
    1: [ "Which car company sold the most cars in 2020 worldwide?", 'Ford', 'Volkswagen', 'Toyota', 'Nissan', 'Toyota', 3 ], 
    2: [ "Which car company has the most accidents in 2020 worldwide?", 'Subaru', 'Toyota', 'Nissan', 'Honda', 'Subaru', 1 ], 
    3: [ "What car company is worth the most?", 'Toyota', 'Tesla', 'Ferrari', 'Lamborghini', 'Tesla', 2 ], 
}

def randomiser():
    global qnum
    qnum = random.randint(1,3)
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
        self.main_title.destroy()
        self.user_instruction.destroy()
        self.name_entry.destroy()
        self.start_button.destroy()
        Quiz(window)
    
class Quiz:

   def __init__(self, parent):
    background_color="deepskyblue1"

    randomiser()

    self.question_label=Label(window, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.place(x=50, y=50)  

    self.var1=IntVar()

    self.rb1 = Radiobutton(window, text = questions_answers[qnum][1], font=("Helvetica", "30"), bg="red", value=1, variable=self.var1)
    self.rb1.place(x=600, y=400)

    self.rb2 = Radiobutton(window, text = questions_answers[qnum][2], font=("Helvetica", "30"), bg="blue", value=2, variable=self.var1)
    self.rb2.place(x=200, y=400)

    self.rb3 = Radiobutton(window, text = questions_answers[qnum][3], font=("Helvetica", "30"), bg="yellow", value=3, variable=self.var1)
    self.rb3.place(x=600, y=200)

    self.rb4 = Radiobutton(window, text = questions_answers[qnum][4], font=("Helvetica", "30"), bg="limegreen", value=4, variable=self.var1)
    self.rb4.place(x=200, y=200)

    self.start_button = Button(window, text="Confrim",bg="forestgreen",command=self.quiz_counter)
    self.start_button.place(x=525, y=500)
    self.score_display  = Label(window, text =
                             'score')
    self.score_display.place(x=550, y=550)   
     
     
   def questions_setup(self):
     randomiser()
     self.var1.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.rb1.config(text=questions_answers[qnum][1])
     self.rb2.config(text=questions_answers[qnum][2])
     self.rb3.config(text=questions_answers[qnum][3])
     self.rb4.config(text=questions_answers[qnum][4])

 #Code for score
   def quiz_counter(self):
      global score
      score = 0
      scr_label=self.score_display
      choice=self.var1.get()
      if len(asked)>9:
        if choice == questions_answers[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.start_button.config(text="Confirm")
        else:
          score+=0
          scr_label.configure(text="The correct answer was: "+ questions_answers[qnum][5] )
          self.start_button.config(text="confirm")
     
      else:
            if choice==0:
              self.start_button.config(text="Try Again, you didn't select an option then submit again" )
              choice=self.var1.get()
            else:
              if choice == questions_answers[qnum][6]:
                score+=1
                scr_label.configure(text=score)
                self.start_button.config(text="confirm")
                self.questions_setup()
 
              else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5])
                  self.start_button.config(text="Confirmn")
                  self.questions_setup()
       

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