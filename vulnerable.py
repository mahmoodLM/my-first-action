import os
import sys

def ping_address():
    # استقبال عنوان IP أو مدخل من المستخدم
    user_input = sys.argv[1]
    
    # ثغرة أمنية: دمج مدخلات المستخدم مباشرة مع أمر النظام دون تنقية (CWE-78)
    os.system("ping -c 1 " + user_input)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ping_address()
