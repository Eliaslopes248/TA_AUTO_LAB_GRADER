#!/usr/bin/env python3
"""
Attendance Checker Script

This script reads students from my_students.csv and checks if they are present
in all_attendence.csv. It then writes the results to grades.csv with:
- first_name, last_name, grade
- Original grade if student was present
- Grade of 50 if student was absent
"""

import csv
import re



def read_full_attendance():
    try:
        FULL_SHEET = "./all_attendance.csv"
        result = []

        with open(FULL_SHEET, "r+", newline="") as file:
            openedFile = csv.reader(file)

            for line in openedFile:
                # Join in case multiple columns, then split on ANY whitespace
                raw_text = " ".join(line).strip()
                
                # Use regex to handle spaces, tabs, multiple whitespace
                content = re.split(r"\s+", raw_text)

                # Drop any empty strings
                content = [c.strip() for c in content if c.strip()]

                result.append(content)

        return result

    except Exception as e:
        print("Error:", e)

def read_students_to_grade():
    try:
        STUDENT_SHEET = "./my_students.csv"
        result = []

        with open(STUDENT_SHEET, "r+", newline="") as file:
            openedFile = csv.reader(file)

            for line in openedFile:
                # Join in case multiple columns, then split on ANY whitespace
                raw_text = " ".join(line).strip()
                
                # Use regex to handle spaces, tabs, multiple whitespace
                content = re.split(r"\s+", raw_text)

                # Drop any empty strings
                content = [c.strip() for c in content if c.strip()]

                # swap first and last name positions
                content[0],content[1] = content[1],content[0]
                result.append(content)

        return result

    except Exception as e:
        print("Error:", e)


def isPresent(student, attendance_sheet):
    for record in attendance_sheet:
        if (record[0] == student[0]) and (record[1] == student[1]):
            return True
    return False

def grade_students(attendance_sheet, myStudents):
    absent_count=0
    for student in myStudents:
        # ignore incomplete work
        if student[-1] == "0":
            continue

        # check if present
        present= isPresent(student, attendance_sheet)
        if not present:
            absent_count+=1
            student[-1] = '50'
            print("ABSENT:", student)
    print(f"{absent_count} Total found absent....")
    return myStudents

def write_grades(grades):
    GRADE_SHEET = "./grades.csv"
    try:
        with open(GRADE_SHEET,"w+") as file:
            file_writer= csv.writer(file)
            file_writer.writerows(grades)
    except Exception as e:
        print(e)

def main():
    attendance_sheet    = read_full_attendance()
    my_students         = read_students_to_grade()
    grades              = grade_students(attendance_sheet=attendance_sheet, myStudents=my_students)
    write_grades(grades)


# to run script in terminal write: bash run.sh
if __name__ == "__main__":
    main()

