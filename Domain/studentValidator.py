class StudentException(Exception):
    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return self._msg


class StudentValidationException(StudentException):
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


class StudentValidator:
    @staticmethod
    def validate(student):
        errors = []
        try:
            int(student.student_id)
        except ValueError as va:
            errors.append("Input value for student id not an integer!")

        try:
            isinstance(student.name,str)
        except ValueError as va:
            errors.append("Input value for student name not a string!")
        if student.name is None:
            errors.append("Student doesn't have a name!!")

        try:
            isinstance(student.group,str)
        except ValueError as va:
            errors.append("Input value for student group not a string!")
        if student.group is None:
            errors.append("Student doesn't have a group!!")

        if len(errors) != 0:
            raise StudentValidationException(errors)
