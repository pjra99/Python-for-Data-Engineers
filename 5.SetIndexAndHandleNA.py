import pandas as pd

def p(df):
    print(df)
    
def main():
    data = [(101, 'Rajesh', 'IT', 75000, 'Chennai'),
            (102, 'Priya', 'HR', 60000, 'Mumbai'),
            (103, 'Anil', 'IT', None, 'Hyderabad'),
            (104, 'Sneha', None, 62000, 'Pune'),
            (105, 'Manish', None, 90000, None),
            (106, 'Suresh', 'IT', 78000, None)]
    
    columns = ["EmpID", "Name", "Department", "Salary", "Location"] 

    df = pd.DataFrame(data, columns=columns)
    
    #We can set index using set_index with the desired name of the column. Now set_index returns a new df if we don't use inplace 
    #attribute, or we set inplace attribute to false, like in below example
    df_ = df.set_index("EmpID")

    p(df_)

    #If we set inplace attribute to True, that means that the original df is modified
    df.set_index("EmpID", inplace=True)

    #Replacing NA values using fillna, values inside NA function is the replacement value, like shown in below examples
    df1 = df.fillna('Not Avl')
    df2 = df.fillna(0)

    #We can also pass a dictionary in fillna function, as a param, where the key is the column name and the value is the 
    #replacement value for that column, see the below ex
    df3 = df.fillna({
        "EmpID":0,
        "Department":"Dep to be assigned yet",
        "Salary":0,
        "Location":"Not Avl"
    })
    #In the below output, EmpID value won't be replaced because indexed columns don't accepted a replacement value as that's
    #the whole purpose of index, right?
    p(df3)

    #Forward fill- Carry forward previous row cell's value in the None/NaN cells
    df4 = df.fillna(method="ffill")
    p(df4)
    #Similarly we can use Backward fill, to fill next row cell's value in the cells having no value, the method name is 'bfill'

    #Now there's another attribute 'limit' which can be used with ffill and bfill. Limit is used to specify upto how many consecutive empty cells in a column,
    #we want to have the same value as the last cell, having a value. See the below example

    df5 = df.fillna(method='ffill',  limit=1)
    #above implementation will only apply ffill in 1 cell ahead of the last cell having value in the column Location, i.e., 5th row
    p(df5)

    #Interpolate- It calculates the replacement value for empty cells and fills it, based on the previous and next row values in each column. If it doesn't work in all the cells
    df6 = df.interpolate()
    p(df6)

    #Dropna - can be used to drop rows with null values
    df7 = df.dropna()
    p(df7)

    #Dropna accepts the parmaters like 'how' and 'thresh'
    #'all' deletes rows having NA in all the columns
    #'thresh' param can be used to sepcifes the number of valid columns in a row, for keeping the row
    df8 = df.dropna(how="all")
    p(df8)

    df9 = df.dropna(thresh=3) 
    p(df9)
     
    weather_data = [
    ('2017-01-01', 32.0, 6.0, 'Rain'),
    ('2017-01-04', None, 9.0, 'Sunny'),
    ('2017-01-05', 28.0, None, 'Snow'),
    ('2017-01-07', 32.0, None, 'Rain'),
    ('2017-01-10', 34.0, 8.0, 'Cloudy'),
    ('2017-01-11', 40.0, 12.0, 'Sunny')
    ]

    df10 = pd.DataFrame(weather_data, columns=['Date', 'Temp', 'Windspeed', 'Event'])
    df10['Date'] = pd.to_datetime(df10['Date']) #set date column to date type
    df10.set_index('Date', inplace=True) #setting 'Date' column as the index of the data frame
    p(df10)

    #Data range can be used to create a date_range with a range of start date to end date
    dt = pd.date_range('01-01-2017', '01-11-2017')
    #Now this can be used to create an index and then set the index of any df, as shown below
    ind = pd.DatetimeIndex(dt)
    df11 = df10.reindex(ind)
    p(df11)


if __name__ =="__main__":
    main()