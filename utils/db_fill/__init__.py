from tareasbot import DB
from tareasbot.database.models import Course, NRC, User, Assignment
import csv


def fill_courses(file="courses.csv"):
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        line = 0
        for row in reader:
            if line > 0:
                course_dept = row[0]
                course_code = row[1]
                course_name = row[2]

                DB.add_course(course_dept, course_code, course_name)
                print(f"Added course: {course_name} ({course_dept} {course_code})")

            line += 1

        print(f"Read {line-1} lines")


