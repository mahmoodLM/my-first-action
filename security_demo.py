# كود يحتوي على ثغرة أمنية خطيرة يكتشفها Bandit فوراً
def run_user_script(user_input):
    # استخدام دالة eval يُعد من أخطر الثغرات الأمنية (B307: eval)
    return eval(user_input)

# كلمة سر مكشوفة في الكود (B105: hardcoded_password_string)
DB_PASSWORD = "Hardcoded_Secret_Password_123"
