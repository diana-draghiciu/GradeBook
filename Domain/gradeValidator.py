class GradeException(Exception):
    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return self._msg


class GradeValidationException(GradeException):
    def __init__(self, error_list):
        self._errors = error_list

    @property
    def errors(self):
        # Gives access to the list of errors
        return self._errors

    def __str__(self):
        # str representation
        result = ''
        for e in self.errors:
            result += e
            result += '\n'
        return result


class GradeValidator:
    @staticmethod
    def validate(grade):
        errors = []
        try:
            int(grade.student_id)
        except ValueError as va:
            errors.append("Input value for student id not an integer!")

        try:
            int(grade.lab_pb)
        except ValueError as va:
            errors.append("Input value for laboratory problem not an integer!")

        if grade.lab_pb < 1 or grade.lab_pb > 20:
            errors.append('Laboratory problem must be between 1 and 20.')

        try:
            int(grade.lab_nr)
        except ValueError as va:
            errors.append("Input value for laboratory no not an integer!")

        if grade.value is not None:
            try:
                int(grade.value)
            except ValueError as va:
                errors.append("Input value for grade not an integer!")

            if grade.value < 1 or grade.value > 10:
                errors.append('Grade must be between 1 and 10.')

        if len(errors) != 0:
            raise GradeValidationException(errors)
