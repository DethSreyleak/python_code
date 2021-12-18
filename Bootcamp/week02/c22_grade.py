def grade(score):
   
    if score == 100:
        return "A"
    elif score > 91:
        return "A"
    elif score < 89:
        return "B"
    elif score > 80:
        return "B"
    elif score > 75:
        return "C"
    elif score > 66:
        return "D"
    elif score < 59:
        return "F"
    else:
        return "F"
student = int(input("Enter a number: "))
print(grade(student))