import os

#path do delete files from
DOWNLOAD_PATH = r"C:\Users\ashwi\downloads"

files = os.listdir(DOWNLOAD_PATH)

#files with these extensions will be removed
remove_exts = ["tmp", "part", "crdownload", "zip", "rar", "7z", "exe", "msi", "bat", "log", "bak", "old"]

#deleting the files with those extensions
for file in files:
    broken = file.split(".")
    ext = broken[-1]
    if ext in remove_exts:
        delete_path = DOWNLOAD_PATH + "\\" + file
        os.remove(delete_path)