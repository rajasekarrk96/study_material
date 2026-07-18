import _08_excess_libaries.Data_Science_Libraries._01_basic_libaries._01_00_sample as e
e.go()
e.ok(5)
e.lol()
# _01_00_sample.go()

from _08_excess_libaries.Data_Science_Libraries._01_basic_libaries._01_00_sample import go
go()


from _08_excess_libaries.Data_Science_Libraries._01_basic_libaries._01_00_sample import lol,ok
print(lol())

from _08_excess_libaries.Data_Science_Libraries._01_basic_libaries._01_00_sample import *
go()

import  sys
print(sys.path)



print(dir(e))
print(e.__name__)

# running file will have name (main)
if __name__ == "__main__":
    print("cool")
#     rest of the fucntions
