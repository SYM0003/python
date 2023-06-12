

# unzip file
from zipfile import *
f=ZipFile('zp.zip','r',ZIP_STORED)
# f.filelist #->list of zipped file in f with all info
# >>[<ZipInfo filename='abc.txt' compress_type=deflate filemode='-rw-rw-rw-' file_size=45 compress_size=37>,
#  <ZipInfo filename='abc2.txt' compress_type=deflate filemode='-rw-rw-rw-' file_size=27 compress_size=17>]

files=f.namelist() # will give list of all zipped file inside f
# # print(files)

for file in files:
    with open(file) as f:
        print(f.read())
        print('-'*50)
