from django.db import models




class Position(models.Model):
    position_name = models.CharField(max_length=40)
    position_description = models.CharField(max_length=200)
    position_salary_range = models.CharField(max_length=40)
    is_trainer = models.BooleanField()

    def __str__(self):
        return f'Position (name: {self.position_name}, is training students: {self.is_trainer})'


class Employee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=40)
    employee_surname = models.CharField(max_length=40)
    employee_start_date = models.DateField()
    employee_PESEL = models.IntegerField()
    employee_phone_number = models.CharField(max_length=20)
    employee_address = models.CharField(max_length=100)
    employee_position = models.ManyToManyField(Position)
    position_salary = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return f'Employee (name: {self.employee_name}, {self.employee_surname}, position: {self.employee_position})'


class Yacht(models.Model):
    yacht_id = models.IntegerField()
    yacht_name = models.CharField(max_length=40)
    yacht_model = models.CharField(max_length=40)
    yacht_production_date = models.DateField()
    yacht_our_registration_date = models.DateField()
    yacht_length = models.IntegerField()
    yacht_max_crew = models.IntegerField()

    def __str__(self):
        return f'Yacht (name: {self.yacht_name},{self.yacht_model}  Produced: {self.yacht_production_date})'


class Course(models.Model):
    LANGUAGES = (
        ('PL', 'Polski'),
        ('EN', 'English'),
    )
    LOCATION = (
        ('IL', 'Inland waters'),
        ('OS', 'Open sea waters'),
    )
    course_id = models.IntegerField()
    course_price = models.DecimalField(decimal_places=2, max_digits=8)
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=200, default="Course description goes here")
    course_language = models.CharField(max_length=2, choices=LANGUAGES)
    course_location = models.CharField(max_length=2, choices=LOCATION)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    course_instructor = models.ManyToManyField(Employee)
    course_yachts_assigned = models.ManyToManyField(Yacht)

    def __str__(self):
        return f'Course (name: {self.course_name}, starting: {self.course_start_date})'


class Student(models.Model):
    student_id = models.IntegerField()
    course_attended = models.ManyToManyField(Course)
    student_name = models.CharField(max_length=40)
    student_surname = models.CharField(max_length=40)
    student_PESEL = models.IntegerField()
    student_phone_number = models.CharField(max_length=20)
    student_address = models.CharField(max_length=200)
    student_birth_date = models.DateField()
    student_amount_due = models.DecimalField(decimal_places=2, max_digits=8)

    def assign_course_due_value(self, amount):
        self.student_amount_due += amount
        return self.student_amount_due

    def __str__(self):
        return f'Student (name: {self.student_name},{self.student_surname}  course: {self.course_attended})'




