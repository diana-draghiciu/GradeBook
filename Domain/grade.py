class Grade:
    def __init__(self, student_id, lab_nr, lab_pb, value):
        self.__student_id = student_id
        self.__lab_nr = lab_nr
        self.__lab_pb = lab_pb
        self.__value = value

    @property
    def student_id(self):
        return self.__student_id

    @property
    def lab_nr(self):
        return self.__lab_nr

    @lab_nr.setter
    def lab_nr(self, value):
        self.__lab_nr = value

    @property
    def lab_pb(self):
        return self.__lab_pb

    @lab_pb.setter
    def lab_pb(self, value):
        self.__lab_pb = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.student_id)+": "+str(self.__lab_nr)+", pb: "+str(self.lab_pb)+" grade: "+str(self.__value)
