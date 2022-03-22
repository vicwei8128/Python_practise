import pandas as pd

#Row Oriented Dictionary To DataFrame
sales1=[{'account':'Jones LLC', 'Jan':150, 'Feb':200, 'Mar':140},
       {'account':'Alpha Co', 'Jan':200, 'Feb':210, 'Mar':215},
       {'account':'Blue Inc', 'Jan':50, 'Feb':90, 'Mar':95},]

df=pd.DataFrame(sales1)
print(df)
print(type(df))

#Column Oriented Dictionary To DataFrame
sales2={'account':['Jones LLC', 'Alpha Co','Blue Inc'],
        'Jan':[150,200,50], 
        'Feb':[200, 210,90],
        'Mar':[140, 215, 95],
       }       

df=pd.DataFrame.from_dict(sales2)
print(df)
print(type(df))

#List With Column Header To DataFrame
sales3=[('account', ['Jones LLC', 'Alpha Co','Blue Inc']),
       ('Jan', [150,200,50]), 
       ('Feb', [200, 210,90]),
       ('Mar',[140, 215, 95]),
      ]

df=pd.DataFrame.from_items(sales3)
print(df)
print(type(df))

#List Without Column Header To DataFrame
sales4=[('Jones LLC', 150, 200, 140),
       ('Alpha Co', 200, 210, 215),
       ('Blue Inc', 50, 90, 95)]
labels=['account','Jan', 'Feb', 'Mar']

df=pd.DataFrame.from_records(sales4, columns=labels)
print(df)
print(type(df))

