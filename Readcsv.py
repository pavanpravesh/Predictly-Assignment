import csv        #importing required libraries
import re
import pandas as pd


a=[]              #creating empty list to append first_name column of the csv file
b=[]              #creating empty list to append first_name column of the csv file
c=[]              #creating empty list to append email column of the csv file
d=[]              #creating empty list to append subject column of the csv file
e=[]              #creating empty list to append email body column of the csv file

                
file_name = "sample_email.csv" 
f = open(file_name)        #opening sample_email.csv file
csv_file = csv.reader(f)
column = [] 
for line in csv_file:      #appending required columns to particular list 
    column.append(line[0])      
    a.append(line[0])
    column.append(line[1])
    b.append(line[1])
    column.append(line[10])
    c.append(line[10])
    column.append(line[11])
    d.append(line[11])
    column.append(line[12])
    e.append(line[12])
del(a[0],b[0],c[0],d[0],e[0])       #deleting empty element present at [0]
z=[]
for i in range(0, len(a)): 
   z.append(a[i] +" "+ b[i])        #adding elements of column first_name and last_name to form file name
n=z
for x in range(len(n)):             
    for y in range(len(c)):
        if x==y:
            f = open("email_template_of_"+str(n[x])+'.txt', 'a')   #creating .txt file for each name in csv
            f.write("Email to: "+str(c[y])+"\nSubject line:")      #adding email to .txt file of particular name file from particular column
            f.close()
        for p in range(len(d)):
            if x==y==p:
                f = open("email_template_of_"+str(n[x])+'.txt', 'a')
                f.write(""+str(d[p])+"\nHi"" "+str(n[x])+",")             #adding subject line to .txt file of particular name file from particular column
                f.close()
            for q in range(len(e)):
                if x==y==p==q:
                    f = open("email_template_of_"+str(n[x])+'.txt', 'a')
                    f.write("\n"+str(e[q])+"\nThanks,\nRob Willison.")    #adding email body to .txt file of particular name file from particular column
                    f.close()
# using list comprehension 
listToStr = ' '.join([str(elem) for elem in e]) 
  
    
lst1=re.findall("\d{3}-\d{3}-\d{4}",listToStr)                     #searching for phone number in particular ,txt file using regular expression
lst2=re.findall("\(\d{3}\) \d{3}-\d{4}",listToStr)                 #searching for phone number in particular ,txt file using regular expression
lst3=re.findall("\w{1,20}\[\w{2}\]\w{2,20}.\w{2,3}",listToStr)     #searching for email id in particular ,txt file using regular expression
lst4=re.findall("\w{1,20}@\w{2,20}.\w{2,3}",listToStr)             #searching for email id in particular ,txt file using regular expression
lt1=lst1+lst2
lt2=lst3+lst4

                                            
my_df = pd.DataFrame(lt1)
my_df.to_csv('mail_number.csv', index=False, header=False)         #creating .csv file for searched phone numbers in a particular file

my_df = pd.DataFrame(lt2)
my_df.to_csv('email_id.csv', index=False, header=False)            #creating .csv file for searched email id in a particular file
                    
  


