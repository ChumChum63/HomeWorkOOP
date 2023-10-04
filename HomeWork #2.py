class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecture_grade:
                lecturer.lecture_grade[course] += [grade]
            else:
                lecturer.lecture_grade[course] = [grade]
        else:
            return 'Ошибка'

    def avg_score(self):
        for num in self.grades.values():
            return sum(num) / len(num)
        if len(self.grades) == 0:
            return f"Нет оценок"

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_score()}\n"
                f"Курсы в процессе изучения: {','.join(self.courses_in_progress)}\nЗавершенные курсы: {','.join(self.finished_courses)}")


    def __lt__(self, other):
        return self.avg_score() < other.avg_score()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grade = {}

    def avg_score(self):
        for num in self.lecture_grade.values():
            return sum(num) / len(num)
        if len(self.lecture_grade) == 0:
            return f"Нет оценок"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_score()}"

    def __lt__(self, other):
        return self.avg_score() < other.avg_score()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Java']

bad_student = Student('Lyffi', 'Monkey D', 'your_gender')
bad_student.courses_in_progress += ['Java', 'Git']
bad_student.finished_courses += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git', 'Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Java', 9)

cool_reviewer.rate_hw(bad_student, 'Java', 3)
cool_reviewer.rate_hw(bad_student, 'Git', 5)

bad_reviewer = Reviewer('Big', 'Mama')
bad_reviewer.courses_attached += ['Python', 'Java']

bad_reviewer.rate_hw(best_student, 'Python', 8)
bad_reviewer.rate_hw(best_student, 'Java', 7)

bad_reviewer.rate_hw(bad_student, 'Java', 7)

cool_lecturer = Lecturer('Homer', 'Simpson')
cool_lecturer.courses_attached += ['Python', 'Git', 'Java']

best_student.rate_lecture(cool_lecturer, 'Python', 7)
best_student.rate_lecture(cool_lecturer, 'Git', 7)
best_student.rate_lecture(cool_lecturer, 'Java', 8)

bad_student.rate_lecture(cool_lecturer, 'Git', 7)
bad_student.rate_lecture(cool_lecturer, 'Java', 5)


bad_lecturer = Lecturer('Marge', 'Simpson')
bad_lecturer.courses_attached += ['Python', 'Java']

best_student.rate_lecture(bad_lecturer, 'Python', 5)
best_student.rate_lecture(bad_lecturer, 'Java', 3)

bad_student.rate_lecture(bad_lecturer, 'Java', 8)

all_students = [best_student, bad_student]
def avg_grade_students(all_students, course):
    all_grade = []
    if all_students:
        for students in all_students:
            for key, value in students.grades.items():
                if key == course:
                    all_grade += value
                return sum(all_grade) / len(all_grade)

all_lecture = [cool_lecturer, bad_lecturer]
def avg_grade_lecture(all_lecture, course):
    all_grade = []
    if all_lecture:
        for lectures in all_lecture:
            for key, value in lectures.lecture_grade.items():
                if key == course:
                    all_grade += value
                return sum(all_grade) / len(all_grade)

print(best_student.grades)
print(bad_student.grades)
print(cool_lecturer.lecture_grade)
print(bad_lecturer.lecture_grade)
print(best_student)
print(bad_student)
print(cool_lecturer)
print(bad_lecturer)
print(cool_reviewer)
print(bad_reviewer)
print(best_student < bad_student)
print(cool_lecturer > bad_lecturer)
print(avg_grade_students(all_students, 'Python'))
print(avg_grade_lecture(all_lecture, 'Python'))