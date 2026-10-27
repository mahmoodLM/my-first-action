import os
import sys

# التأكد من وجود مدخل نصي صريح من المستخدم (sys.argv[1] is a string)
if len(sys.argv) > 1:
    user_input = sys.argv[1]
    
    # ثغرة حقن الأوامر الصريحة (Command Injection - CWE-78)
    os.system("ping -c 1 " + user_input)
