from flask import Flask, render_template, redirect, url_for, request, session
from models import db, Student, Admin
import os

# 初始化 Flask 应用
app = Flask(__name__)

# 配置数据库
app.secret_key = os.urandom(36)  # 用于加密会话
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/student_db'  # 替换为你的数据库配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 禁用 Flask-SQLAlchemy 的事件系统，避免警告

# 初始化数据库
db.init_app(app)

# 在应用启动时创建数据库表
with app.app_context():
    db.create_all()

# 路由：主页
@app.route('/')
def index():
    return render_template('index.html')

# 路由：登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        admin = db.session.query(Admin).filter(Admin.email == email).first()
        if admin is not None and admin.password == password:
            session['admin'] = admin.username
            return redirect(url_for('main'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

# 路由：注册页面
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取表单数据
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # 检查邮箱是否已经存在
        existing_admin = db.session.query(Admin).filter(Admin.email == email).first()
        if existing_admin:
            return "该邮箱已经注册！", 400
        
        # 创建新的管理员账号并保存到数据库
        new_admin = Admin(username=username, email=email, password=password)
        db.session.add(new_admin)
        db.session.commit()
        
        return redirect(url_for('login'))  # 注册成功后跳转到登录页面
    
    return render_template('register.html')  # GET 请求时渲染注册页面

# 路由：主页面
@app.route('/main')
def main():
    return render_template('main.html')

# 路由：学生信息录入
@app.route('/student_entry', methods=['GET', 'POST'])
def student_entry():
    if request.method == 'POST':
        name = request.form.get('name')
        student_id = request.form.get('student_id')
        volunteer_hours = request.form.get('volunteer_hours')
        ideological_education = request.form.get('ideological_education')
        cultural_participation = request.form.get('cultural_participation')
        score_1 = request.form.get('score_1')
        academic_activity = request.form.get('academic_activity')
        social_practice = request.form.get('social_practice')
        score_2 = request.form.get('score_2')
        awards = request.form.get('awards')
        score_3 = request.form.get('score_3')
        position = request.form.get('position')
        score_4 = request.form.get('score_4')
        total_score = int(score_1) + int(score_2) + int(score_3) + int(score_4)

        student = Student(
            name=name,
            student_id=student_id,
            volunteer_hours=volunteer_hours,
            ideological_education=ideological_education,
            cultural_participation=cultural_participation,
            score_1=score_1,
            academic_activity=academic_activity,
            social_practice=social_practice,
            score_2=score_2,
            awards=awards,
            score_3=score_3,
            position=position,
            score_4=score_4,
            total_score=total_score
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('main', message="学生信息录入成功"))
    return render_template('student_entry.html')

# 路由：学生信息查看
@app.route('/student_view')
def student_view():
    students = Student.query.order_by(Student.student_id).all()
    return render_template('student_view.html', students=students)

# 路由：管理员信息变更
@app.route('/admin_update', methods=['GET', 'POST'])
def admin_update():
    admin = Admin.query.first()  # 假设只有一个管理员
    if request.method == 'POST':
        admin.username = request.form['username']
        admin.email = request.form['email']
        admin.password = request.form['password']
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('admin_update.html', admin=admin)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
