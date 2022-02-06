import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
fileNames = glob.glob(pattern)
print(fileNames)

# TODO: use os.path.getsize to find each file's size
for file in fileNames:
    print(os.path.getsize(file))

# TODO: Add a test to only display files that are not zero length
for file in fileNames:
    if os.path.getsize(file) != 0:
        print(file)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
for file in fileNames:
    if os.path.getsize(file) != 0:
        print(os.path.basename(file))

