from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # منطق التحقق
        if username != 'admin' or password != 'password':
            error = 'اسم المستخدم أو كلمة المرور غير صحيحة'
        else:
            return "تم تسجيل الدخول بنجاح"
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
