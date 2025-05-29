import pandas as p

def main():
    lst_of_dct = [
        {"id":12, "name":"John", "Age":18, "Branch": "CS"},
        {"id":13, "name":"Paul", "Age":17, "Branch": "IT"},
        {"id":14, "name":"Shawn", "Age":18, "Branch": "CS"},
        {"id":15, "name":"Leena", "Age":19, "Branch": "EC"}
    ]
    df = p.DataFrame(lst_of_dct)

    #To create a function to csv
    df.to_csv('Student.csv')

    #To write to excel with a sheet name 
    df.to_excel('Student1.xlsx', sheet_name="batch-1")

    #To change the start rows/cols, to write data
    df.to_excel('Student2.xlsx', startrow=3, startcol=4)

    




if __name__ == "__main__":
    main()