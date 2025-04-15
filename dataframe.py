import pandas as pd

def main():
    df = pd.read_csv("BigMart Sales.csv")

    #to print selected columns
    print(df[['Item_Identifier','Item_Fat_Content']])

    #to print first 5 rows
    print(df.head())
    
    #to print last 5 rows or specify a number to increase/decrease the rows
    print(df.tail())
    #to print specific number of rows
    print(df.head(20))

    #To apply filter to the columns
    print(df[df["Item_Fat_Content"] == "Low Fat"])

    #Applying filter using filter function, for displaying selective columns
    print(df.filter(items=["Item_Identifier", "Item_Fat_Content", "Item_Weight"])[df["Item_Weight"]>10])

    ##SLICING
    #To view all the rows
    print(df[:])

    #Applying slicing, to retrive rows from 5th index to 19th index
    print(df[5:20])

    #Similary we can use step, below df retrieves rows from 5th index to 19th index and skips 2 rows
    print(df[5:20:2])

    ##LOC and #ILOC
    #LOC: it is used to return the rows and columns in a selective fashion
    #syntax: df.loc[start_ind: end_ind, ["Col1", "Col3", ...]]
    ######VERY IMP: LOC USES INCLUSIVE SLICING FOR THE END_INDEX, i.e  end index is inlcuded
    print(df.loc[2:11,["Item_Identifier", "Item_Fat_Content", "Item_Weight"]])

    #We can apply slicing/range in the col name as well
    print(df.loc[:,"Item_Identifier": "Item_Fat_Content"])
    
    #filtering out rows using loc
    print(df.loc[df.Item_Weight>10])

    #specifying columns with filteration (using loc)
    print(df.loc[df.Item_Weight>10, ['Item_Identifier', 'Item_Fat_Content']])

    #ILOC
    #I in ILOC stands for integer. ILOC uses only integer based index (no label) for rendering
    ######VERY IMP: ILOC USES EXCLUSIVE SLICING FOR THE END_INDEX, i.e  end index is exluded, very much like array/string slicing
    print(df.iloc[:,1:5])

    #direct slicing
    print(df[0:9])
    #note: panda uses iloc by default

if __name__ =="__main__":
    main()