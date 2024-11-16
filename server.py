from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'user1' and password == 'password123':
            return redirect(url_for('home'))  # الانتقال إلى الصفحة الرئيسية إذا كانت البيانات صحيحة
        else:
            return 'اسم المستخدم أو كلمة المرور غير صحيحة'
    return render_template('login.html')

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


