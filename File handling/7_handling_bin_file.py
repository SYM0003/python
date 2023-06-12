# # handling binary files
# f=open('1.jpeg','rb')
# x=open('2.jpeg','wb')
# x.write(f.read())


# # handling csv file(xl)
# # csc->comma seprated values
# # writing in csv file
# import csv
# f=open('data.csv','w',newline='')
# w=csv.writer(f)
# w.writerow(['name','rollno','dob'])
# # w.writerow(['name','rollno','dob'])
# w.writerows([['shyam','35','3'],['vishal','23','3']])


# # reding data from csv file
# import csv
# f=open('data.csv','r')
# r=csv.reader(f)
# x=list(r)
# for nm,rn,db in x:
#     print(f'{nm}\t {rn}\t {db}')




# # handling zip files
# # zip files
# from zipfile import *

# f=ZipFile('zp.zip','w',ZIP_DEFLATED)
# f.write('abc.txt')
# f.write('abc2.txt')
# f.close



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
