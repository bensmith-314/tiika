from pathlib import Path

directory = Path('everydays')

# List all files in the directory and sort them alphabetically by name
files = sorted([f for f in directory.iterdir() if f.is_file()])

# Remove .DS_Store
files = files[1:]

with open("imagePaths.txt", "w") as newFile:
    for file in files:
        newFile.write(f"<img src=\"{file}\">\n")