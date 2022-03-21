"""
Write an application to help with the management of laboratory activities for a faculty course such as FP. Students
enrolled in the class can be assigned one of the 20problem statements(numbered from 1 to 20)from each laboratory, and
when they turn it in they are graded. The application will beused by the teacher and will provide the following
functionalities:-Add a student to the course. Each student has an id, a nameand a group. You cannot have more than
one student having the same id, as well as students without a name or group.-Remove a student from the course.
A student can only be removed while they have not received any grades.-Assign a laboratory problem statement to a
student. You cannot assign more than one problem statements from the same laboratory to a student. If the student was
already assigned a problem, the program must report the error.-Assign a laboratory to a group. Each student in the group
will be assigned a problem statement. Implement an algorithm to assign students with problem statements (e.g. each
subsequent student isassigned the next problem in the list of problem statements). In case a student was already
assigned a problem statement, this must not be changed!-Grade a student for a laboratory, with an integer grade 1
to 10.Validate that the grade is valid. Grades cannot be changed!-Best/worst students in a group. Given a group,
list its students in decreasing order of their average grade.-Students failing the class. Provide the list of all the
students (regardless of group), for whom the average grade is less than 5.-Undo/redo the last performed operation
that changes the list of students or grade assignments.

Data  is loadedand savedto  two  text  files:  “students.txt”,  “grades.txt”.  When  starting  the program, make sure
to have at least 10 students in the students file.
"""
from Controller.UndoService import UndoService
from Controller.gradeController import GradeController
from Controller.studentController import StudentController
from Repository.GradeTextFileRepo import GradeTextFileRepository
from Repository.StudentTextFileRepo import StudentTextFileRepository
from UI.console import UI

student_repo=StudentTextFileRepository()
grade_repo=GradeTextFileRepository()
undo_srv=UndoService()
student_srv=StudentController(student_repo,grade_repo,undo_srv)
grade_srv=GradeController(grade_repo,student_repo,undo_srv)
ui=UI(student_srv,grade_srv,undo_srv)
ui.start()