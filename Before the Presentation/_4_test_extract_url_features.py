training_with_url = __import__('_4_training_with_url')  
import pandas 

def testForAllURLs():
    df = training_with_url.getAllURLs() 
    x_df , y_df = training_with_url.reduce_test_data( df , test_size=0.3 ) 
    features = training_with_url.extract_features( x_df ) 
    res , x_test , y_test = training_with_url.training_with_extracted_features( features , y_df ) 
    accuracy , test_len = training_with_url.getAccuracy( res , x_test , y_test ) 
    print("accuracy:" + str( accuracy ) ) 
def testForKaggleURLs( test_size ):
    from sklearn.model_selection import train_test_split
    T = 10 
    total_accuracy = 0
    for i in range( 0 , T ): 
        reduce_x_train , x_df , reduce_y_train , y_df = train_test_split( X_df , Y_df , test_size=test_size )  # reduce the number of test data 
        res , x_test , y_test = training_with_url.training_with_extracted_features( x_df , y_df ) 
        cur_accuracy , test_len = training_with_url.getAccuracy( res , x_test , y_test ) 
        total_accuracy = total_accuracy + cur_accuracy
        print("accuracy:" + str( cur_accuracy ) ) 
    return total_accuracy / T , test_len
def testByISCXURLfeatures():
    training = __import__('1_training') 
    res , test_x , test_y = training.training( [ 0 , 1 , 2 , 20 , 21 , 34 , 38 , 44 , 57 ] ) 
    accuracy , test_len = training_with_url.getAccuracy( res , X_df , Y_df ) 
    print("Accuracy:" + str( accuracy ) ) 
# testForAllURLs() 

def get_extracted_features( reduce_ratio = 0.99 ):
    df = training_with_url.getKaggleURLs() 
    X_df , Y_df = training_with_url.reduce_test_data( df , test_size=reduce_ratio )  
    X_df = training_with_url.extract_features( X_df ) 
    
    extracted_features = pandas.DataFrame( X_df ) 
    extracted_features.to_csv('.\\4_accuracy\\extracted_features.csv' , index=None )
    Y_df = pandas.DataFrame( Y_df ) 
    Y_df.to_csv('.\\4_accuracy\\extracted_type.csv' , index=None )
    return X_df , Y_df 

def trainKaggleURLs( reduce_ratio ):
    test_size = [ 0.01 , 0.05 , 0.10 , 0.15 , 0.20 , 0.25 , 0.30 , 0.45 , 0.50 , 0.55 ]
    test_len_list = []
    accuracy = [] 
    for i in test_size : 
        acc , test_len = testForKaggleURLs( i ) 
        accuracy.append( acc )
        test_len_list.append( test_len ) 
    accuracy_for_kaggle_urls = pandas.DataFrame() 
    accuracy_for_kaggle_urls['test_size'] = test_size 
    accuracy_for_kaggle_urls['test_len'] = test_len 
    accuracy_for_kaggle_urls['accuracy'] = accuracy 
    accuracy_for_kaggle_urls.to_csv('.\\4_accuracy\\accuracy' + str( reduce_ratio ) +  '.csv' , index=None ) 

    import matplotlib.pyplot as plt 
    import seaborn 
    seaborn.lineplot( accuracy_for_kaggle_urls , x='test_len' , y='accuracy' ) 
    plt.savefig('.\\4_accuracy\\accuracy' + str( reduce_ratio ) + '.png') 

reduce_ratio = 0.05
X_df , Y_df = get_extracted_features( reduce_ratio ) 
trainKaggleURLs( reduce_ratio )
# testByISCXURLfeatures()