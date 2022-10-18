import os

try:
    os.remove("python2.txt")
except FileNotFoundError:
    print("File already deleted")





