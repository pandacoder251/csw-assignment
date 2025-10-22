students = [
    {"info": (101, "Ram"), "marks": [85,90,92], "skills": {"Python","Java"}},
    {"info": (102, "Laxman"), "marks": [70,80,88], "skills": {"C","Python"}},
    {"info": (103, "Janaki"), "marks": [95,100,90], "skills": {"Java","C++"}}
]

# a) Average marks per student
avg_marks = {student["info"][1]: sum(student["marks"])/len(student["marks"]) for student in students}
print("Average Marks:", avg_marks)

# b) Total skill frequency
from collections import Counter
all_skills = [skill for student in students for skill in student["skills"]]
skill_freq = dict(Counter(all_skills))
print("Skill Frequency:", skill_freq)

# c) Top-performing student
top_student = max(avg_marks, key=avg_marks.get)
print("Top-performing student:", top_student)
