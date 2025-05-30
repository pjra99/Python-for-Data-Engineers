import pandas as pd

def main():
    #Ways to create Df!"
    ##Using csv or excel

    csv_name = "BigMart Sales.csv"
    df = pd.read_csv(csv_name)
    # print(df)
    #You can specify the sheetname in case the csv is a workbook, like this pd.read_csv(csv_name)

    #You can use the 'parse_dates' attr to convert the type of the date column to date, which are by default considered as strings
    df =pd.read_csv(csv_name, parse_dates=['Outlet_Establishment_Year'])
    print(df)

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

    #while reading a csv we can give certain instructions based on the requirements
    #Below example skips the mentioned number of rows to exclude in the processed data frame
    df4 = pd.read_csv(csv_name, skiprows=1)

    print(df4)

    #Below example tells the compiler which row to consider for headers

    df4 = pd.read_csv(csv_name, header=3)

    print(df4)

    #Note: We can also mention header None in order to set the headers to just column indexes

    #We can also give the columns names if you want to give headers by yourself, but then it will consider headers(is present) 
    # as first row, so make sure to skip 1st rows if headers are already present
     
    df5 = pd.read_csv("Emp data.csv", skiprows= 1, names=["Emp Id", "Emp Name","Emp Dept", "Emp Salry" ])


    #To Read limited rows of the csv
    df5 = pd.read_csv("Emp data.csv", nrows =2)


    #To replace any value with NaN

    df5 = pd.read_csv("Emp data.csv", na_values=["Not Available", "na"])

    #To replace value from specific columns
    df5 = pd.read_csv("Emp data.csv", na_values={
       "Salary (INR)": ["Not Available", "na", "HR"]})


    #Using converters while reading data frames to  modfiy cell values
    df5 = pd.read_csv("Emp data.csv", converters={
        "Department": modify_dept_name
    })

    #Parse dates is used to change the type of the specific column to date type
    df5 = pd.read_csv("Emp data.csv", parse_dates=["Joining date"])
    print(df5)

def modify_dept_name(cell):
    if cell =="IT":
        return "Information Technology"
    elif cell=="HR":
        return "Human Resource"
    elif cell=="QA":
        return "Quality Assurance"

if __name__=="__main__":
    main()