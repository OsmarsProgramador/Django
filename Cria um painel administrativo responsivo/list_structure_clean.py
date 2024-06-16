import os


def list_files(startpath, prefix=""):
    for item in sorted(os.listdir(startpath)):
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print(f"{prefix}├── {item}/")
            list_files(path, prefix + "│   ")
        else:
            print(f"{prefix}├── {item}")


print(".")
list_files(".")
