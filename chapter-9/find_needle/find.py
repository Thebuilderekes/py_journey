import os

# Replace this with the path to your directory
DIRECTORY = "../find_needle/"
COUNT = 0
# loop through file names from 0.txt to 999.txt
for i in range(50):
    filename = os.path.join(DIRECTORY, f"{i}.txt")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
            if "needle" in contents:
                print(f"found the needle in file: {i}.txt")
                COUNT = COUNT + 1
    except exception as e:

        print(f"error reading {filename}: {e}")

print("there are", COUNT, "occurences of needle")
# TODO find all occurences of the "needle" and get the number of occurences
