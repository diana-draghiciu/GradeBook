from Controller.UndoService import FunctionCall, Operation, CascadedOperation
from Domain.grade import Grade
from Domain.gradeValidator import GradeValidator


class StudentController:
    def __init__(self, student_repo, grade_repo, undo_srv):
        self._repo = student_repo
        self._grade_repo = grade_repo
        self._undo_service = undo_srv

    def add(self, student, record_undo=True):
        self._repo.store(student)
        if record_undo:
            undo = FunctionCall(self.remove, student.student_id, False)
            redo = FunctionCall(self.add, student, False)
            self._undo_service.record(Operation(undo, redo))

    def remove(self, student_id, record_undo=True):
        student = self._repo.find(student_id)
        can_delete=True
        if student is not None:
            for grade in self._grade_repo.grade_list:
                if grade.student_id == student_id and grade.value is not None:
                    can_delete=False
                    break
        if can_delete:
            self._repo.delete(student_id)
            if record_undo:
                undo = FunctionCall(self.add, student, False)
                redo = FunctionCall(self.remove, student_id, False)
                self._undo_service.record(Operation(undo, redo))


    def assignLab(self, id_, lab_no, lab_pb, record_undo=True):
        for grade in self._grade_repo.grade_list:
            if grade.student_id == id_ and grade.lab_nr == lab_no:
                raise Exception("Laboratory problem already assigned!")

        grade=Grade(id_, lab_no, lab_pb, None)
        GradeValidator.validate(grade)
        self._grade_repo.store(grade)
        if record_undo:
            undo = FunctionCall(self._grade_repo.delete, id_)
            redo = FunctionCall(self.assignLab, id_, lab_no, lab_pb, False)
            self._undo_service.record(Operation(undo, redo))

    def assignLabToGroup(self, group_id, lab_no, record_undo=True):
        lab_pb = 1
        new_list = []
        for student in self._repo.student_list:
            if student.group == group_id:
                self.assignLab(student.student_id, lab_no, lab_pb, False)
                new_list.append(Grade(student.student_id, lab_no, lab_pb, None))
                lab_pb += 1

        if record_undo:
            # Record for cascaded undo/redo
            cascade_list = []
            for elem in new_list:
                undo = FunctionCall(self._grade_repo.delete, elem.student_id)
                redo = FunctionCall(self.assignLab, elem.student_id, elem.lab_nr, elem.lab_pb, False)
                cascade_list.append(Operation(undo, redo))

            cop = CascadedOperation(*cascade_list)
            self._undo_service.record(cop)
