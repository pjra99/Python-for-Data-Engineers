import pandas as pd
def main():
    #Ways to create Df!"
    ##Using csv or excel
    df = pd.read_csv("BigMart Sales.csv")
    print(df)
    #You can specify the sheetname in case the csv is a workbook, like this pd.read_csv("BigMart Sales.csv")

    #Creating from a lost of rows
    data = [(101, 'Rajesh', 'IT', 75000, 'Bangalore'),
            (102, 'Priya', 'HR', 60000, 'Mumbai'),
            (103, 'Anil', 'IT', 80000, 'Hyderabad'),
            (104, 'Sneha', 'HR', 62000, 'Pune'),
            (105, 'Manish', 'Finance', 90000, 'Chennai'),
            (106, 'Suresh', 'IT', 78000, 'Bangalore')]
    
    columns = ["EmpID", "Name", "Department", "Salary", "Location"]

    df1 = pd.DataFrame(data)

    print(df1)
    #we can also specify columns like this

    df1 = pd.DataFrame(data, columns=columns)

    print(df1)

    #creating df from a dictionary or list of dict

    data1 = {
        "id":[101, 102, 103],
        "emp_name": ["Anil", "Suresh", "Panil"],
        "dept":['IT', 'Sales', 'HR']
    }

    df2 = pd.DataFrame(data1)
    print(df2)

    lst_of_dct = [
        {"id":12, "name":"John", "Age":18, "Branch": "CS"},
        {"id":13, "name":"Paul", "Age":17, "Branch": "IT"},
        {"id":14, "name":"Shawn", "Age":18, "Branch": "CS"},
        {"id":15, "name":"Leena", "Age":19, "Branch": "EC"}
    ]

    df3 = pd.DataFrame(lst_of_dct)

    print(df3)

if __name__=="__main__":
    main()