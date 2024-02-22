import pandas
training = __import__('1_training') 

def test_Accuracy( ratio_of_train , train_features , training_times ):
    total_accuracy = 0 
    # train the modal for n times
    for k in range( 0 , training_times ):
        # get the trained modal and x_test, y_test  
        res , x_test , y_test , N = training.training( train_features , ratio_of_train ) # N == len( x_train ) + len( x_test )
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
################################################################### plot the tree ###############################################################################
from sklearn import tree
import matplotlib.pyplot as plt 
MAX_DEPTH = 2
res , x_test , y_test , N = training.training( [ 0 , 1 , 2 , 20 , 34 , 38 , 44 , 57 , 73 ] , 0.3 , MAX_DEPTH ) # N == len( x_train ) + len( x_test )
plt.clf()
plt.figure( figsize=( 15 , 10 ) )
print("o")
tree.plot_tree( res , fontsize=30 )
print("X")
plt.savefig(".\\" + str( MAX_DEPTH ) + "decision tree.png")

######################################################### return prediction and y_test for True Pos, False Pos ##################################################
def test_Accuracy2( ratio_of_train , train_features , training_times ):
    total_accuracy = 0 
    
    # train the modal for n times
    for k in range( 0 , training_times ):
        # get the trained modal and x_test, y_test  
        res , x_test , y_test , N = training.training( train_features , ratio_of_train ) # N == len( x_train ) + len( x_test )
        prediction = res.predict( x_test ) 
        y_test = ( pandas.DataFrame( y_test ) ).values.tolist()  
        # print( x_test ) 
        # calculate the accuracy of current trained modal 
        misPrediction = 0 
        # 5 url types -> ben, dec, phi, spam, mal
        for i in range( 0 , len( prediction ) ):
            if( prediction[ i ] != y_test[ i ][ 0 ] ):
                misPrediction = misPrediction + 1 
        # print( "misPrediction:" + str( misPrediction ) ) 
        accuracy = ( len( prediction ) - misPrediction ) / len( prediction ) 
        # print( "Accuracy: " + str( k ) + " " + str( accuracy ) ) 
        total_accuracy = total_accuracy + accuracy 

    return total_accuracy / training_times , N - len( x_test ) , prediction , y_test 
######################################## Calculate the TP , FP ############################################
# 5 url types -> ben, dec, phi, spam, mal( B D P S M ) 
NUM_TRAINING = 10 
avg_acc , num_train , prediction , y_test = test_Accuracy2( ratio_of_train=0.3 , train_features=[ 0 , 1 , 2 , 20 , 34 , 38 , 44 , 57 , 73 ] , training_times = NUM_TRAINING ) 
# print( prediction , y_test ) 
TYPE = ['b' , 'D' , 'p' , 's' , 'm'] 
TP_FP = {'b/b':0 , 'b/D':0 , 'b/p':0 , 'b/s':0 , 'b/m':0 , 'D/b':0 , 'D/D':0 , 'D/p':0 , 'D/s':0 , 'D/m':0 , 'p/b':0 , 'p/D':0 , 'p/p':0 , 'p/s':0 , 'p/m':0 , 's/b':0 , 's/D':0 , 's/p':0 , 's/s':0 , 's/m':0 , 'm/b':0, 'm/D':0 , 'm/p':0 , 'm/s':0 , 'm/m':0 }  
for i in range( 0 , len( prediction ) ): 
    # print( prediction[ i ][ 0 ] , y_test[ i ][ 0 ][ 0 ] )
    if( prediction[ i ][ 0 ] == TYPE[ 0 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 0 ] ):
        TP_FP['b/b'] = TP_FP['b/b'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 0 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 1 ] ):
        TP_FP['b/D'] = TP_FP['b/D'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 0 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 2 ] ):
        TP_FP['b/p'] = TP_FP['b/p'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 0 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 3 ] ):
        TP_FP['b/s'] = TP_FP['b/s'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 0 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 4 ] ):
        TP_FP['b/m'] = TP_FP['b/m'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 1 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 0 ] ):
        TP_FP['D/b'] = TP_FP['D/b'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 1 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 1 ] ):
        TP_FP['D/D'] = TP_FP['D/D'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 1 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 2 ] ):
        TP_FP['D/p'] = TP_FP['D/p'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 1 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 3 ] ):
        TP_FP['D/s'] = TP_FP['D/s'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 1 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 4 ] ):
        TP_FP['D/m'] = TP_FP['D/m'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 2 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 0 ] ):
        TP_FP['p/b'] = TP_FP['p/b'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 2 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 1 ] ):
        TP_FP['p/D'] = TP_FP['p/D'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 2 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 2 ] ):
        TP_FP['p/p'] = TP_FP['p/p'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 2 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 3 ] ):
        TP_FP['p/s'] = TP_FP['p/s'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 2 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 4 ] ):
        TP_FP['p/m'] = TP_FP['p/m'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 3 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 0 ] ):
        TP_FP['s/b'] = TP_FP['s/b'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 3 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 1 ] ):
        TP_FP['s/D'] = TP_FP['s/D'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 3 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 2 ] ):
        TP_FP['s/p'] = TP_FP['s/p'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 3 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 3 ] ):
        TP_FP['s/s'] = TP_FP['s/s'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 3 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 4 ] ):
        TP_FP['s/m'] = TP_FP['s/m'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 4 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 0 ] ):
        TP_FP['m/b'] = TP_FP['m/b'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 4 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 1 ] ):
        TP_FP['m/D'] = TP_FP['m/D'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 4 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 2 ] ):
        TP_FP['m/p'] = TP_FP['m/p'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 4 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 3 ] ):
        TP_FP['m/s'] = TP_FP['m/s'] + 1 
    elif( prediction[ i ][ 0 ] == TYPE[ 4 ] and y_test[ i ][ 0 ][ 0 ] == TYPE[ 4 ] ):
        TP_FP['m/m'] = TP_FP['m/m'] + 1 
