def tuples():
  #This is an empty tuple
  t1 = ()
  print("Empty tuple: ",t1)

  #This is a one item tuple
  t2 = (1,)
  print("\nOne item tuple: ",t2)

  # A four item tuple
  t3 = (0,'Ni',1.2,3)
  print("\nFour item tuple: ",t3)
  
  # A four item tuple -> initialised without brackets
  t4 = 0,'Ni',1.2,3
  print("\nFour item tuple(without brackets)  : ",t4)

  # Nested tuples
  t5 = ('abc', ('def', 'ghi') )
  print("\nNested tuple: ",t5)

  #Using the tuple keyword
  t6 = tuple('Okay')
  print("\nUsing 'tuple' keyword: ",t6)

  # Index, Index of Index, Slicing, Length
  print(f"\nAccessing using Index: {t4[2]}\nAccessing using Index of Index: {t5[0][1]}\nSlice: {t4[1:3]}\nLength: {len(t6)}")



def main():
  tuples()

main()