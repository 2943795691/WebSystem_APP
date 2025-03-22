from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'  # 指定表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    student_id = db.Column(db.String(100), unique=True, nullable=False)
    
    # 思想品德
    volunteer_hours = db.Column(db.Integer, nullable=True)
    ideological_education = db.Column(db.Integer, nullable=True)
    cultural_participation = db.Column(db.Integer, nullable=True)
    score_1 = db.Column(db.Integer, nullable=True)  # 总分1
    
    # 实践活动
    academic_activity = db.Column(db.Integer, nullable=True)
    social_practice = db.Column(db.Integer, nullable=True)
    score_2 = db.Column(db.Integer, nullable=True)  # 总分2
    
    # 荣誉奖项
    awards = db.Column(db.String(200), nullable=True)
    score_3 = db.Column(db.Integer, nullable=True)  # 总分3
    
    # 学生工作情况
    position = db.Column(db.String(100), nullable=True)
    score_4 = db.Column(db.Integer, nullable=True)  # 总分4
    
    # 学生总分
    total_score = db.Column(db.Integer, nullable=True)  # 总分

    def __init__(self, name, student_id, volunteer_hours, ideological_education, cultural_participation, score_1, academic_activity, social_practice, score_2, awards, score_3, position, score_4, total_score):
        self.name = name
        self.student_id = student_id
        self.volunteer_hours = volunteer_hours  
        self.ideological_education = ideological_education
        self.cultural_participation = cultural_participation
        self.score_1 = score_1
        self.academic_activity = academic_activity
        self.social_practice = social_practice
        self.score_2 = score_2
        self.awards = awards
        self.score_3 = score_3
        self.position = position
        self.score_4 = score_4
        self.total_score = total_score

    def __repr__(self):
        return '<Student %r>' % self.name

class Admin(db.Model):
    __tablename__ = 'admins'  # 指定表名
    username = db.Column(db.String(100), unique=True, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Admin %r>' % self.username
