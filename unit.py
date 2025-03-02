import os
import hashlib
import time

data_paths = ["C:\Program Files (x86)", "C:\Program Files",
              "C:\ProgramData", "C:\Windows"]

def scrape_data():
    data = []
    for path in data_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                data.append(os.path.join(root, file))
    return data

def grerate_log_name(data):
    return hashlib.sha256(data.encode()).hexdigest() + str(time.time())

def create_log_folder():
    return os.mkdir("C:/Users/endoc/ii")

def create_log_file(data):
    try:
        f = open(f"C:/Users/endoc/ii/{grerate_log_name(data[0])}", "w")
        for i in data:
            f.write(f"{i}\n")
        f.close()
    except FileExistsError as e:
        print(e)

def main():
    try:
        create_log_folder()
    except:
        print("Folder already exists")

    data = scrape_data()

    create_log_file(data)


if __name__ == "__main__":
    main()
