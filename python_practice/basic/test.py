nums = [2, 4, 6, 8, 10]

arr = [x for x in range(11) if x in nums]

# print(*arr, sep=', ')

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

even_mat = [x for row in mat for x in row if( x % 2 == 0 ) ]

print(*even_mat)



def getData(self, value):
  value = int(value)
  ans = -1  
  with open("/tmp/record/txt", "r") as filee:
    for line in filee:
      roll, section, marks = line.split(',')
      marks = int(marks)
      if( ans == -1 ):
        if( marks == value):
          ans = roll
      
  return ans

