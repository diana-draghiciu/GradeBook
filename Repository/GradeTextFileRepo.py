from Domain.grade import Grade
from Repository.gradeRepo import GradeRepo


class GradeTextFileRepository(GradeRepo):
    def __init__(self, file_name='grades.txt'):
        super().__init__()
        self._file_name = file_name
        self._load()

    def store(self, item):
        super().store(item)
        self._save()

    def delete(self, id_):
        super().delete(id_)
        self._save()

    def _save(self):
        f = open(self._file_name, 'wt')
        for grade in self.grade_list:
            line = str(grade.student_id) + ';' + str(grade.lab_nr) + ';' + str(grade.lab_pb) + ';' + str(grade.value)
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
            value = line[3].strip('\n')
            if value != 'None':
                super().store(Grade(int(line[0]), int(line[1]), int(line[2]), int(value)))
            else:
                super().store(Grade(int(line[0]), int(line[1]), int(line[2]), None))
