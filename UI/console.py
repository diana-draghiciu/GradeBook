from Domain.student import Student
from Domain.studentValidator import StudentValidator


class UI:
    def __init__(self, student_srv, grade_srv, undo_srv):
        self._student_srv = student_srv
        self._grade_srv = grade_srv
        self._undo_srv=undo_srv

    def add_student(self):
        std_id = input("Give student id: ")
        std_name = input("Give student name: ")
        std_group = input("Give student group: ")
        StudentValidator.validate(Student(std_id, std_name, std_group))
        self._student_srv.add(Student(int(std_id), std_name, std_group))

    def remove_student(self):
        std_id = input("Give student id: ")
        self._student_srv.remove(int(std_id))

    def assign_lab_pb(self):
        std_id = input("Give student id: ")
        lab_no = input("Give the lab nr: ")
        lab_pb = input("Give the lab pb you desire to assign: ")
        self._student_srv.assignLab(int(std_id), int(lab_no), int(lab_pb))

    def assign_lab_gr(self):
        group_id = input("Give group id: ")
        lab_no = input("Give the lab nr: ")
        self._student_srv.assignLabToGroup(group_id, int(lab_no))

    def grade_student(self):
        id_ = input("Give student id: ")
        lab_no =input("Give laboratory no: ")
        value=input("Give grade value: ")
        self._grade_srv.grade(int(id_), int(lab_no), int(value))

    def list(self, list):
        for elem in list:
            print(str(elem))

    def students_ranking(self):
        group=input("Give group id: ")
        list=self._grade_srv.getStudentRanking(group)
        self.list(list)

    def failing_students(self):
        list= self._grade_srv.getFailingStudents()
        if len(list)!=0:
            self.list(list)
        else:
            print("No students are failing!")

    def undo(self):
        self._undo_srv.undo()

    def redo(self):
        self._undo_srv.redo()

    def list_students(self):
        self.list(self._student_srv._repo.student_list)

    def list_grades(self):
        self.list(self._grade_srv._repo.grade_list)

    @staticmethod
    def print_menu():
        print()
        print("1. Add a new student")
        print("2. Delete a student")
        print("3. Assign a lab pb")
        print("4. Assign to a group ")
        print("5. Grade a student")
        print("6. Display student ranking")
        print("7. Display failing students")
        print("8. Undo")
        print("9. Redo")
        print("10. Exit")
        print("11. List students")
        print("12. List grades")

    def start(self):
        command_dict = {"1": self.add_student, "2": self.remove_student, "3": self.assign_lab_pb, "4": self.assign_lab_gr, "5": self.grade_student, "6": self.students_ranking, "7": self.failing_students, "8": self.undo, "9": self.redo, "11": self.list_students, "12": self.list_grades}
        are_we_done_yet = False

        while not are_we_done_yet:
            try:
                self.print_menu()
                command = input('Enter command: ')

                if command == '10':
                    are_we_done_yet = True
                elif command not in command_dict:
                    print('Invalid command!')
                else:
                    command_dict[command]()
            except Exception as excep:
                print(excep)
