import random
import pandas as pd
import string

def random_age_generator():
    return random.randint(6, 18)

def random_gender_generator():
    return random.choice(["Male", "Female"])

def random_grade_generator():
    return random.randint(0,100)

def random_name_generator():
    letters = string.ascii_lowercase
    first_name = ''.join(random.choice(letters) for _ in range(5)).capitalize()
    last_name = ''.join(random.choice(letters) for _ in range(5)).capitalize()
    return f"{first_name} {last_name}"

names = []
ages = []
genders = []
class1_grades = []
class2_grades = []
class3_grades = []
class4_grades = []
class5_grades = []

for _ in range (1000000):
    names.append(random_name_generator())
    ages.append(random_age_generator())
    genders.append(random_gender_generator())
    class1_grades.append(random_grade_generator())
    class2_grades.append(random_grade_generator())
    class3_grades.append(random_grade_generator())
    class4_grades.append(random_grade_generator())
    class5_grades.append(random_grade_generator())

students_df = pd.DataFrame({
    "Name": names,
    "Age": ages,
    "Gender": genders,
    "Class1": class1_grades,
    "Class2": class2_grades,
    "Class3": class3_grades,
    "Class4": class4_grades,
    "Class5": class5_grades,
})

students_df.to_csv("studentsfinalfr.csv", index=False)
print("success")


