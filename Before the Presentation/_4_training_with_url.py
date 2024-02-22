from sklearn.model_selection import train_test_split
from sklearn import tree
import pandas 
import csv 

def getAllURLs():
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

    df2 = df2.iloc[ 0 : 40000 , : ]
    df = pandas.merge( df1 , df2 , how='outer' ) 
    df = pandas.merge( df , df3 , how='outer' ) 
    df = pandas.merge( df , df4 , how='outer' ) 
    df = pandas.merge( df , df5 , how='outer' ) 
    # print( df )    
    return df 
def getKaggleURLs():
    with open('dataset\malicious_phish.csv' , encoding='utf-8') as file: 
        dataset = csv.reader( file ) 
        df = pandas.DataFrame( data=dataset , columns=['URL' , 'URLType' ] )
        df = df.iloc[ 1 : , : ]
        return df 
def reduce_test_data( df , test_size = 0.3 ):
    ########## reduce the number of test urls and mix up them ###########
    from sklearn.model_selection import train_test_split
    reduce_x_train , reduce_x_test , reduce_y_train , reduce_y_test = train_test_split( df['URL'] , df['URLType'] , test_size=test_size ) 
    return reduce_x_test , reduce_y_test

def extract_features( df ):
    extract_url_features = __import__('2_extract_url_features')  
    ############ Construct the feature dataframe #############
    # ['Querylength', 'numDomainLevel' , 'numPathLayer' , 'domainlength', 'pathLength', 'NumberofDotsinURL', 'URL_DigitCount', 'URL_Letter_Count', 'spcharUrl']
    test_features = pandas.DataFrame(columns=['Entropy_Domain' , 'argPathRatio' , 'ArgUrlRatio' , 'argDomanRatio' , 'pathurlRatio' , 'CharacterContinuityRate' , 'NumberRate_FileName' , 'domainUrlRatio' , 'NumberRate_URL' , 'pathDomainRatio' , 'NumberRate_AfterPath' , 'avgpathtokenlen'] )  
    test_features = pandas.concat( [ test_features , pandas.DataFrame( columns=['Entropy_Domain' , 'argPathRatio' , 'ArgUrlRatio' , 'argDomanRatio' , 'pathurlRatio' , 'CharacterContinuityRate' , 'NumberRate_FileName' , 'domainUrlRatio' , 'NumberRate_URL' , 'pathDomainRatio' , 'NumberRate_AfterPath' , 'avgpathtokenlen'] , data=[[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ] ] ) ] )
    ################## Extract URL features ##################
    count = 0 
    for url in df:
        print( count )
        url = extract_url_features.feature( url )
        # url.display() 
        feature = url.getFeatureList2() 
        test_features = pandas.concat( [ test_features , pandas.DataFrame( columns=['Entropy_Domain' , 'argPathRatio' , 'ArgUrlRatio' , 'argDomanRatio' , 'pathurlRatio' , 'CharacterContinuityRate' , 'NumberRate_FileName' , 'domainUrlRatio' , 'NumberRate_URL' , 'pathDomainRatio' , 'NumberRate_AfterPath' , 'avgpathtokenlen'] , data=[ feature ] ) ] )
        count = count + 1 
    # remove the first row that was created at line 49
    test_features = test_features.iloc[1: , :] 
    return test_features 

def training_with_extracted_features( features , url_type ):
    ############# Test Extracted URL Features ################
    from sklearn import tree 
    x_train , x_test , y_train , y_test = train_test_split( features , url_type , test_size=0.3 )    
    DT = tree.DecisionTreeClassifier() 
    res = DT.fit( x_train , y_train )
    return res , x_test , y_test 

def getAccuracy( res , x_test , y_test ): # res: the trained modal 
    misPrediction = 0 
    prediction = res.predict( x_test ) 
    y_test = ( pandas.DataFrame( y_test ) ).values.tolist()  
    for i in range( 0 , len( y_test ) ):
        if( prediction[ i ] != y_test[ i ][ 0 ] ):
            misPrediction = misPrediction + 1 
    # print("misprediction:" + str( misPrediction ) )
    # print("Accuracy:" + str( ( len( y_test ) - misPrediction ) / len( y_test ) ) )
    return ( len( y_test ) - misPrediction ) / len( y_test )  , len( y_test )

def get_trained_modal( test_size = 0.3 ):
    df = getAllURLs() 
    x_df , y_df = reduce_test_data( df , test_size ) 
    features = extract_features( x_df ) 
    res , x_test , y_test = training_with_extracted_features( features , y_df ) 
    return res 
