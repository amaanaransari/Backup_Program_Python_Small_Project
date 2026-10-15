import os
import datetime
import shutil

def backup_file(source,destination):
    today = datetime.datetime.today().strftime("%Y-%m-%d_%H-%M-%S") #this last strtime is needed as windows doesnt support : so if you are on linux or mac you dont need str
    backup_file_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name, 'gztar', source)
    print("BackUp Completed Boss")

source = r"D:\App Data\Desktop\Python\veermala_python"
destination = r"D:\App Data\Desktop\Python\veermala_python\backups"

backup_file(source, destination)
