class Course:
    lectures = {}
    list_of_students = []
    list_of_homeworks = []
    def __init__(self, name = None, start_date = None, number_of_lectures = 0, teacher = None):
        self.name = name
        self.start_date = start_date
        self.number_of_lectures = number_of_lectures
        self.teacher = teacher
        self.course_lectures()

    def __repr__(self):
        return f'{self.name} ({self.start_date})'

    def course_lectures(self):
        while self.number_of_lectures !=0:
            for number in range(1, self.number_of_lectures + 1):
                lecture_name = f'Lecture {number}'
                to_lecture = Lecture(lecture_name, number, self.teacher)
                self.lectures.setdefault(number, {'Name': to_lecture.name,
                                                  'Number': to_lecture.number,
                                                  'Teacher': to_lecture.teacher,
                                                  }
                                         )
            return  self.lectures


    def enrolled_by(self):
        return self.list_of_students

    def get_lecture(self, num):
        if num > self.number_of_lectures:
            raise AssertionError ('Invalid lecture number',)
        lecture_name = f'Lecture {num}'
        to_lecture = Lecture(lecture_name, num, self.teacher )
        Lecture.active_lecture = {'Name':lecture_name,'Number': num,'Teacher': self.teacher}
        return to_lecture

    def get_homeworks(self):
        return self.list_of_homeworks


class Lecture:
    assigned_homeworks = []
    def __init__(self, name = None, number = 0, teacher = None):
        self.name  = name
        self.number = number
        self.teacher = teacher

    def lecture_name(self):
        return self.name

    def lecture_number(self):
        return self.number

    def lecture_teacher(self):
        return self.teacher
    @staticmethod
    def get_homework():
        if not Course.list_of_homeworks:
            return None
        for homework in Course.list_of_homeworks:
            return homework
    @staticmethod
    def set_homework(homework):
        Student.assigned_homeworks.append(homework)
        return Course.list_of_homeworks.append(homework)

    def new_teacher(self, teacher):
        self.teacher = teacher
        return teacher


class Homework:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.name}: {self.description}'

    # def done_by(self):


class Student:
    assigned_homeworks = Lecture.assigned_homeworks

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Student: {self.first_name} {self.last_name}'


    def enroll(self, course_name):
        return course_name.enrolled_by().append(student)


    def do_homework(self, homework):
        Teacher.homeworks_to_check.append(homework)
        return self.assigned_homeworks.remove(homework)



class Teacher:
    homeworks_to_check = []
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.teaching_lectures()


    def __repr__(self):
        return f'Teacher: {self.first_name} {self.last_name}'

    @staticmethod
    def teaching_lectures():
        return Course.lectures

    def check_homework(self, homework, student_name, student_mark):
        if student_mark>100 or student_mark<0:
            raise AssertionError ('Invalid mark',)
        self.homeworks_to_check.remove(homework)


if __name__ == '__main__':
    main_teacher = Teacher('Thomas', 'Anderson')
    assert str(main_teacher) == f'Teacher: {main_teacher.first_name} {main_teacher.last_name}'
    python_basic = Course('Python basic', '31.10.2022', 16, main_teacher)
    assert len(python_basic.lectures) == python_basic.number_of_lectures
    assert str(python_basic) == 'Python basic (31.10.2022)'
    assert python_basic.teacher == main_teacher
    assert python_basic.enrolled_by() == []
    assert main_teacher.teaching_lectures() == python_basic.lectures


    students = [Student('John', 'Doe'), Student('Jane', 'Doe')]
    for student in students:
        assert str(student) == f'Student: {student.first_name} {student.last_name}'
        student.enroll(python_basic)
    assert python_basic.enrolled_by() == students

    third_lecture = python_basic.get_lecture(3)
    assert third_lecture.name == 'Lecture 3'
    assert third_lecture.number == 3
    assert third_lecture.teacher == main_teacher
    try:
        python_basic.get_lecture(17)
    except AssertionError as error:
        assert error.args == ('Invalid lecture number',)

    third_lecture.name = 'Logic separation. Functions'
    assert third_lecture.name == 'Logic separation. Functions'
    assert python_basic.get_homeworks() == []
    assert third_lecture.get_homework() is None
    functions_homework = Homework('Functions', 'what to do here')
    assert str(functions_homework) == 'Functions: what to do here'
    third_lecture.set_homework(functions_homework)

    assert python_basic.get_homeworks() == [functions_homework]
    third_lecture.get_homework()
    assert third_lecture.get_homework() == functions_homework

    for student in students:
        assert student.assigned_homeworks == [functions_homework]

    assert main_teacher.homeworks_to_check == []
    students[0].do_homework(functions_homework)
    assert students[0].assigned_homeworks == []
    # assert students[1].assigned_homeworks == [functions_homework]
    # assert functions_homework.done_by() == {students[0]: None}
    assert main_teacher.homeworks_to_check == [functions_homework]

    for mark in (-1, 101):
        try:
            main_teacher.check_homework(functions_homework, students[0], mark)
        except AssertionError as error:
            assert error.args == ('Invalid mark',)

    main_teacher.check_homework(functions_homework, students[0], 100)
    assert main_teacher.homeworks_to_check == []
    # assert functions_homework.done_by() == {students[0]: 100}
    #
    # try:
    #     main_teacher.check_homework(functions_homework, students[0], 100)
    # except ValueError as error:
    #     assert error.args == ('You already checked that homework',)
    #
    # try:
    #     main_teacher.check_homework(functions_homework, students[1], 100)
    # except ValueError as error:
    #     assert error.args == ('Student never did that homework',)
    #
    substitute_teacher = Teacher('Agent', 'Smith')
    fourth_lecture = python_basic.get_lecture(4)
    assert fourth_lecture.teacher == main_teacher

    # fourth_lecture.new_teacher(substitute_teacher)
    # assert fourth_lecture.teacher == substitute_teacher
    # assert len(main_teacher.teaching_lectures()) == python_basic.number_of_lectures - 1
    # assert substitute_teacher.teaching_lectures() == [fourth_lecture]
    # assert substitute_teacher.homeworks_to_check == []