print( TP_FP ) 
for k , v in TP_FP.items():
    print( k , v )
exit() 

####################################################### csv for varying number of test data ####################################################################
accuracy_csv = pandas.DataFrame()
test_size_list = [ 0.9 , 0.85 , 0.8 , 0.75 , 0.7 , 0.65 , 0.6 , 0.55 , 0.5 , 0.45 , 0.4 , 0.35 , 0.3 , 0.25 , 0.2 , 0.15 , 0.1 , 0.05 ]
accuracy_csv['test_size'] = test_size_list 
avg_acc = [] 
num_train_list = [] 
# print( accuracy_csv )

test_size = 0.9 # percentage of dataset used as test data 
while( test_size > 0 ):
    cur_avg_acc , cur_num_train = test_Accuracy( ratio_of_train=test_size , train_features=[ 0 , 1 , 2 , 20 , 34 , 38 , 44 , 57 , 73 ] , training_times = NUM_TRAINING ) 
    avg_acc.append( cur_avg_acc )
    num_train_list.append( cur_num_train )  
    # print("Average Accuracy for " + str( NUM_TRAINING ) + " times training with test size " + str( test_size ) + ": " + str( cur_avg_acc ) ) 
    test_size = test_size - 0.05
accuracy_csv['average_accuracy'] = avg_acc 
accuracy_csv['number_of_train'] = num_train_list 
accuracy_csv.to_csv('.\\1_accuracy\\average_accuracy_vary_test_size.csv')

##################################################### lineplot for varying number of test data #################################################################
import matplotlib.pyplot as plt 
import seaborn 
plt.clf() 
# print( accuracy_csv ) 
seaborn.lineplot( accuracy_csv , x='number_of_train' , y='average_accuracy') 
plt.savefig('.\\1_accuracy\\average_accuracy_vary_test_size.png') 

######################################################### accuracy without specific feature ####################################################################
without = ['without_Query_Length', 'without_Domain_Token_Count', 'without_Path_Token_Count', 'without_Domain_Length', 'without_Number_of_dots_in_URL', 'without_URL_Digit_Count', 'without_URL_Letter_Count', 'without_Number_of_Special_Characters_in_URL', 'without_Entropy'] 
test_feature = [ 0 , 1 , 2 , 20 , 34 , 38 , 44 , 57 , 73 ] 
avg_acc_without = [] 
accuracy_csv
for i in range( 0 , 9 ):
    list = test_feature.copy() # without using copy(), test_feature won't be deep copied   
    # print( i )
    # print( len( list ) )
    del list[ i ]
    features_average_accuracy , _n = test_Accuracy( 0.3 , list, NUM_TRAINING )
    avg_acc_without.append( features_average_accuracy )  
    print("avg_accuracy_" + without[ i ] + ':' + str( features_average_accuracy ) )  
acc_without = pandas.DataFrame()
acc_without['features'] = without 
acc_without['accuracy'] = avg_acc_without  
print( acc_without ) 
plt.clf() 
plt.figure( figsize=( 15 , 15 ) )
plt.xticks(rotation=45, ha='right') 

seaborn.lineplot( acc_without , x='features' , y='accuracy' )
plt.savefig('.\\1_accuracy\\avg_acc_without.png') 
acc_without.to_csv('.\\1_accuracy\\avg_acc_without.csv' , index=None )  

# i == 0 ->> without Query Length(A)(0)
# i == 1 ->> without Domain Token Count(B)(1)
# i == 2 ->> without Path Token Count(C)(2)
# i == 3 ->> without Domain Length(U)(20)
# i == 4 ->> without Number of dots in URL(AI)(34)
# i == 5 ->> without URL Digit Count(AM)(38)
# i == 6 ->> without URL Letter Count(AS)(44)
# i == 7 ->> without Number of Special Characters in URL(BF)(57)
# i == 8 ->> without Entropy(BV)(73)


# d = DATASET.iloc[ : , [ 74 , 31 , 27 , 28 , 26 , 36 , 64 , 29 , 61 , 30 , 66 , 5 ] ]
# print( d )
# _12_features_average_accuracy , _ =  test_Accuracy( 0.3 , [ 74 , 31 , 27 , 28 , 26 , 36 , 64 , 29 , 61 , 30 , 66 , 5 ] , NUM_TRAINING ) 
# print("avg_accuracy_for_12_features:" + str( _12_features_average_accuracy ) ) 

'''
1.	Entropy Domain(BW)(74)
2.	argPathRatio(AF)(31)
3.	ArgUrlRatio(AB)(27)
4.	ArgDomanRatio(AC)(28)
5.	pathurlRatio(AA)(26)
6.	CharacterContinuityRate(AK)(36) 
7.	NumberRateFileName(BM)(64)
8.	domainUrlRatio(AD)(29)
9.	NumberRateURL(BJ)(61)
10.	PathDomainRatio(AE)(30)
11.	NumberRate AfterPath(BO)(66) 
12.	Avgpathtokenlen(F)(6)
'''
### Entropy_Domain  argPathRatio  ArgUrlRatio  argDomanRatio  pathurlRatio  CharacterContinuityRate NumberRate_FileName domainUrlRatio  NumberRate_URL  pathDomainRatio  NumberRate_AfterPath  avgpathtokenlen