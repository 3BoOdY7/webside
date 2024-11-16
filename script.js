// بيانات الدخول المتاحة في الكود (يمكنك تعديلها لاحقًا)
const validUsername = 'user1'; // اسم المستخدم الصحيح
const validPassword = 'password123'; // كلمة المرور الصحيحة

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    if (username === validUsername && password === validPassword) {
        // التوجيه إلى الصفحة الرئيسية
        window.location.href = 'index.html'; // أو إلى صفحة أخرى
    } else {
        // عرض رسالة خطأ
        document.getElementById('error').textContent = 'اسم المستخدم أو كلمة المرور غير صحيحة';
    }
}
