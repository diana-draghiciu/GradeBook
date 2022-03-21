class StudentRepo:
    def __init__(self):
        self.__student_list = []

    @property
    def student_list(self):
        return self.__student_list

    @student_list.setter
    def student_list(self, index, value):
        self.__student_list[index] = value

    def getAll(self):
        return self.__student_list

    def find(self, student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                return student
        return None

    def store(self, student):
        """
        Adds the new student to the list of students
        :param student:
        :return:
        """
        std = self.find(student.student_id)
        if std is None:
            self.student_list.append(student)
        else:
            raise ValueError("Student id already in list!")

    def delete(self, student_id):
        student = self.find(student_id)
        self.student_list.remove(student)

