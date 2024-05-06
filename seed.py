import faker
from random import randint

from connect_db import session
from models import Groups, Students, Teachers, Subjects, Magazine

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 40
NUMBER_SUBJECTS = 5
NUMBER_TEACHERS = 4
NUMBER_RATING = 20


def generate_fake_data(number_groups, number_students, number_subjects, number_teachers, number_rating) -> tuple():

    fake_groups = []
    fake_students = []
    fake_subjects = []
    fake_teachers = []
    fake_rating = []

    fake_data = faker.Faker()

    for _ in range(number_groups):
        fake_groups.append(fake_data.company())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())
    
    for _ in  range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_rating):
        fake_rating.append(randint(1,5))

    return fake_groups, fake_students, fake_subjects, fake_teachers, fake_rating


def prepare_data(groups, students, subjects, teachers, rating):

    for_groups = []

    for group in groups :
        for_groups.append((group,))

    for_students =[]

    for student in students :
        for_students.append((student, randint(1,NUMBER_GROUPS)))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1,NUMBER_TEACHERS)))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_rating = []

    for student_id in range(1, NUMBER_STUDENTS + 1):

        for subject_id in range(1, NUMBER_SUBJECTS + 1):

            rating_list = [randint(1, 5) for _ in range(NUMBER_RATING)]
            for_rating.append((subject_id, student_id, rating_list))

    return for_groups, for_students, for_subjects, for_teachers, for_rating


def insert_data_to_db(groups, students, subjects, teachers, ratings):
    # Додаємо групи
    for group_data in groups:
        group = Groups(group_name=group_data[0])
        session.add(group)
    session.commit()

    # Додаємо вчителів
    for teacher_data in teachers:
        teacher = Teachers(teacher_name=teacher_data[0])
        session.add(teacher)
    session.commit()

    # Додаємо предмети, використовуючи вчителів, які вже збережені в базі даних
    for subject_data in subjects:
        subject = Subjects(subject_name=subject_data[0], teacher_id=subject_data[1])
        session.add(subject)
    session.commit()

    # Додаємо студентів, використовуючи групи, які вже збережені в базі даних
    for student_data in students:
        student = Students(student_name=student_data[0], group_id=student_data[1])
        session.add(student)
    session.commit()

    # Додаємо оцінки
    for rating in ratings:
        subject_id, student_id, scores = rating
        for score in scores:
            magazine = Magazine(subject_id=subject_id, student_id=student_id, rating=score)
            session.add(magazine)
    session.commit()


if __name__ == "__main__":
    groups, students, subjects, teachers, rating = prepare_data(*generate_fake_data(NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_TEACHERS,NUMBER_RATING))
    insert_data_to_db(groups, students, subjects, teachers, rating)

    