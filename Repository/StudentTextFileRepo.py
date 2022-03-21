from Domain.student import Student
from Repository.studentRepo import StudentRepo


class StudentTextFileRepository(StudentRepo):
    def __init__(self, file_name='students.txt'):
        super().__init__()
        self._file_name = file_name
        self._load()

    def store(self, item):
        super().store(item)
        self._save()

    def delete(self, id_):
        book=super().delete(id_)
        self._save()
        return book

    def _save(self):
        f = open(self._file_name, 'wt')
        for student in self.student_list:
            line = str(student.student_id) + ';' + student.name + ';' + student.group
            f.write(line)
            f.write('\n')
        f.close()

    def _load(self):
        """
        Load data from file
        We assume file-saved data is valid
        """
        f = open(self._file_name, 'rt')  # read text
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split(';')
            super().store(Student(int(line[0]), line[1], line[2].strip('\n')))
