import pandas 
import numpy 
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




