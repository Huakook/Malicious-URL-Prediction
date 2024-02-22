import validators 
import pandas 
training_with_url = __import__('2_training_with_url') 
extract_url_features = __import__('2_extract_url_features') 
# predict with All-URL-trained modal
# res = training_with_url.get_trained_modal( test_size = 0.1 ) 

# predict with Kaggle-URL-trained modal
res = training_with_url.get_trained_modal_Kaggle() 

while( 1 ):
    url = input("Enter an URL:")  
    if( url == 'exit' ):
        break
    if( validators.url( url ) ):
        # print("Valid")
        feature = extract_url_features.feature( url )
        feature_list = feature.getFeatureList() 
        feature_df = pandas.DataFrame(columns=['Querylength', 'domain_token_count' , 'path_token_count' , 'domainlength', 'pathLength', 'NumberofDotsinURL', 'URL_DigitCount', 'URL_Letter_Count', 'spcharUrl'] )  
        feature_df = pandas.concat( [ feature_df , pandas.DataFrame( columns=['Querylength', 'domain_token_count' , 'path_token_count' , 'domainlength', 'pathLength', 'NumberofDotsinURL', 'URL_DigitCount', 'URL_Letter_Count', 'spcharUrl'] , data=[ feature_list ] ) ] )
        prediction = res[0].predict( feature_df ) 
        print( feature_df )
        print(prediction) 
        print("prediction:" + prediction[ 0 ] )  
    else:
        print("Invalid URL !") 
# https://practice.geeksforgeeks.org/explore?page=1&sprint=a663236c31453b969852f9ea22507634&sortBy=difficulty&sprint_name=SDE%20Sheet
# https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset
# https://github.com/
# https://www.unb.ca/cic/datasets/url-2016.html
# https://stackoverflow.com/questions/59447378/sklearn-plot-tree-plot-is-too-small

