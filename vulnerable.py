import os
import sys

def run_system_command():
    # استقبال العنصر الأول من مدخلات المستخدم كـ String (Source)
    user_input = sys.argv[1]
    
    # ثغرة حقن الأوامر الصريحة (Sink: CWE-78)
    os.system("ping -c 1 " + user_input)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_system_command()
