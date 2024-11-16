from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # مفتاح سري لتخزين الجلسات بشكل آمن

# بيانات الحسابات وكلمات السر
users = {
    'user1': 'password123',
    'user2': 'password456',
    'admin': 'admin123'
}

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['loggedIn'] = True  # حفظ حالة تسجيل الدخول في الجلسة
            return redirect(url_for('home'))  # الانتقال إلى الصفحة الرئيسية
        else:
            return 'اسم المستخدم أو كلمة المرور غير صحيحة'
    return render_template('login.html')

# الصفحة الرئيسية
@app.route('/')
def home():
    if 'loggedIn' not in session:  # التحقق من وجود حالة تسجيل الدخول في الجلسة
        return redirect(url_for('login'))  # إذا لم يكن المستخدم مسجلاً دخوله، يتم التوجيه إلى صفحة تسجيل الدخول
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
