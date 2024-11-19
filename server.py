from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # يمكن إضافة عملية التحقق هنا
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # مثال
            return redirect(url_for('main'))
        else:
            return 'خطأ في البيانات!'
    return render_template('login.html')

# الصفحة الرئيسية بعد تسجيل الدخول
@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
