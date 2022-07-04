from tkinter import *
import random
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
        background_color="deepskyblue1"
        
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        
        self.main_title=Label(self.quiz_frame, text="Car Quiz", font=("Tw Cen MT", "18","bold"))
        self.main_title.grid(row=0, padx=20)
        
        self.var1=IntVar()

        self.user_instruction=Label(self.quiz_frame, text="Please Enter Your Username Below:", font=("Tw Cen MT", "18","bold"),bg=background_color)
        self.user_instruction.grid(row=1, padx=20, pady=20)

        self.name_entry=Entry(self.quiz_frame)
        self.name_entry.grid(row=2, padx=20, pady=20)

        self.start_button=Button(self.quiz_frame, text="Continue", font=("Helvetica"," 13", "bold"),bg="darkgrey",command=self.name_collection)
        self.start_button.grid(row=3, padx=20, pady=20)

    def name_collection(self):
        name=self.name_entry.get()
        names.append(name)
        self.quiz_frame.destroy()
        Quiz(root)
    
class Quiz:

   def __init__(self, parent):
    background_color="deepskyblue1"
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomiser()

    self.question_label=Label(self.quiz_frame, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold"))
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.var1=IntVar()

    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.rb4.grid(row=4, sticky=W)

    self.confirm_button = Button(self.quiz_frame, text="Confrim",bg="white")
    self.confirm_button.grid(row=6)
     
     
   def questions_setup(self):
     randomiser()
     self.varl.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.rb1.config(text=questions_answers[qnum][1])
     self.rb2.config(text=questions_answers[qnum][2])
     self.rb3.config(text=questions_answers[qnum][3])
     self.rb4.config(text=questions_answers[qnum][4])

       
if __name__ == "__main__":
  root = Tk()
  root.title("Car Quiz")
  quiz_instance = Quiz1(root)
  root.mainloop()