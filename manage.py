from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    lynch = Professor(name='Lynch, Christopher Michael', department='Finance')
    sharma = Professor(name='Pratyush Nidhi Sharma', department='Accounting & MIS')
    gillespie = Professor(name='Gillespie, Jackson F ', department='Accounting')
    wang = Professor(name='Jiannan Wang', department='Accounting & MIS')
    course1 = Course(course_number= 'FINC 311', title='Principles of Finance', description='Introduces fundamental techniques and concepts related to the financial management of business firms. Topics include the time value of money, valuation, capital budgeting, working capital management, cost of capital, capital structure analysis, short and long term financing.', professor = lynch)
    course2 = Course(course_number='MISY 330', title='Database Design & Implementation', description='Learning data mining alogorithms and the SQL language.', professor = sharma)
    course3 = Course(course_number='ACCT 327', title='Cost Accounting', description='Process, job order and standard costing; variable and absorption costing; budgeting, decentralization, and transfer pricing; and cost analysis for managerial applications.', professor = gillespie)
    course4 = Course(course_number='MISY 350', title='Web Application Development', description='Fundamentals of web development, including Python and Flask.', professor = wang)
    db.session.add(lynch)
    db.session.add(sharma)
    db.session.add(gillespie)
    db.session.add(wang)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
