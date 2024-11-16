// قائمة الحسابات المسموح بها
const accounts = [
    { username: "user1", password: "password1" },
    { username: "user2", password: "password2" },
    { username: "admin", password: "admin123" }
];

// وظيفة تسجيل الدخول
function login() {
    const usernameInput = document.getElementById("username").value;
    const passwordInput = document.getElementById("password").value;
    const errorElement = document.getElementById("error");

    // البحث عن الحساب في القائمة
    const account = accounts.find(acc => acc.username === usernameInput && acc.password === passwordInput);

    if (account) {
        // تسجيل الدخول ناجح - الانتقال إلى الصفحة الرئيسية
        window.location.href = "main.html";
    } else {
        // عرض رسالة خطأ
        errorElement.textContent = "عذرا حسابك غير مسجل في المنصة الرجاء التحقق واعادة المحاولة";
    }
}
