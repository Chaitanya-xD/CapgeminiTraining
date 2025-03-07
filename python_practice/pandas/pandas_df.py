import pandas as pd

data ={
  'Name' : ['Alice', 'Bob', 'Charlie', 'David'],
  'Age' : [25,30,25,40],
  'City':['New York', 'Los Angeles', 'Chicago', 'Houston'],
  'Gender' : ['F','M','F','M'],
  'Death' : [2001,2002,2003,2004]
}
#To set multiple index
#df.set_index(["Name", "Age", "City"],inplace=True)
# print(df.loc[("Alice", 25, "New York"),"Death"])

df = pd.DataFrame(data)
df_2 = pd.DataFrame({
  'Name' : ['Alice', 'Bob', 'Charlie','James'],
  'Married' : ['Yes','No','Yes','No']  
  }
)

df_merge = pd.merge(df,df_2,on='Name',how='right')
print(df_merge)