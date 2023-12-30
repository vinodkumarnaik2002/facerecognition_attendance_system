import csv
import datetime
import os


current_date = datetime.datetime.now().strftime("%d:%m:%y")


file_name = f"{current_date}.csv"
if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='') as f:
        f.writelines(f'studentname,time,date')
else:
    print("File already exists.")

