import pandas as pd

def main():
    data = [(101, 'Rajesh', 'IT', 75000, None),
            (102, 'Priya', 'HR', 60000, 'Mumbai'),
            (103, 'Anil', 'IT', None, 'Hyderabad'),
            (104, 'Sneha', None, 62000, 'Pune'),
            (None, 'Manish', 'Finance', 90000, 'Chennai'),
            (106, 'Suresh', 'IT', 78000, 'Bangalore')]
    
    columns = ["EmpID", "Name", "Department", "Salary", "Location"]

    df = pd.DataFrame(data, columns=columns)
    
    #We can set index using set_index with the desired name of the column. Now set_index returns a new df if we don't use inplace 
    #attribute, or we set inplace attribute to false, like in below example
    df_ = df.set_index("EmpID")

    # print(df_)

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
    print(df3)

    




if __name__ =="__main__":
    main()