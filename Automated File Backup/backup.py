# 需要套件 pip install schedule
import os
import shutil
import datetime
import schedule
import time

source_dir = 'C:/Users/burnett/Desktop/test'
destination_dir = 'C:/Users/burnett/Desktop/backup'

def copy_folder_to_directory(source, dest):
  today = datetime.date.today()
  dest_dir = os.path.join(dest, str(today))

  try:
    shutil.copytree(source, dest_dir)
    print(f"folder copied to: {dest_dir}")
  except FileExistsError:
    print(f"Folder already exist in: {dest}")

# copy_folder_to_directory(source_dir, destination_dir)

# 每日固定時間備份
schedule.every().day.at('11:53').do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
  schedule.run_pending()
  time.sleep(60)