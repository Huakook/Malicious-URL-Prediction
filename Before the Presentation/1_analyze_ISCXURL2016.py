import matplotlib.pyplot as plt
import seaborn
import pandas 

DATASET = pandas.read_csv(".\ISCXURL2016\FinalDataset\All.csv")

############################################# remove those columns with NANs and INFs #################################################
features = DATASET.drop([ 'argPathRatio' , "NumberRate_Extension", 'Entropy_DirectoryName' , 'Entropy_Extension' , 'URL_Type_obf_Type' ] , axis = 1 )
# print( features )

##################################################### All features Hist ################################################################
plt.hist( features ) 
plt.savefig(".\\1_hist\\all_hist.png") 

##################################################### URL Types Hist ###################################################################
url_type = DATASET.iloc[ : , [ 79 ] ]
# print( url_type )
plt.clf() 
plt.figure( figsize=(10,10) )
# print( url_type.columns.values )
seaborn.histplot( url_type , x=url_type.columns.values[0] , hue = url_type.columns.values[0] ) 
plt.savefig(".\\1_hist\\url_type_hist.png")

##################################################### URL Types Hist Value #############################################################
plt.clf()
x , y , z = plt.hist( url_type ) 
# print( x )
x = [ i for i in x if  i != 0 ]
# print( x )
# print() 
hist_values = pandas.DataFrame()
hist_values['Defacement'] = x[ 0 : 1 ]
hist_values['Benign'] = x[ 1 : 2 ]
hist_values['Malware'] = x[ 2 : 3 ]
hist_values['Phishing'] = x[ 3 : 4 ]
hist_values['Spam'] = x[ 4 : 5 ]
# print( hist_values )
hist_values.to_csv('.\\1_hist\\URL_TYPE_hist.csv' , index=False) 

##################################################### All features Corr ################################################################
corr = features.corr() 
### print( corr )
corr.to_csv(".\\1_corr\\all_corr.csv" , index = True , encoding='utf-8')
plt.clf() 
plt.figure( figsize=(40,40) )
seaborn.heatmap( corr )
plt.savefig(".\\1_corr\\all_corr.png")

##################################################### 12 features Corr #################################################################
features = DATASET.iloc[ : , [ 0 , 1 , 2 , 20 , 34 , 38 , 43 , 44 , 49 , 57 , 73 ] ]
### print( features )
corr = features.corr() 
### print( corr)
corr.to_csv(".\\1_corr\\12_features_corr.csv")
plt.clf() 
plt.figure( figsize=(40,40) )
seaborn.set( font_scale=3 )
seaborn.heatmap( corr ,  linewidths=.5 )
plt.savefig(".\\1_corr\\12feature_corr.png")

##################################################### 10 features Corr #################################################################
features = DATASET.iloc[ : , [ 0 , 1 , 2 , 20 , 34 , 38 , 44 , 57 , 73 ] ]
### print( features )
corr = features.corr() 
corr.to_csv(".\\1_corr\\9_features_corr.csv")
### print( corr)
plt.clf() 
plt.figure( figsize=(40,40) )
seaborn.set( font_scale=3 )
seaborn.heatmap( corr ,  linewidths=.5 )
plt.savefig(".\\1_corr\\9feature_corr.png")