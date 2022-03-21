class Student:
    def __init__(self, id_, name, group):
        self.__student_id = id_
        self.__name = name
        self.__group = group

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group

    def __str__(self):
        return str(self.student_id)+": "+self.name+", gr. "+self.group