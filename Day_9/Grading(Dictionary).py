student_scores = {
    "luffy": 70,
    "zoro": 55,
    "sanji": 88,
    "ace": 82,
    "doflamingo": 100,
    "usopp": 75
}

grades = {}

for name in student_scores:
    score = student_scores[name]
    if score > 90:
        grades[name] = "Outsatnding"
    elif score > 80:
        grades[name] = "Exceeds Expectation"
    elif score > 70:
        grades[name] = "Acceptable"
    else:
        grades[name] = "Fail"

print(grades)
