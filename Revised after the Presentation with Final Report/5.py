import numpy 
import pandas
pandas.options.mode.chained_assignment = None
'''See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  features.replace([numpy.inf, -numpy.inf], numpy.nan, inplace=True)
C:\AMP\Apache24\htdocs\Big Data Final Project\1_training.py:8: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame'''
DATASET = pandas.read_csv(".\ISCXURL2016\FinalDataset\All.csv")
def training( train_features , ratio_of_train = 0.3 , max_depth = 20 ): # selected_features: [ 0 , 1 , 2 , 20 , 21 , 34 , 38 , 43 , 44 , 49 , 57 , 73 ]    
    features = DATASET.iloc[ : , train_features ] # X 
    features.replace([numpy.inf, -numpy.inf], numpy.nan, inplace=True)
    features.dropna()
    url_type = DATASET.iloc[ : , 79 : 80 ] # Y 

    from sklearn.model_selection import train_test_split
    from sklearn import tree
    # train_test_split( X , Y , test_size )
    x_train , x_test , y_train , y_test = train_test_split( features , url_type , test_size = ratio_of_train )
    ### print("Train Data")
    ### print( x_train )
    ### print( y_train )
    DT = tree.DecisionTreeClassifier( max_depth=max_depth) 
    res = DT.fit( x_train , y_train )
    return res , x_test , y_test , len( url_type ) 

def test_Accuracy( ratio_of_train , train_features , training_times , max_depth = 300 ):
    total_accuracy = 0 
    # train the modal for n times
    for k in range( 0 , training_times ):
        # get the trained modal and x_test, y_test  
        res , x_test , y_test , N = training( train_features , ratio_of_train , max_depth=max_depth ) # N == len( x_train ) + len( x_test )
        prediction = res.predict( x_test ) 
        y_test = ( pandas.DataFrame( y_test ) ).values.tolist()  
        # print( x_test )
        # calculate the accuracy of current trained modal 
        misPrediction = 0 

        for i in range( 0 , len( prediction ) ):
            if( prediction[ i ] != y_test[ i ][ 0 ] ):
                misPrediction = misPrediction + 1 
        # print( "misPrediction:" + str( misPrediction ) ) 
        accuracy = ( len( prediction ) - misPrediction ) / len( prediction ) 
        # print( "Accuracy: " + str( k ) + " " + str( accuracy ) ) 
        total_accuracy = total_accuracy + accuracy 
    return total_accuracy / training_times , N - len( x_test ) 

from sklearn import tree
import matplotlib.pyplot as plt 
import seaborn 
def plotTree( features , ratio_of_train , max_depth , feature_names=[] , prefix="" ): 
    res , x_test , y_test , N = training( features , ratio_of_train , max_depth ) # N == len( x_train ) + len( x_test )
    plt.clf()
    plt.figure( figsize=( 50 , 20 ) )
    # print("o")
    tree.plot_tree( res , fontsize=30 , feature_names=feature_names , rounded=True , class_names=['Defacement', 'benign' , 'malware' , 'phishing' , 'spam'] )
    # print("X")
    plt.savefig(".\\5\\" + prefix + str( max_depth ) + "decision tree.png")
    # values: the number of samples for the certain classification 
    # if class_names=['Defacement', 'benign' , 'malware' , 'phishing' , 'spam'] 
    # e.g., [100 , 200 , 300 , 400 , 500 ] ->> 100 Defacement samples , 200 benign samples , 300 malware samples... 

