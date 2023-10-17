

# import os
import subprocess
subprocess.run(["cmd", "/c", "date"])

# subprocess.run(["date"]) is a linux command!



# print("HOME: " + os.environ.get("HOME", ""))
# print("SHELL: "+ os.environ.get("SHELL", ""))
# print("Fruit: " + os.environ.get("Fruit", ""))
# export fruit=Pineapple

import subprocess
subprocess.run(["cmd", "/c", "date"])

# subprocess.run(["date"]) is a linux command! 
# In windows, we are using the cmd shell to execute the date command. The /c flag is used to run the command and then terminate the cmd process.

from datetime import datetime

current_date_time = datetime.now()
print(current_date_time)

# This Python code will give you the current date and time.

16-10
