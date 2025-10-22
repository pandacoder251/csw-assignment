# Store scores
scores = [85, 90, 75, 60, 95, 70, 80]

# i. Average score
average = sum(scores) / len(scores)
print("Average score:", average)

# ii. Minimum and Maximum
print("Minimum score:", min(scores))
print("Maximum score:", max(scores))

# iii. Scores above average
above_avg = [score for score in scores if score > average]
print("Scores above average:", above_avg)

# iv. Sort descending
scores_desc = sorted(scores, reverse=True)
print("Scores in descending order:", scores_desc)

# v. Replace three lowest scores with 0
scores_sorted = sorted(scores)
scores_sorted[:3] = [0, 0, 0]
print("Scores after replacing three lowest with 0:", scores_sorted)
