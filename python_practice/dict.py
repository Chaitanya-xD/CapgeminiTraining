def dicts():

  #This is an empty dicitonary
  d1 = {}
  print("This is an empty dictionary: ",d1)

  #This is a dictionary with 2 key-value pairs
  d2 = { 
    'water':1,
    'eggs':6
  }
  print("\nThis is dictionary with two key-value pairs: ",d2)
  
  #This is nested dictionary 
  d3 = {
    'Food': {
      'water':1,
      'eggs':6
    }
  }

  print("\nThis is nested dictionary : ",d3)

  #Creating a dictionary using dict keyword
  d4 = dict(name='Bob',age='50')
  print("\nDictionary using dict keyword: ",d4)

  #Using zip on two lists to create a dictionary
  keyList = ['a','b','c','d']
  valueList = [3,4,5,6]
  d5 = dict(zip(keyList,valueList))
  
  print(f"\nKey List: {keyList}" )
  print(f"Value List: {valueList}" )
  print("The dictionary created using zip: ",d5)

  #Creating a dictionary using from keys function
  d6 = dict.fromkeys( ['x','y'] )
  print("The dictionary created using fromkeys: ",d6)

  #Creating a dictionary using from keys function
  d7 ={
    'apple':'$3',
    'banana': '$2',      
    'strawberry': '$1'
  }

  print(f"\nAccessing values using dictionaries: {d7['apple']}")

  #Printing the keys in a dictionary
  print("\nThe keys of the dictionary are: ",d7.keys())
  
  #Printing the values in a dictionary
  print("\nThe values of the dictionary are: ",d7.values())

  #Printing the items in a dictionary
  print("\nThe items in the dictionary are: ",d7.items())
  
  #Copying the dictionary into another dictionary
  d8 = d7.copy()
  print("\nTHe copied dictionary is: ",d8)
  
  #Using the .get(key,default) 
  print("\nUsing .get(key,default) on an existing key:",d8.get('apple','$0'))
  print("Using .get(key,default) on a new key:",d8.get('grapes','$0'))

  #Using .update() i.e merging two lists
  d4.update(d8)
  print("\nThe merged dictionaries are: ",d4)

  #Popping element in a dictionary
  print("\nPopping element: ",d4.pop('name'))

def main():
  dicts()

main()