import json
import os

# copy and paste the syllabus table completely in target.txt. 
# Refer sample.txt to check the text format. 
# ignore table heading
file1 = open("target.txt","r")

_list = file1.readlines()

len_lines = len(_list)
number_of_subjects = len_lines/4

data = []

for i in range(0, len_lines, 4):
    semester_number = int(_list[i].replace('\t',' ').replace('\n','').replace('--', '0'))
    type = _list[i+1].replace('\t',' ').split(' ')[:2]
    subject_name = _list[i+2].replace('\t',' ').replace('\n','')
    marks = [int(x) for x in _list[i+3].replace('\t',' ').replace('\n','').split(' ')]
    _dict={
            'semester': semester_number,
            'course_type': type[0],
            'subject_code': type[1],
            'subject_name': subject_name,
            'l': marks[0],
            't': marks[1],
            'p': marks[2],
            'c': marks[3],
            'cae': marks[4],
            'ese': marks[5]
    }
    data.append((_dict))

# Converting list to json
jsonString = json.dumps(data)

# Output filename has to be given here
filename = "SCHOOL/DEPT_BRANCH_REVISED_YY.json"

file2 = open(filename,"w")
file2.write(jsonString)

print(f'''File Generated: {filename}
Number of Subjects = {number_of_subjects}
Size of the generated file: {file2.seek(0, os.SEEK_END)} Bytes''')
