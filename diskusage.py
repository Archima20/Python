import shutil 
du = shutil.disk_usage("/")
print(du)
free = du.free/du.total*100
print(free)

import psutil
psutil.cpu_percent(0.1)

#little exercise 

