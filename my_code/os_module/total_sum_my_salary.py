# importing required modules
""" this script will calculate total salary based on 
   data available in the payslip present in path "C:\\Users\\ipasha\\Desktop\\pay_slips" """
"""caution this file is path specific and payslip specific """
import PyPDF2
import os
 
# creating a pdf file object

path = str(input("enter the path"))
print(path)
# path must be "C:\\Users\\ipasha\\Desktop\\pay_slips"
ret_of_os_walk = list(os.walk(path))

my_total_salary = 0


print("number of payslips available : ",len(ret_of_os_walk[0][2]))
fi_size = 0
number_of_payslips_available = len(ret_of_os_walk [0][2])
while (fi_size<number_of_payslips_available):
    
    
    pdfFileObj = open(ret_of_os_walk [0][0]+"\\"+ret_of_os_walk [0][2][fi_size], 'rb')
 
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
    # printing number of pages in pdf file

    print("number of pages: ",pdfReader.numPages)
 
    # creating a page object
    pageObj = pdfReader.getPage(0)

    print("str type print")
    # extracting text from page
    print(pageObj.extractText())

    lit_of_data = str(pageObj.extractText())

    print("\n\n\n\n")


    filename = 'payslip.txt'

    with open(filename, 'w') as f:
        f.write(lit_of_data)

    with open('payslip.txt','r') as file:
        # reading each line    
        for line in file:
 
        
            lit= list(line.split())
            pay = 0
            salary = 0
            size = len(lit)
            index =0 
            while (index < size):
            
                if(lit[index] == "50100334761637"):
                    salary= (lit[index+1])
                    break
                
                index = index+1
            print("my salary is : ",salary)
            sa = []
         
            for p in salary:
                if(p==","):
                    continue
                sa.append(p)
            
            print(sa)
            s = 0

            for k in sa:
                if k == ".":
                    break
                s= s*10+int(k)
            print("hoo this is my salary of month : ",s)
            my_total_salary = my_total_salary+s
            fi_size  =fi_size+1


print("hoo this is my salary total earning : ",my_total_salary)
#closing the pdf file object
pdfFileObj.close()