def test_depth_acc( limit = 15 ):
    d = [] 
    acc = [] 
    features = [ 0 , 1 , 2 , 20 , 34 , 38 , 44 , 57 , 73 ] 
    features_names = ['Query Length' , 'Domain Token Count' , 'Path Token Count' , 'Domain Length' , 'Entropy' , 'URL Digit Count' , 'URL Letter Count' , 'Number of Special Characters' , 'Number of dots' ]
    for i in range( 1 , limit + 1 ):
        plotTree( features , 0.3 , i , feature_names=features_names ) 
        ac , s = test_Accuracy( 0.3 , features , 10 , i ) 
        d.append( i ) 
        acc.append( ac ) 
        print( "max_depth:" + str( i ) + " acc:" +  str( ac ) )  
    df_ = pandas.DataFrame()
    df_['max_depth'] = d 
    df_['accuracy'] = acc 
    plt.clf() 
    seaborn.lineplot( df_ , x='max_depth' , y='accuracy' ) 
    plt.savefig('.\\5\\depth_acc.png') 
    df_.to_csv('.\\5\\depth_acc.csv' , index=None )  

def test_reduce_features( features , features_names , max_depth ):
    acc = [] 
    remove = [] 
    for i in range( 0 , len( features ) ): 
        tmp_features = features.copy() 
        tmp_features.remove( tmp_features[ i ] ) 
        ac , s = test_Accuracy( 0.3 , tmp_features , 10 , max_depth=max_depth ) 
        acc.append( ac ) 
        remove.append( features_names[ i ] ) 
    df_ = pandas.DataFrame()
    df_['removed_feature'] = remove 
    df_['accuracy'] = acc 
    plt.clf() 
    plt.figure(figsize=(12 , 12))
    plt.xticks(rotation=45, ha='right') 
    seaborn.lineplot( df_ , x='removed_feature' , y='accuracy' ) 
    plt.savefig('.\\5\\' + str( i_th ) + '_th_remove_acc') 
    return acc.index( max( acc ) ) , max( acc ) # return the index of the max accuracy 



#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#################################################### test the acceptable depth for the tree ###########################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
# test_depth_acc( limit = 10 ) 



#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
######################################################### reduce the number of features ###############################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
# [ 0 , 1 , 2 , 20 , 34 , 38 , 44 , 57 , 73 ] 

i_th = 0 
''' 
features = [ 0 , 1 , 2 , 20 , 34 , 38 , 44 , 57 , 73 ] 
features_names = ['Query Length' , 'Domain Token Count' , 'Path Token Count' , 'Domain Length' , 'Entropy' , 'URL Digit Count' , 'URL Letter Count' , 'Number of Special Characters' , 'Number of dots' ]
max_acc = 0.99 
while( len( features ) > 0 and max_acc > 0.85 ):
    next_remove_feature_index , max_acc = test_reduce_features( features_names=features_names , features=features , max_depth=11 ) 
    print( "next_remove:" + str( features[ next_remove_feature_index ] ) + features_names[ next_remove_feature_index ] ) 
    i_th = i_th + 1 
    features.remove( features[ next_remove_feature_index ] ) 
    features_names.remove( features_names[ next_remove_feature_index ] ) 
''' 
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
###################################### test the acceptable depth for the tree with 4 features #########################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

d = [] 
acc = [] 
features = [ 20 , 34 , 38 , 57 ] 
features_names = ['Query Length' , 'Domain Token Count' , 'Path Token Count' , 'Domain Length' , 'Entropy' , 'URL Digit Count' , 'URL Letter Count' , 'Number of Special Characters' , 'Number of dots' ]
for i in range( 1 , 15 + 1 ):
    plotTree( features , 0.3 , i , feature_names=features_names , prefix="4_features_" ) 
    ac , s = test_Accuracy( 0.3 , features , 10 , i ) 
    d.append( i ) 
    acc.append( ac ) 
    print( "max_depth:" + str( i ) + " acc:" +  str( ac ) )  
df_ = pandas.DataFrame()
df_['max_depth'] = d 
df_['accuracy'] = acc 
plt.clf() 
plt.figure( figsize=(10, 10))
seaborn.lineplot( df_ , x='max_depth' , y='accuracy' ) 
plt.savefig('.\\5\\4_features depth_acc.png') 
df_.to_csv('.\\5\\4_features depth_acc.csv' , index=None ) 