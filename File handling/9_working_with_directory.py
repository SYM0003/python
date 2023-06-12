import os

# # getcwd method                                                                                     
# # it returns the current working directory
# print(os.getcwd())

# # mkdir method
# os.mkdir('test_dir')#it will make a dir in cwd

# #creating dir in a path of cwd
# os.mkdir("test_Dir/test_subdir")
# os.mkdir("test_Dir/test_subdir/test_subdir2")

# creating dir at specified location
# os.mkdir('E:/test_dir')

# # # makedirs method
# # # os.makedirs(name)

# # create a dir 'new_dir' in cwd and 'new_dir2 in 'new_dir':
# os.makedirs('new_dir/new_dir2')

# # create a dir 'new_dir' in E and 'new_dir2 in 'new_dir':
# os.makedirs('E:/new_dir/new_dir2')

# # Note: if dir already exist it will give FileExistError



# # rmdir and removedirs method
# # to use remove any dir using this method the dir must be an empty dir
# # you can't remove a non-empty dir

# # cwd->File handling
# os.rmdir('test')#it will remove 'test' dir from cwd if present else FileNotFoundError
# os.rmdir('test_dir/test_subdir/test_subdir2') #will remove 'test_subdir2 that is present in test_dir/test_subdir


# os.removedirs('test_dir/test_subdir')# will remove both dirs of the path if they are empty






# #creating multipe dirs
# # 

# print(os.listdir('E:/'))#will give dir and files that are present inside of the E drive

# # the issue with listdir method is that we can find the dirs and files that exist in the 
# # given path but it doesn't give the dir and file that may present in the sub dirs of given path
# # the solution for this problem is walk method
# # it gives a generator object 
# # tree = os.walk('E:/shyam/programing/PYTHON/decorators')
# tree = os.walk('decorators')
# for x in tree:
#     print(x)




 
# # rename method 
# # syntax:
# os.rename(src, dst)

# # case 1:
# # cwd->PYTHON
# os.rename('leet_46.py','leet.py')# will rename leet_46.py by leet.py and leet.py will be in CWD ONLY.

# case 2:
# # cwd->PYTHON
# # NOTE
# os.rename('abc.txt', 'File handling\\abc2.txt')#will rename abc.txt by abc2.txt and the renamed file will moved in File handling dir


# # case 3:
# # cwd->PYTHON
# os.rename('File handling\\abc2.txt','abc.txt')#will rename abc2.txt by abc.txt of 'File handling' dir and the renamed file will moved to cwd dir


# # case 4
# # cwd ->PYTHON
# os.rename('File handling\\abc2.txt','File handling\\abc1.txt')#will rename abc1.txt by abc2.txt of 'File handling' dir and the renamed file will be in same dir

