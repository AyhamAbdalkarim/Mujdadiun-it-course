score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C or below"

print(grade)

# shorthand ternary
status = "pass" if score >= 50 else "fail"
print(status)
