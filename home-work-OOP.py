"""
А что могут делать лекторы? Получать оценки за лекции от студентов :)
Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале,
хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок).
Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
"""
class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}

  def add_courses(self, course_name):
      self.finished_courses.append(course_name)   


class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []


class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)

class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
    else:
        return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)