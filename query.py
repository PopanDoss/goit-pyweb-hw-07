from sqlalchemy import func, desc

from connect_db import session

from models import Groups, Students, Teachers, Subjects, Magazine


def query_1_avg_rating():

    query = session.query(Students.student_name, func.round(func.avg(Magazine.rating),2).label("avg_rating"))\
        .select_from(Magazine)\
        .join(Students)\
        .group_by(Students.student_id)\
        .order_by(desc("avg_rating"))\
        .limit(5).all()
    return query


def query_2_avg_rating_subject():

    subject = input("Вкажіть назву предмета: ",    )

    query  = session.query(Students.student_name, func.round(func.avg(Magazine.rating), 2).label("avg_rating_subject")) \
        .join(Magazine).join(Subjects, Subjects.subject_id == Magazine.subject_id) \
        .filter(Subjects.subject_name == subject) \
        .group_by(Students.student_name) \
        .order_by(desc("avg_rating_subject")) \
        .first()
    return query


def query_3_avg_rating_subjects_groups():

    subject = input("Вкажіть назву предмета: ",    )

    query =  session.query(Groups.group_name, func.round(func.avg(Magazine.rating), 2).label("avg_subjects_groups")) \
        .select_from(Magazine) \
        .join(Students).join(Groups).join(Subjects) \
        .filter(Subjects.subject_name == subject) \
        .group_by(Groups.group_name) \
        .order_by(desc("avg_subjects_groups"))\
        .all()

    return  query


def query_4_avg_rating_all():

    avg_rating_all =  session.query(func.round(func.avg(Magazine.rating), 2).label("avg_rating_all")).all()

    return  avg_rating_all


def query_5_search_subjects_teacher():

    teacher = input ("Вкажіть викладача: ", )

    query = session.query(Subjects.subject_name.label("search_subjects"))\
        .join(Teachers) \
        .filter(Teachers.teacher_name == teacher) \
        .all()
    
    return query

def query_6_search_students_group():

    group = input ("Вкажіть групу: ", )

    query = session.query(Students.student_name.label("students_group"))\
        .join(Groups) \
        .filter(Groups.group_name == group) \
        .all()
    
    return query

def query_7_search_rating_group_subject():

    group = input ("Вкажіть групу: ", )
    subject = input ("Вкажіть предмет: ", )

    query = session.query(Students.student_name, Magazine.rating) \
        .join(Groups).filter(Groups.group_name == group)\
        .join(Magazine).filter(Magazine.student_id == Students.student_id) \
        .join(Subjects).filter(Subjects.subject_name == subject)\
        .all()
    
    return query

def query_8_avg_rating_teacher():

    teacher = input ("Вкажіть викладача: ", )

    query = session.query(func.avg(Magazine.rating).label('average_rating')) \
        .select_from(Magazine) \
        .join(Students).join(Groups).join(Subjects).join(Teachers) \
        .filter(Teachers.teacher_name == teacher) \
        .group_by(Teachers.teacher_id) \
        .all()

    return query

def query_9_student_subjects():

    student = input ("Вкажіть студента: ", )

    query = session.query(Subjects.subject_name) \
        .distinct()\
        .join(Magazine, Subjects.subject_id == Magazine.subject_id) \
        .join(Students, Magazine.student_id == Students.student_id) \
        .filter(Students.student_name == student)\
        .all()
        
    return query

def query_10_student_subjects_teacher():

    student = input("Вкажіть студента: ")
    teacher = input("Вкажіть викладача: ")

    query = session.query(Subjects.subject_name) \
        .join(Magazine, Magazine.subject_id == Subjects.subject_id) \
        .join(Students, Students.student_id == Magazine.student_id) \
        .join(Teachers, Teachers.teacher_id == Subjects.teacher_id) \
        .filter(Students.student_name == student) \
        .filter(Teachers.teacher_name == teacher) \
        .distinct() \
        .all()
    
    return query


if __name__=="__main__":

    result_1 = query_1_avg_rating()
    print(result_1)

    result_2 = query_2_avg_rating_subject()
    print(result_2)

    result_3 = query_3_avg_rating_subjects_groups()
    print(result_3)

    result_4 = query_4_avg_rating_all()
    print(result_4)

    result_5 = query_5_search_subjects_teacher()
    print(result_5)

    result_6 = query_6_search_students_group()
    print(result_6)

    result_7 = query_7_search_rating_group_subject()
    print(result_7)

    result_8 = query_8_avg_rating_teacher()
    print(result_8)

    result_9 = query_9_student_subjects()
    print(result_9)

    result_10 = query_10_student_subjects_teacher()
    print(result_10)

    