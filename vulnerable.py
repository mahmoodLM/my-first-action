import os
import sys

# استقبال مدخلات المستخدم الصريحة (Source)
user_command = sys.argv[1]

# تنفيذ أمر النظام المباشر دون تنقية (Sink: Command Injection)
os.system("ls -la " + user_command)
