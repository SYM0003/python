# wap to check whether file given file exist or not
import os
print(os.path.isfile('abc.txt'))



# wap to print the no of lines, no of charactars, no of words in a line

f=open('abc.txt')
lcnt=wcnt=ccnt=0

# for line in f.readlines:
for line in f:#internally imlimented as line 14
    lcnt+=1
    wcnt+=len(line.split())
    ccnt+=len(line)


print(f'lines in {f.name} : {lcnt}')
print(f'words in {f.name} : {wcnt}')
print(f'characters in {f.name} : {ccnt}')