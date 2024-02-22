import validators 
import pandas 
training_with_url = __import__('_4_training_with_url') 
extract_url_features = __import__('2_extract_url_features') 

res = training_with_url.get_trained_modal( test_size = 0.1 ) 

while( 1 ):
    url = input("Enter an URL:")  
    if( url == 'exit' ):
        break
    if( validators.url( url ) ):
        # print("Valid")
        
        feature = extract_url_features.feature( url )
        feature_list = feature.getFeatureList2() 
        feature_df = pandas.DataFrame(columns=['Entropy_Domain' , 'argPathRatio' , 'ArgUrlRatio' , 'argDomanRatio' , 'pathurlRatio' , 'CharacterContinuityRate' , 'NumberRate_FileName' , 'domainUrlRatio' , 'NumberRate_URL' , 'pathDomainRatio' , 'NumberRate_AfterPath' , 'avgpathtokenlen'] )  
        feature_df = pandas.concat( [ feature_df , pandas.DataFrame( columns=['Entropy_Domain' , 'argPathRatio' , 'ArgUrlRatio' , 'argDomanRatio' , 'pathurlRatio' , 'CharacterContinuityRate' , 'NumberRate_FileName' , 'domainUrlRatio' , 'NumberRate_URL' , 'pathDomainRatio' , 'NumberRate_AfterPath' , 'avgpathtokenlen'] , data=[ feature_list ] ) ] )
        prediction = res.predict( feature_df ) 
        print( feature_df )
        print(prediction) 
        print("prediction:" + prediction[ 0 ] )  
    else:
        print("Invalid URL !") 