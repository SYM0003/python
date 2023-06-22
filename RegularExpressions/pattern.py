import re
# uncomment block to see the result (don't uncomment muliple block in same execution)
# # block1(comment  line 8 to see the outuput for the patter of example1)
# # example 1
# pattern = re.compile('ab')

# # example 2
# pattern = re.compile('[ab]')
# matcher = pattern.finditer(input('Enter the string'))
# count = 0
# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')
#     count += 1
# print(f'No of "ab" in occurence of provided string :{count}')

# # block 3
# # in example 1 and 2 we were first we were creating the pattern
# # object an then created the matcher object for that pattern but
# # we can combine that two lines in a single line
# # sytanx
# # mathcher=re.finditer(pattern, string)

# matcher = re.finditer('[ab]', 'stwerfccacdfadfa')
# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')

# # block 4: if you want to find all patter except given pattern
# matcher = re.finditer('[^ab]', 'stwerfccacdfadfa')
# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')


# # block 5: search any lower case alphabate symbol in given string
# matcher = re.finditer('[a-z]', 'stwerfccaAcdfadfa')
# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')

# # block 6: search any upper case alphabate symbol in given string
# matcher = re.finditer('[A-Z]', 'stwerfccaAcdfadfa')
# for match in matcher:

# # block 7: search any alphabate symbol in given string
# matcher = re.finditer('[a-zA-Z]', 'stwDr2fcc4aAc6f8dfa')
# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')

# # block 8: search any digit from 0 to 9 in given string
# matcher = re.finditer('[0-9]', 'stwDr2fcc4aAc6f8dfa')
# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')

# # block 8: search any alphanumeric character in given string
# matcher = re.finditer('[0-9a-zA-Z]', 'stwDr2fcc4aAc6f8dfa')
# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')


# # block 9: search any character except alphanumeric character in given string
# matcher = re.finditer('[^0-9a-zA-Z]', 'stwDr2fcc4aAc@6f8dfa')
# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')



# # '\s'->predefined class for searching space in the given string
# # '\S'->predefined class for searching any character except space in the given string
# # '\d'->predefined class for searching digit in the given string
# # '\D'->predefined class for searching any charachter except digit in the given string
# # '\w'->predefined class for searching any alpha numeric character in the given string
# # '\W'->predefined class for searching any charachter excpet alpha numeric character in the given string(for special character)
# # '.'-> predefined class for searching any character in the given string



# # NOTE ->QUANTIFIERS:
# # we can use QUANTIFIERS to specify the number of occurence to match
# # a -->exactly one 'a'
# # a+ -->exactly one 'a'
# # a*--> any number of a include zero
# # a?--> atmost one a 
# # a{m}--> exatly m number of a
# # a{m,M}--> minimum m and maximum M occurenc of a

# matcher = re.finditer('a+','aaba,aaa')

# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')

# # output
# # 0...2...aa
# # 3...4...a
# # 5...8...aaa


# matcher = re.finditer('a*','aaba,aaa')

# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')

# # output
# # 0...2...aa
# # 2...2...
# # 3...4...a
# # 4...4...
# # 5...8...aaa
# # 8...8...


# matcher = re.finditer('a?','aaba,aaa')

# for match in matcher:
#     print(f'{match.start()}...{match.end()}...{match.group()}')

# # output
# # 0...1...a
# # 1...2...a
# # 2...2...
# # 3...4...a
# # 4...4...
# # 5...6...a
# # 6...7...a
# # 7...8...a
# # 8...8...



matcher = re.finditer('a{2}','aaba,aaa')

for match in matcher:
    print(f'{match.start()}...{match.end()}...{match.group()}')

# # output
# # 0...2...aa
# # 5...7...aa