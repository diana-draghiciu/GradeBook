from Controller.UndoService import FunctionCall, Operation
from Domain.grade import Grade
from Domain.gradeValidator import GradeValidator


class GradeController:
    def __init__(self, grade_repo, student_repo, undo_srv):
        self._repo = grade_repo
        self._student_repo = student_repo
        self._undo_service = undo_srv

    def undo_grade(self, grade):
        grade.value=None

    def grade(self, id_, lab_no, new_grade,record_undo=True):
        for grade in self._repo.grade_list:
            if grade.student_id == id_ and grade.lab_nr == lab_no:
                GradeValidator.validate(Grade(id_, lab_no, grade.lab_pb, new_grade))
                grade.value = new_grade

                if record_undo:
                    undo = FunctionCall(self.undo_grade, grade, False)
                    redo = FunctionCall(self.grade, id_, lab_no, new_grade, False)
                    self._undo_service.record(Operation(undo, redo))
                break

    def averageGrade(self, student_id):
        average = 0
        nr = 0
        for grade in self._repo.grade_list:
            if grade.student_id == student_id:
                if grade.value!=None:
                    average = average + grade.value
                    nr += 1
        if nr==0:
            return 0
        return average / nr

    def getStudentRanking(self, group):
        new_list = []
        for student in self._student_repo.student_list:
            if student.group == group:
                new_list.append(student)

        return sorted(new_list, key=lambda x: self.averageGrade(x.student_id), reverse=True)

    def getFailingStudents(self):
        new_list = []
        for student in self._student_repo.student_list:
            aux=self.averageGrade(student.student_id)
            if aux < 5 and aux!=0:
                new_list.append(self._student_repo.find(student.student_id))
        return new_list