import os
import shutil
from datetime import datetime
def write_log(message):
    with open("file_log.txt", "a") as log:
        log.write(f"{datetime.now()} - {message}\n")
df=pd.read_csv("C:\Users\Hanumakshi\OneDrive\Desktop\Testfile")
trimport os

folder_path = input("Enter folder path: ")

try:
    if not os.path.exists(folder_path):
        raise FileNotFoundError("Folder does not exist!")

    print("Folder found!")

except Exception as e:
    print("Error:", e)
  for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
