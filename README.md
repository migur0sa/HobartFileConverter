# Hobart File Converter

Python Script that convert HT files from Hobart Scales to Tab Delimited

The way to use it is "python Converter_Tab.py FILENAME.ht" and it'll prompt you for a desired output file name.

This is an explanation of what the script is doing in case you need to modify it. 

1. The code first checks if a filename was provided as a command-line argument and prompts the user to enter the output filename.

2. It then reads the input file and processes its contents by removing unwanted characters and replacing them with the desired ones.

3. The re.sub() function is used to remove newline characters between p# and RT89.

4. The modified contents are split by "p#" and joined with newline characters, creating a new file content structure.

5. The new file content is split into rows and columns, effectively creating a table.

6. Finally, the output is saved as a tab-delimited text file with the specified output filename.

The result is a cleaned and formatted file that is easier to read and process. Enjoy 🚀

Later on I will upload a new script to pull ingredients out of the scale files.
