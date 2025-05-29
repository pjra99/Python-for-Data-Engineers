import pandas as pd

def main():
    data = [(101, 'Rajesh', 'IT', 75000, None),
            (102, 'Priya', 'HR', 60000, 'Mumbai'),
            (103, 'Anil', 'IT', None, 'Hyderabad'),
            (104, 'Sneha', None, 62000, 'Pune'),
            (105, 'Manish', 'Finance', 90000, 'Chennai'),
            (106, 'Suresh', 'IT', 78000, 'Bangalore')]
    
    columns = ["EmpID", "Name", "Department", "Salary", "Location"]

    df = pd.DataFrame(data, columns=columns)
    
    #We can set index using set_index with the desired name of the column. Now set_index returns a new df if we don't use inplace 
    #attribute, or we set inplace attribute to false, like in below example
    df_ = df.set_index("EmpID")

    print(df_)

    #If we set inplace attribute to True, that means that the original df is modified
    df.set_index("EmpID", inplace=True)
    



if __name__ =="__main__":
    main()