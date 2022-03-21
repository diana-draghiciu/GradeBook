from Domain.gradeValidator import GradeValidator


class GradeRepo:
    def __init__(self):
        self.__grade_list = []

    @property
    def grade_list(self):
        return self.__grade_list

    def store(self, grade):
        GradeValidator.validate(grade)
        self.__grade_list.append(grade)
        return grade

    def delete(self, id_):
        for grade in self.__grade_list:
            if grade.student_id==id_:
                self.__grade_list.remove(grade)
                break