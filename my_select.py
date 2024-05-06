from sqlalchemy import func, desc

from connect_db import session

from models import Groups, Students, Teachers, Subjects, Magazine


def select_1():

    query = session.query(Students.student_name, func.round(func.avg(Magazine.rating),2).label("avg_rating"))\
        .select_from(Magazine)\
        .join(Students)\
        .group_by(Students.student_id)\
        .order_by(desc("avg_rating"))\
        .limit(5).all()
    return query


def select_2():

    subject = input("Вкажіть назву предмета: ",    )

    query  = session.query(Students.student_name, func.round(func.avg(Magazine.rating), 2).label("avg_rating_subject")) \
        .join(Magazine).join(Subjects, Subjects.subject_id == Magazine.subject_id) \
        .filter(Subjects.subject_name == subject) \
        .group_by(Students.student_name) \
        .order_by(desc("avg_rating_subject")) \
        .first()
    return query


def select_3():

    subject = input("Вкажіть назву предмета: ",    )

    query =  session.query(Groups.group_name, func.round(func.avg(Magazine.rating), 2).label("avg_subjects_groups")) \
        .select_from(Magazine) \
        .join(Students).join(Groups).join(Subjects) \
        .filter(Subjects.subject_name == subject) \
        .group_by(Groups.group_name) \
        .order_by(desc("avg_subjects_groups"))\
        .all()

    return  query


def select_4():

    avg_rating_all =  session.query(func.round(func.avg(Magazine.rating), 2).label("avg_rating_all")).all()

    return  avg_rating_all


def select_5():

    teacher = input ("Вкажіть викладача: ", )

    query = session.query(Subjects.subject_name.label("search_subjects"))\
        .join(Teachers) \
        .filter(Teachers.teacher_name == teacher) \
        .all()
    
    return query

def select_6():

    group = input ("Вкажіть групу: ", )

    query = session.query(Students.student_name.label("students_group"))\
        .join(Groups) \
        .filter(Groups.group_name == group) \
        .all()
    
    return query

def select_7():

    group = input ("Вкажіть групу: ", )
    subject = input ("Вкажіть предмет: ", )

    query = session.query(Students.student_name, Magazine.rating) \
        .join(Groups).filter(Groups.group_name == group)\
        .join(Magazine).filter(Magazine.student_id == Students.student_id) \
        .join(Subjects).filter(Subjects.subject_name == subject)\
        .all()
    
    return query

def select_8():

    teacher = input ("Вкажіть викладача: ", )

    query = session.query(func.avg(Magazine.rating).label('average_rating')) \
        .select_from(Magazine) \
        .join(Students).join(Groups).join(Subjects).join(Teachers) \
        .filter(Teachers.teacher_name == teacher) \
        .group_by(Teachers.teacher_id) \
        .all()

    return query

def select_9():

    student = input ("Вкажіть студента: ", )

    query = session.query(Subjects.subject_name) \
        .distinct()\
        .join(Magazine, Subjects.subject_id == Magazine.subject_id) \
        .join(Students, Magazine.student_id == Students.student_id) \
        .filter(Students.student_name == student)\
        .all()
        
    return query

def select_10():

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

    result_1 = select_1()
    print(result_1)

    result_2 = select_2()
    print(result_2)

    result_3 = select_3()
    print(result_3)

    result_4 = select_4()
    print(result_4)

    result_5 = select_5()
    print(result_5)

    result_6 = select_6()
    print(result_6)

    result_7 = select_7()
    print(result_7)

    result_8 = select_8()
    print(result_8)

    result_9 = select_9()
    print(result_9)

    result_10 = select_10()
    print(result_10)

    