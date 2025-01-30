def sets():
  empty_set = set()
  fruits = {'apple', 'banana', 'grapes'}
  print("This is an empty set: ",empty_set)
  print("\nThis is a set with four elements: ",fruits)

  fruits.add('cherry')
  fruits.remove('apple')
  print("\nUpdated Set: ",fruits)

  s1= {1, 2, 3}
  s2 = {3, 4, 5}
  print("\nUnion: ", s1|s2 )
  print("\Intersection: ", s1&s2 )


def main():
  sets()