training_with_url = __import__('2_training_with_url')  
import pandas 

def testForAllURLs():
    df = training_with_url.getAllURLs() 
    x_df , y_df = training_with_url.reduce_test_data( df , test_size=0.3 ) 
    features = training_with_url.extract_features( x_df ) 
    res , x_test , y_test , num_train = training_with_url.training_with_extracted_features( features , y_df ) 
    accuracy = training_with_url.getAccuracy( res , x_test , y_test ) 
    print("accuracy:" + str( accuracy ) ) 
def testForKaggleURLs( test_size ):
    from sklearn.model_selection import train_test_split
    T = 5 
    total_accuracy = 0
    total_train = 0 
    for i in range( 0 , T ): 
        reduce_x_train , x_df , reduce_y_train , y_df = train_test_split( X_df , Y_df , test_size=test_size )  # reduce the number of test data 
        res , x_test , y_test , num_train = training_with_url.training_with_extracted_features( x_df , y_df ) 
        cur_accuracy = training_with_url.getAccuracy( res , x_test , y_test ) 
        total_accuracy = total_accuracy + cur_accuracy
        total_train = total_train + num_train 
        print("accuracy:" + str( cur_accuracy ) ) 
    return total_accuracy / T , total_train / T 
def testByISCXURLfeatures():
    training = __import__('1_training') 
    res , test_x , test_y , _ = training.training( [ 0 , 1 , 2 , 20 , 21 , 34 , 38 , 44 , 57 ] ) # ValueError: too many values to unpack (expected 3) ->> the number of receiving varibles is less than the number of returned values
    accuracy = training_with_url.getAccuracy( res , X_df , Y_df ) 
    print("Accuracy:" + str( accuracy ) ) 
# testForAllURLs() 

def get_extracted_features( reduce_ratio = 0.99 ):
    df = training_with_url.getKaggleURLs() 
    X_df , Y_df = training_with_url.reduce_test_data( df , test_size=reduce_ratio )  
    X_df = training_with_url.extract_features( X_df ) 
    
    extracted_features = pandas.DataFrame( X_df ) 
    extracted_features.to_csv('.\\2_accuracy\\extracted_features' + str( reduce_ratio ) + '.csv' , index=None )
    Y_df = pandas.DataFrame( Y_df ) 
    Y_df.to_csv('.\\2_accuracy\\extracted_type' + str( reduce_ratio ) + '.csv' , index=None )
    return X_df , Y_df 

def trainKaggleURLs( reduce_ratio ):
    test_size = [ 0.01 , 0.05 , 0.10 , 0.15 , 0.20 , 0.25 , 0.30 , 0.45 , 0.50 , 0.55 ]
    num_train_list = []
    accuracy = [] 
    for i in test_size : 
        acc , avg_num_train = testForKaggleURLs( i ) 
        accuracy.append( acc ) 
        num_train_list.append( avg_num_train ) 
    accuracy_for_kaggle_urls = pandas.DataFrame() 
    accuracy_for_kaggle_urls['test_size'] = test_size
    accuracy_for_kaggle_urls['num_train'] = num_train_list  
    accuracy_for_kaggle_urls['accuracy'] = accuracy 
    accuracy_for_kaggle_urls.to_csv('.\\2_accuracy\\accuracy' + str( reduce_ratio ) +  '.csv' , index=None ) 
    print( accuracy_for_kaggle_urls )

    import matplotlib.pyplot as plt 
    import seaborn 
    seaborn.lineplot( accuracy_for_kaggle_urls , x='num_train' , y='accuracy' ) 
    plt.savefig('.\\2_accuracy\\accuracy' + str( reduce_ratio ) + '.png') 
print("acc for ISCXURL2016 URL Dataset")
testForAllURLs() # 32672 rows, about 30sec for extracting features

print("\nacc for Kaggle Dataset")
res , x_test , y_test , num_train = training_with_url.get_trained_modal_Kaggle( 0.1 ) 
acc = training_with_url.getAccuracy( res , x_test , y_test ) 
print( "ratio:0.1 " + "acc:" + str( acc ) ) 
res , x_test , y_test , num_train = training_with_url.get_trained_modal_Kaggle( 0.2 ) 
acc = training_with_url.getAccuracy( res , x_test , y_test ) 
print( "ratio:0.2 " + "acc:" + str( acc ) ) 
res , x_test , y_test , num_train = training_with_url.get_trained_modal_Kaggle( 0.3 ) 
acc = training_with_url.getAccuracy( res , x_test , y_test ) 
print( "ratio:0.3 " + "acc:" + str( acc ) ) 
res , x_test , y_test , num_train = training_with_url.get_trained_modal_Kaggle( 0.5 ) 
acc = training_with_url.getAccuracy( res , x_test , y_test ) 
print( "ratio:0.5 " + "acc:" + str( acc ) ) 
exit() 

reduce_ratio = 0.5 #Kaggle dataset has up to 600,000 rows, so we need to reduce its size
X_df , Y_df = get_extracted_features( reduce_ratio=reduce_ratio ) # extract all features  
trainKaggleURLs( reduce_ratio=reduce_ratio ) 
# 0.01 ->> 6000
# 0.05 ->> 30000
# 0.10 ->> 60000 
# 0.20 ->> 120000
# 0.30 ->> 180000
# exit() 



























# print("Accuracy testByISCXURLfeatures:") 
# testByISCXURLfeatures()