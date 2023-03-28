import sys
import re

# Check if a filename was provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide an input filename as a command line argument")
    exit()

# Prompt the user to enter the output filename
output_filename = input("Enter the output filename: ")

with open(sys.argv[1], "r", encoding='utf-8', errors='ignore') as f:
    file_contents = f.read()

file_contents_index = file_contents.index('RT89')
new_file_contents = file_contents[file_contents_index:]
new_file_contents = new_file_contents.replace("", "\t")
new_file_contents = new_file_contents.replace("", "??")
new_file_contents = new_file_contents.replace("", "?")
new_file_contents = new_file_contents.replace("", "&")

# Replace newline characters between p# and RT89 with a space
new_file_contents = re.sub(r'(?<=p#)(.*\n.*)(?=RT89)', lambda m: m.group(0).replace('\n', ''), new_file_contents)

# Split the new_file_contents by "p#" and join with "\n"
new_file_contents = "\n".join(new_file_contents.split("p#"))

# Split the new_file_contents into rows by "\n" and then into columns by "\t"
rows = [line.split("\t") for line in new_file_contents.split("\n")]

# Save the output as a tab-delimited text file
with open(output_filename, 'w', newline='') as f:
    for row in rows:
        f.write("\t".join(row))
        f.write("\n")

# Print a success message
print("Output saved to", output_filename)
