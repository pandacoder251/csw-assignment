def top_student(student_scores):
    avg_scores = {student: sum(scores)/len(scores) for student, scores in student_scores.items()}
    top = max(avg_scores, key=avg_scores.get)
    return top

students = {"Ram":[85,90,92], "Laxman":[70,80,88], "Janaki":[95,100,90]}
print("Top student:", top_student(students))
