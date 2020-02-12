import pandas as pd

# content = pd.read_excel('Book1.xlsx', index_col=0)
# print(content)

df1 = pd.DataFrame([['f', 'b'], ['c', 'd']],
                    index=['row 1', 'row 2'],
                    columns=['col 1', 'col 2'])
df1.to_excel("Book1.xlsx")

#with pd.ExcelWriter('Book1.xlsx', mode='a') as writer:  
#    df.to_excel(writer, sheet_name='Sheet_name_3')
