Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> courses = {
...     "CSC101",
...     "CSC102",
...     "CSC103",
...     "NET110",
...     "COM241", }
>>> course_room_numbers = {
...     "CSC101": "3004",
...     "CSC102": "4501",
...     "CSC103": "6755",
...     "NET110": "1244",
...     "COM241": "1411", }
>>> course_instructors = {
...     "CSC101": "Haynes",
...     "CSC102": "Alvarado",
...     "CSC103": "Rich",
...     "NET110": "Burke",
...     "COM241": "Lee", }
>>> course_meeting_times = {
...     "CSC101": "8:00 a.m.",
...     "CSC102": "9:00 a.m.",
...     "CSC103": "10:00 a.m.",
...     "NET110": "11:00 a.m.",
...     "COM241": "1:00 p.m.", }
>>> def print_course_details(course_room_numbers, course_instructors, course_meeting_times):
...     print("Course Details:\n")
...     for course in course_room_numbers:
...         print(f"Course Number: {course}")
...         print(f"Room Number: {course_room_numbers[course]}")
...         print(f"Instructor: {course_instructors.get(course, 'No instructor assigned')}")
...         print(f"Meeting Time: {course_meeting_times.get(course, 'No meeting time assigned')}\n")
... 
...         
>>> print_course_details(course_room_numbers, course_instructors, course_meeting_times)
Course Details:

Course Number: CSC101
Room Number: 3004
Instructor: Haynes
Meeting Time: 8:00 a.m.

Course Number: CSC102
Room Number: 4501
Instructor: Alvarado
Meeting Time: 9:00 a.m.

Course Number: CSC103
Room Number: 6755
Instructor: Rich
Meeting Time: 10:00 a.m.

Course Number: NET110
Room Number: 1244
Instructor: Burke
Meeting Time: 11:00 a.m.

Course Number: COM241
Room Number: 1411
Instructor: Lee
Meeting Time: 1:00 p.m.

