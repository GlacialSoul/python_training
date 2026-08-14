import csv

# with open("simple.txt", "w") as f:
#     f.write("Hii, everyone")
#     f.write("How are you")


with open("students_raw.csv", "r") as f:
    print(f.read())

def calculate_average(maths, science, english, social_science):
    return (maths+science + english + social_science)/4

with open("student_marks.csv") as f:
    reader = csv.DictReader(f)
    keys = ["roll_no","name","maths","science","english","social_science"]
    
    for line in reader:
        roll_no = line['roll_no']
        name = line['name']
        avg_marks = calculate_average(float('maths'), float('science'), float('english'), float('social_science'))
        # (float(line['maths']),float(line['science']), float(line['english']), float(line['social_science']))
        # students.append(line['name'])

with open('sample.csv', 'w') as outfile:
    outfile.write(roll_no)
    outfile.write(name)
    outfile.write(avg_marks)
    writer = csv.DictWriter(outfile)

    writer.writerow
    
