import shutil 
du = shutil.disk_usage("/")
print(du)
free = du.free/du.total*100
print(free)




