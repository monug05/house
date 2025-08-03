import gdown
import os

file_id = "1sVTPyfr-4HSMK7QlUyR5igMbLvR8tE_A"
url = f"https://drive.google.com/uc?id={file_id}"

destination = "model.pkl"
if not os.path.exists(destination):
    gdown.download(url, destination, quiet=False)
else:
    print("model.pkl already exists.")
