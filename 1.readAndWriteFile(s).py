# import xlsxwriter

def main():
    # using open
    f = open("drivers.json", "r", encoding="utf-8")
    print(f.read())
    f.close()

    #using with Open- this is recommended as it auto closing the file after read/wrrite/append operation
    with open("BigMart Sales.csv", "r") as f:
        print(f.read())
        
    #using for loop for line by line iteration, if you'll loop over f.read() then each word will be printed
    with open("dummyText.txt", "r") as f:
        for x in f:
            print(x)
    
    # writing into a file- using "w" over writes the orignal file content
    with open("dummyText.txt", "w") as f:
        f.write("This content is supposed to be added in the dummy text file")
    
    #to append new content to the existing content use "a"
    with open("dummyText.txt", "a") as f: 
        f.write("\nSome more content....")
    

if __name__ =="__main__":
    main()