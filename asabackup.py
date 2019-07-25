import mmap
import ipaddress
import pandas as pd
import re
data=pd.read_fwf('E:/python279/conf.txt')
df=pd.DataFrame(data)
b=df[df[': Saved'].str.contains('extended permit ip')]
c=b[': Saved'].str.split('host', expand=True).dropna()
d=c.values.tolist()
c[2].to_excel('E:/finalresult.xlsx')


#a=b.values.tolist()
#n=0
#for i in a:
    #print(i) 
    #n=n+1
    #if(n==10):
        #break
       
#a=df[df[': Saved'].str.contains('|'.join(searchfor))==False]
#a1=b[b[': Saved'].str.contains('|'.join(searchfor))==True]
#b=a[a[': Saved'].str.split('host')]
#a1.to_excel("E:\subdata.xlsx")
#c=pd.read_csv("E:\subdata.csv")
#result=pd.DataFrame(c)
#final=result[result[': Saved'].str.contains('')]
#c=pd.DataFrame(a)
#print(c)
#result=c.loc[': Saved'].str.not in 
#for line in open('E:/python279/conf.txt').readlines():
    #if "access-list" in line:
        #print(line)
      
    
    
