# Create necessary variables
max = 0         # Max score found
students = {}   # Student dictionary
best = []       # Student List

# Open file for reading
try:
    file = open("Scores.txt", "r")
except:
    print("Error, file not found. Make sure the directory you run this from contains a \"Scores.txt\" file.")
    exit(1)

# Read each line and insert into students dictionary (Student:Score)
line = file.readline()
while line:
    list = line.split()
    # Check for duplicate names. Save only the highest score.
    if list[0] in students:
        list[1] = list[1] if students[list[0]] < int(list[1]) else students[list[0]]
    students[list[0]] = int(list[1])
    line = file.readline()

# Close file when finished
file.close()


# Iterate over students to find highest score
for score in students.values():
    if score > max:
        max = score

# Iterate over students to find all student names with the highest score
for student,score in students.items():
    if score==max:
        best.append(student)

# Output list of best students (highest score)
print(best)