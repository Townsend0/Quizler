from data import *

a = Quiz()
a.window()
a.right()
a.wrong()
a.writing_area()
a.get_questions()
a.write_question()
a.score()

def ans_true():
    if a.quiz[a.quest_no][1] == "True":
        a.area.config(bg = "green")
        a.score_up()
    else:
        a.area.config(bg = "red")
    a.next_question()

def ans_false():
    if a.quiz[a.quest_no][1] == "False":
        a.area.config(bg = "green")
        a.score_up()
    else:
        a.area.config(bg = "red")
    a.next_question()

a.o.config(command = ans_true)
a.x.config(command = ans_false)

a.screen.mainloop()