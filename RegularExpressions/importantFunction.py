import re


# 1 compile()
# 2 finditer()
    

# # 3 match()-> to check the string start with the given pattern or not
#     # if mathch availabe than it will return mathc object else returns null

# # match=re.mathc('targetstring','pattern')
# matcher=re.match(input('enter target string\n'),input('enter pattern\n'))

# if matcher is not None:
#     print(f'target string doesn\'t start with the pattern')
# else:
#     print(f'target string start with the pattern')



# 4 fullmatch()->to check the the total target string matches with given pattern or not.,ss

matcher=re.fullmatch(input('enter target string\n'),input('enter pattern\n'))

if matcher is not None:
    print(f'target string doesn\'t match with the given pattern')
else:
    print(f'target string mathes with the pattern')

# 5 search()
# 6 findall()
# 8 sub()
# 9 subn()
# 10 split()

        # start()
        # end()
        # group()


    