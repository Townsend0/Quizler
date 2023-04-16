import tkinter
import requests
import html

class Quiz:

    def window(self):
        self.screen = tkinter.Tk()
        self.screen.config(bg = "#375362")
        self.screen.title("Quizler")
        self.screen.geometry("400x550")

    def right(self):
        self.o_img = tkinter.PhotoImage(file = "true.png",)
        self.o = tkinter.Button(image = self.o_img, highlightthickness = 0, activebackground = "green")
        self.o.place(x = 250, y = 425)

    def wrong(self):
        self.x_img = tkinter.PhotoImage(file = "false.png")
        self.x = tkinter.Button(image = self.x_img, highlightthickness = 0, activebackground = "red")
        self.x.place(x = 50, y = 425)

    def writing_area(self):
        self.area = tkinter.Canvas(width = 350, height = 300)
        self.area.pack(pady = 75)

    def score(self):
        self.count = self.quest_no = 0
        self.score = tkinter.Label(text = f"Score: {self.count}/{self.quest_no + 1}", fg = "white", bg = "#375362")
        self.score.config(font = ("courier", 15, "normal"))
        self.score.place(x = 200, y =35)

    def write_question(self):
        self.current_quest = self.area.create_text(175, 150, font = ("normal", 15, "normal"), width = 300, text = self.quiz[0][0])

    def next_question(self):
        def change():
            self.area.config(bg = "white")
            self.quest_no += 1
            if self.quest_no == 10:
                self.area.itemconfig(self.current_quest, text = f"The game ended")
                self.x.config(state = "disabled")
                self.o.config(state = "disabled")
            else:
                self.area.itemconfig(self.current_quest, text = self.quiz[self.quest_no][0])
                self.score.config(text = f"Score: {self.count}/{self.quest_no + 1}")
        self.area.after(250, change)

    def get_questions(self):
        self.dict = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
        self.dict.status_code
        self.quiz = [[ html.unescape(self.dict.json()["results"][a]["question"]), html.unescape(self.dict.json()["results"][a]["correct_answer"])] for a in range(10)]

    def score_up(self):
        self.count += 1
        self.score.config(text = f"Score: {self.count}/{self.quest_no + 1}")
        
        