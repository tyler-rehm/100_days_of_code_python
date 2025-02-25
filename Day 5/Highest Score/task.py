from statistics import median, mean

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total = sum(student_scores)

sum_of_scores = 0

for score in student_scores:
    sum_of_scores += score

print(f"Total: {total} | {sum_of_scores}")

median = median(student_scores)
print(f"Median: {median}")

mean = int(mean(student_scores))
print(f"Median: {mean}")

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"Max: {max_score}")