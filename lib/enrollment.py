from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        return len(self._enrollments)

    def get_enrolled_courses(self):
        courses = []
        for enrollment in self._enrollments:
            courses.append(enrollment.course)
        return courses

    def average_grade(self):
        total_grades = sum(enrollment.grade for enrollment in self._enrollments)
        num_courses = len(self._enrollments)
        average_grade = total_grades / num_courses
        return average_grade


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    def student_count(self):
        return len(self._enrollments)

    @classmethod
    def enrollment_count_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    def average_grade_per_course(self):
        grades_per_course = {}
        for enrollment in self.student.get_enrollments():
            course = enrollment.course
            grades_per_course[course] = grades_per_course.get(course, []) + [enrollment.grade]
        average_grades_per_course = {course: sum(grades) / len(grades) for course, grades in grades_per_course.items()}
        return average_grades_per_course