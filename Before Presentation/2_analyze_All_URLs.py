import pandas 
import matplotlib.pyplot as plt 
import seaborn
training_with_url = __import__('2_training_with_url') 

df1 = pandas.read_csv('.\ISCXURL2016\FinalDataset\\URL\Benign_list_big_final.csv' , encoding='utf-8' , header=None)
df2 = pandas.read_csv('.\ISCXURL2016\FinalDataset\\URL\DefacementSitesURLFiltered.csv' , encoding='utf-8' , header=None)
df3 = pandas.read_csv('.\ISCXURL2016\FinalDataset\\URL\Malware_dataset.csv' , encoding='utf-8' , header=None) 
df4 = pandas.read_csv('.\ISCXURL2016\FinalDataset\\URL\phishing_dataset.csv' , encoding='utf-8' , header=None) 
df5 = pandas.read_csv('.\ISCXURL2016\FinalDataset\\URL\spam_dataset.csv' , encoding='utf-8' , header=None) 

df1.rename( columns={ 0 : 'URL' } , inplace=True )
df2.rename( columns={ 0 : 'URL' } , inplace=True ) 
df3.rename( columns={ 0 : 'URL' } , inplace=True ) 
df4.rename( columns={ 0 : 'URL' } , inplace=True ) 
df5.rename( columns={ 0 : 'URL' } , inplace=True ) 

df1['URLType'] = 'Benign' 
df2['URLType'] = 'Defacement' 
df3['URLType'] = 'Malware' 
df4['URLType'] = 'Phishing' 
df5['URLType'] = 'Spam' 

########################################################## URL Types Hist Value ##################################################################
test_url_type = pandas.DataFrame({ 'URLType': ['Benign' , 'Defacement' , 'Malware' , 'Phishing' , 'Spam'] , 'Number' : [ len( df1 ) , len( df2 ) , len( df3 ) , len( df4 ) , len( df5 ) ] } ) 
# print( test_url_type )
test_url_type.to_csv('.\\2_All_URL\\num_test_URL.csv' , index=None) 
plt.clf() 

df = training_with_url.getAllURLs() 
########################################################### URL Types Histplot ###################################################################
plt.figure( figsize=( 10 , 10 ) ) 
seaborn.histplot( data=df , x='URLType' , hue='URLType' ) 
plt.savefig('.\\2_All_URL\\num_test_URL.png')

