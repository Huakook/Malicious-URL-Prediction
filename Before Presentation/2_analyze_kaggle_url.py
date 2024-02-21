import matplotlib.pyplot as plt 
import seaborn 
import pandas 

df = pandas.read_csv('.\dataset\malicious_phish.csv') 
seaborn.histplot( df , x='type' , hue='type' ) 
plt.savefig('.\\2_Kaggle_hist\\URL_TYPE_hist.png') 


plt.clf()
url_type = df['type'] 
x , y , z = plt.hist( url_type ) 
# print( x )
x = [ i for i in x if  i != 0 ]
# print( x )
# print() 
hist_values = pandas.DataFrame()
hist_values['Phishing'] = x[ 0 : 1 ]
hist_values['Benign'] = x[ 1 : 2 ]
hist_values['Defacement'] = x[ 2 : 3 ]
hist_values['Malware'] = x[ 3 : 4 ]
# print( hist_values )
hist_values.to_csv('.\\2_Kaggle_hist\\URL_TYPE_hist.csv' , index=False) 