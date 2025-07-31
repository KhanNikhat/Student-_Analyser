# import turtle

# t = turtle.Turtle()
# t.speed(10)

# t.penup()
# t.goto(-60, -80)
# t.pendown()
# t.color("darkred")
# t.begin_fill()
# t.goto(-90, -180)
# t.goto(-60, -160)
# t.goto(-30, -180)
# t.goto(-60, -80)
# t.end_fill()

# t.penup()
# t.goto(60, -80)
# t.pendown()
# t.color("darkred")
# t.begin_fill()
# t.goto(30, -180)
# t.goto(60, -160)
# t.goto(90, -180)
# t.goto(60, -80)
# t.end_fill()

# t.penup()
# t.goto(0, -150)
# t.pendown()
# t.color("gold")
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# t.penup()
# t.goto(0, -130)
# t.pendown()
# t.color("goldenrod")
# t.begin_fill()
# t.circle(80)
# t.end_fill()

# t.hideturtle()
# turtle.done()









# import turtle

# check = turtle.Turtle()
# check.hideturtle()
# check.pensize(5)
# check.pencolor("green")
# check.speed(2)

# check.penup()
# check.goto(-20, 0)
# check.pendown()

# check.right(45)
# check.forward(30)

# check.left(90)
# check.forward(60)

# turtle.done()


import tkinter as tk
from tkinter import messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import turtle
students = []
class Student:
  def __init__(self, name, age, grade, math, science, english):
    self.name = name
    self.age = age
    self.grade = grade
    self.scores = {"Math": math, "Science": science, "English": english}
    self.average_score = sum(self.scores.values()) / len(self.scores)
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()
    math = float(entry_math.get())
    science = float(entry_science.get())
    english = float(entry_english.get())
    
    student = Student(name, age, grade, math, science, english)
    students.append(student)
    messagebox.showinfo("Success", f"Student {name} added successfully!")

    if student.average_score > 90:
        draw_medal()

def show_analytics():
    if not students:
        messagebox.showerror("Error", "No students added!")
        return
    data = pd.DataFrame([{"Name": s.name, "Age": s.age, "Grade": s.grade, "Math":s.scores["Math"],"Science": s.scores["Science"], "English": s.scores["English"],"Average Score": s.average_score} for s in students])
    avg_scores = data[["Math", "Science", "English"]].mean()
    messagebox.showinfo("Analytics", f"Average Scores:\n{avg_scores}")
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=data[["Math", "Science", "English"]])
    plt.title("Subject Performance Analysis")
    plt.show()

def export_data():
    if not students:
        messagebox.showerror("Error", "No students added!")
        return
    data = pd.DataFrame([{"Name": s.name, "Age": s.age, "Grade": s.grade, "Math":s.scores["Math"],"Science": s.scores["Science"], "English": s.scores["English"],"Average Score": s.average_score} for s in students])
    data.to_csv("student_data.csv", index=False)
    messagebox.showinfo("Export", "Student data saved to 'student_data.csv'")

def generate_summary():
    if not students:
        messagebox.showerror("Error", "No students added!")
        return
    data = pd.DataFrame([{"Name": s.name, "Age": s.age, "Grade": s.grade, "Math":s.scores["Math"],"Science": s.scores["Science"], "English": s.scores["English"],"Average Score": s.average_score} for s in students])

insights = [
    f"Highest Achiever: {data.loc[data['Average Score'].idxmax(), 'Name']}",
    f"Lowest Performer: {data.loc[data['Average Score'].idxmin(), 'Name']}",
    f"Average Performance Across Subjects:\n{data[['Math', 'Science','English']].mean()}",
    f"Subject with Highest Average Score: {data[['Math', 'Science','English']].mean().idxmax()}",
    f"Subject with Lowest Average Score: {data[['Math', 'Science','English']].mean().idxmin()}"
]
messagebox.showinfo("Summary Report", "\n".join(insights))

import threading
import turtle

def draw_medal():
    def turtle_task():
        screen = turtle.Screen()
        screen.title("Medal of Achievement")
        screen.bgcolor("lightblue")
        t = turtle.Turtle()
        t.speed(3)
        t.color("gold")
# Draw the medal
        t.penup()
        t.goto(-60, -80)
        t.pendown()
        t.color("darkred")
        t.begin_fill()
        t.goto(-90, -180)
        t.goto(-60, -160)
        t.goto(-30, -180)
        t.goto(-60, -80)
        t.end_fill()
        t.penup()
        t.goto(60, -80)
        t.pendown()
        t.color("darkred")
        t.begin_fill()
        t.goto(30, -180)
        t.goto(60, -160)
        t.goto(90, -180)
        t.goto(60, -80)
        t.end_fill()
        t.penup()
        t.goto(0, -150)
        t.pendown()
        t.color("gold")
        t.begin_fill()

        t.circle(100)
        t.end_fill()
        t.penup()
        t.goto(0, -130)
        t.pendown()
        t.color("goldenrod")
        t.begin_fill()
        t.circle(80)
        t.end_fill()
        t.hideturtle()
        turtle.done()
        t.penup()
        t.goto(-30, -70)
        t.pendown()
        t.write("Excellent!", font=("Arial", 14, "bold"))
        screen.mainloop()
    threading.Thread(target=turtle_task).start()

root = tk.Tk()
root.title("Student Performance Analyzer")
root.geometry("400x400")

tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Age").grid(row=1, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1)

tk.Label(root, text="Grade").grid(row=2, column=0)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1)

tk.Label(root, text="Math Score").grid(row=3, column=0)
entry_math = tk.Entry(root)
entry_math.grid(row=3, column=1)

tk.Label(root, text="Science Score").grid(row=4, column=0)
entry_science = tk.Entry(root)
entry_science.grid(row=4, column=1)

tk.Label(root, text="English Score").grid(row=5, column=0)
entry_english = tk.Entry(root)
entry_english.grid(row=5, column=1)

tk.Button(root, text="Add Student", command=add_student).grid(row=6, column=0)
tk.Button(root, text="Show Analytics", command=show_analytics).grid(row=6,
column=1)
tk.Button(root, text="Generate Summary",
command=generate_summary).grid(row=7, column=0)
tk.Button(root, text="Export Data", command=export_data).grid(row=7, column=1)

root.mainloop()
