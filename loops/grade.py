# get marks from 5 students and display the grade according to the mark
"""
if
    marks >= 75 -> A
    marks >= 65 -> B
    marks < 65 -> F
"""
count = 1
while (count <= 5):
    marks = int(input("Enter marks:"))
    if marks >= 75: 
        print("A")
    elif marks >= 65:
        print("B")
    else:
        print("F")

    count = count + 1       

