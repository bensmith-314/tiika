from pathlib import Path

directory = Path('../everydays_small')

# List all files in the directory and sort them alphabetically by name
files = sorted([f for f in directory.iterdir() if f.is_file()])

# Remove .DS_Store
files = files[1:]
files.reverse()

with open("imagePaths.txt", "w") as newFile:
    for file in files:
        newFile.write(f"<a href=\"/i/{str(file)[19:23]}.html\">\n\t<img src=\"/{file}\">\n</a>\n")
