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

	def rate_lecturer(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
			if course in lecturer.grades:
				lecturer.grades[course] += [grade]
			else:
				lecturer.grades[course] = [grade]
		else:
			return 'Ошибка'

	def get_average_grades(self):
		total_grades = 0
		count = 0
		for grades in self.grades.values():
			total_grades += sum(grades)
			count += len(grades)
		if count != 0:
			self.average_grades = total_grades / count
		else:
			self.average_grades = 0
		return self.average_grades

	def __str__(self):
		self.get_average_grades()
		info = f'Имя: {self.name}\n' \
			f'Фамилия: {self.surname}\n' \
			f'Средняя оценка за домашние задания: {self.average_grades:.1f}\n' \
			f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
			f'Завершенные курсы: {", ".join(self.finished_courses)}'
		return info

	def __eq__(self, student):  # для равенства ==
		if not isinstance(student, Student):
			print(f'Не является студентом.')
		return self.get_average_grades() == student.get_average_grades()

	def __ne__(self, student):  # для неравенства !=
		if not isinstance(student, Student):
			print(f'Не является студентом.')
		return self.get_average_grades() != student.get_average_grades()

	def __lt__(self, student):  # для оператора меньше <
		if not isinstance(student, Student):
			print(f'Не является студентом.')
		return self.get_average_grades() < student.get_average_grades()


class Mentor:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
		self.courses_attached = []


class Lecturer(Mentor):
	def __init__(self, name, surname):
		super().__init__(name, surname)
		self.grades = {}
		self.average_grades = 0

	def get_average_grades(self):
		total_grades = 0
		count = 0
		for grades in self.grades.values():
			total_grades += sum(grades)
			count += len(grades)
		if count != 0:
			self.average_grades = total_grades / count
		else:
			self.average_grades = 0
		return self.average_grades

	def __str__(self):
		self.get_average_grades()
		info = f'Имя: {self.name}\n' \
			f'Фамилия: {self.surname}\n' \
			f'Средняя оценка за лекции: {self.average_grades:.1f}'
		return info

	def __eq__(self, lecturer):  # для равенства ==
		if not isinstance(lecturer, Lecturer):
			print(f'Не является студентом.')
		return self.get_average_grades() == lecturer.get_average_grades()

	def __ne__(self, lecturer):  # для неравенства !=
		if not isinstance(lecturer, Lecturer):
			print(f'Не является студентом.')
		return self.get_average_grades() != lecturer.get_average_grades()

	def __lt__(self, lecturer):  # для оператора меньше <
		if not isinstance(lecturer, Lecturer):
			print(f'Не является студентом.')
		return self.get_average_grades() < lecturer.get_average_grades()


class Reviewer(Mentor):
	def rate_hw(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'

	def __str__(self):
		info = f'Имя: {self.name}\nФамилия: {self.surname}'
		return info


student_id1 = Student('Ruoy', 'Eman', 'your_gender')
student_id1.courses_in_progress += ['Python']
student_id1.courses_in_progress += ['Git']
student_id1.finished_courses = ['Введение в програмирование']
student_id2 = Student('John', 'Doe', 'your_gender')
student_id2.courses_in_progress += ['C++']
student_id2.courses_in_progress += ['Git']
student_id2.finished_courses = ['Введение в програмирование', 'Python']

lecturer_id1 = Lecturer('Some', 'Buddy')
lecturer_id1.courses_attached += ['Python']
lecturer_id2 = Lecturer('Peter', 'Parker')
lecturer_id2.courses_attached += ['C++', 'Git']

reviewer_id1 = Reviewer('Some', 'Buddy')
reviewer_id1.courses_attached += ['Python']
reviewer_id2 = Reviewer('Peter', 'Parker')
reviewer_id2.courses_attached += ['C++', 'Git']

student_id1.rate_lecturer(lecturer_id1, 'Python', 9)
student_id1.rate_lecturer(lecturer_id1, 'Python', 8)
student_id1.rate_lecturer(lecturer_id2, 'Git', 9)
student_id1.rate_lecturer(lecturer_id2, 'Git', 10)
student_id2.rate_lecturer(lecturer_id2, 'C++', 10)
student_id2.rate_lecturer(lecturer_id2, 'C++', 7)
student_id2.rate_lecturer(lecturer_id2, 'Git', 9)
student_id2.rate_lecturer(lecturer_id2, 'Git', 10)

reviewer_id1.rate_hw(student_id1, 'Python', 7)
reviewer_id1.rate_hw(student_id1, 'Python', 10)
reviewer_id1.rate_hw(student_id2, 'Python', 9)
reviewer_id1.rate_hw(student_id2, 'Python', 10)

reviewer_id2.rate_hw(student_id1, 'Git', 7)
reviewer_id2.rate_hw(student_id1, 'Git', 9)
reviewer_id2.rate_hw(student_id2, 'C++', 7)
reviewer_id2.rate_hw(student_id2, 'C++', 9)
reviewer_id2.rate_hw(student_id2, 'Git', 9)
reviewer_id2.rate_hw(student_id2, 'Git', 10)

print(student_id1, student_id2, sep='\n')
print(student_id1 > student_id2)
print(lecturer_id1, lecturer_id2, sep='\n')
print(lecturer_id1 != lecturer_id2)
