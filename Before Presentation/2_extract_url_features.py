import math
'''
additional features: 
number of parameters 
'''
# Structure of an URL
###### class feature selection #####
###### improved class feature selection #####
class feature:
    def __init__( self , url ):
        self.url = url
        self.protocol = self.get_protocol()
        self.domain = self.get_domain()
        self.path = self.get_path()
        
        ### combine the following 4 functions into one scan() ###
        # self.num_digits = self.get_num_digits()
        # self.num_letters = self.get_num_letters()
        # self.num_special_char = self.get_num_special_char()
        # self.num_dots = self.get_num_dots() 
        self.num_digits = 0 
        self.num_letters = 0 
        self.num_special_char = 0 
        self.num_dots = 0  
        self.scan()
        
        self.path_len = len( self.path )
        ### combine the following 3 functions into one get_path_info
        # self.num_layer_path = self.get_num_layer_path()
        # self.num_param = self.get_num_param() 
        # self.file_ext = self.get_file_ext()
        self.path_token_count = 0 
        self.get_path_info()
        self.num_level_domain = self.get_num_level_domain()
        self.domain_token_count = self.get_domain_token_count() 
        self.domain_len = len( self.domain ) 
        self.entropy = self.get_entropy() 
        self.domain_entropy = self.get_domain_entropy() 
        # get query_len, query_digit_count, and query_letter_count 
        self.query = "" 
        self.query_len = 0 
        self.query_digit_count = 0 
        self.query_letter_count = 0
        self.get_query_info() 
        self.num_param = 0 
        if( self.path_len != 0 ):
            self.argPathRatio = self.num_param / self.path_len
        else:
            self.argPathRatio = -1 
        if( self.query_len != 0 ):
             self.NumberRateAfterPath = self.query_digit_count / self.query_len 
        else:
            self.NumberRateAfterPath = 0 
        self.ArgUrlRatio = self.num_param / len( self.url ) 
        if( len( self.domain ) != 0 ):
            self.ArgDomanRatio = self.num_param / len( self.domain ) 
            self.PathDomainRatio = self.path_len / len( self.domain ) 
        else:
            self.ArgDomanRatio = 0 
        self.pathurlRatio = self.path_len / len( self.url ) 
        self.domainUrlRatio = len( self.domain ) / len( self.url )
        self.NumberRateURL = self.num_digits / len( self.url ) 
        
        if( self.path_token_count != 0 ):
            self.avgpathtokenlen = self.path_len / self.path_token_count 
        else:
            self.avgpathtokenlen = 0 
        ##############~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.CharacterContinuityRate = 0  
        self.NumberRateFileName = 0 
        ##############~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def isDigit( self , c ):
        if( c >= '0' and c <= '9' ):
            return True
        return False
    def isLetter( self , c ):
        if( c >= 'a' and c <= 'z' ) or ( c >= 'A' and c <= 'Z' ):
            return True
        return False
    def isSpecialCharacter( self , c ):
        if( ( not self.isDigit( c ) ) and ( not self.isLetter( c ) ) ):
            if( c != '.' and c != '/' and c != '\\' ):
               return True
        return False
    def scan( self ):
        num_d = 0 # digits
        num_l = 0 # letters
        num_s = 0 # special cahracter 
        num_dot = 0 # number of dots 
        for i in range( 0 , len( self.url ) ):
            if( self.isLetter( self.url[ i ] ) == 1 ):
                num_l = num_l + 1 
            elif( self.isDigit( self.url[ i ] ) == 1 ):
                num_d = num_d + 1 
            elif( self.isSpecialCharacter( self.url[ i ] ) == 1 ):
                num_s = num_s + 1 
            elif ( self.url[ i ] == '.' ):
                num_dot = num_dot + 1 
        self.num_digits = num_d 
        self.num_letters = num_l 
        self.num_special_char = num_s 
        self.num_dots = num_dot 
        return 0 
    def get_url( self ):
        return self.url
    def get_protocol( self ):
        if( self.url.find( "https") != -1 ):
            return "https"
        if( self.url.find( "http" ) != -1 ):
            return "http"
        return ""
    def get_domain( self ):    
        url = self.url.replace( self.protocol + "://" , "" ) 
        i = 0 
        # print( len( url ) )
        for i in range( 0 , len( url ) ):
            if url[ i ] == '/':
                return url[:i]
        return url
    def get_path( self ):
        path = ( self.url.replace( self.protocol + "://" , "" ) ).replace( self.domain , "" )
        if( len( path ) > 1 and path[ 0 ] == '/' ):
            path = path[1:]
        return path
    def get_entropy( self ):
        string = self.url.strip()
        prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
        entropy = sum([(p * math.log(p) / math.log(2.0)) for p in prob])
        return entropy
    def get_domain_entropy( self ):
        string = self.domain.strip()
        prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
        entropy = sum([(p * math.log(p) / math.log(2.0)) for p in prob])
        return entropy
    def get_path_info( self ):
        start = -1 
        end = -1 # indicates if the url is found or not
        num_param = 0 
        num_path_layer = 0 
        path_token_count = 1  
        question_mark = 0 # if a query string appears
        for i in range( 0 , len( self.path ) ):
            if( self.path[ i ] == '/' ):
               num_path_layer = num_path_layer + 1 
               if( start != -1 and end == -1 ):
                   # print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
                   end = i - 1
            if( self.isDelimitor( self.path[ i ] ) == 1 ):
                path_token_count = path_token_count + 1 
            if( self.path[ i ] == '.' and question_mark == 0 and self.isLetter( self.path[ i - 1 ] ) == 1 ):
                start = i + 1
            
            if( self.path[ i ] == '?' ):
                question_mark = 1 
                if( start != -1 and end == -1 ):
                    end = i - 1
                for j in range( i , len( self.path ) ):
                    if( self.path[ j ] == '=' ):
                        num_param = num_param + 1 
                break
        # print("start:" + str( start ) + " end:" + str( end ) )
        if( start == -1 or( len( self.path ) >= end + 1 ) and self.path[ end + 1 ] == '/' ): 
            self.file_ext = "" 
            start = -1
        if( start != -1 and end == -1 ):
            self.file_ext = self.path[ start :]
        else:
            self.file_ext = self.path[ start : end + 1 ]
        self.num_param = num_param 
        self.num_layer_path = num_path_layer
        self.path_token_count = path_token_count 
    def isDelimitor( self , c ):
        if( c == '.' or c == '/' or c == '?' or c == '=' or c == '-' or c == '_' ):
            return 1  
        return 0 
    def get_num_level_domain( self ):
        num = 1
        for i in range( 0 , len( self.domain ) ): 
            if( self.domain[ i ] == '.' ): 
                num = num + 1 
        return num 
    def get_domain_token_count( self ):
        num = 1
        for i in range( 0 , len( self.domain ) ): 
            if( self.isDelimitor( self.domain[ i ] ) == 1 ): 
                num = num + 1  
        return num 
    def get_num_dots( self ):
        num = 0 
        for i in range( 0 , len( self.url ) ):
            if( self.url[ i ] == '.' ):
                num = num + 1 
        return num 
    def get_query_info( self ):
        # num_param = 0 
        i = len( self.path ) - 1 
        while( 1 ):
            if( i < 0 ):
                break 
            if( self.path[ i ] == '?' ):
                self.query = self.path[ i + 1 :  ]
                break 
            i = i - 1 
        self.query_len = len( self.query ) 
        query_digit_count = 0 
        query_letter_count = 0 
        for i in range( 0 , len( self.query ) ): 
            if( self.isDigit( self.query[ i ] ) ):
                query_digit_count = query_digit_count + 1 
            elif ( self.isLetter( self.query[ i ] ) ):
                query_letter_count = query_letter_count + 1 
            # elif ( self.query[ i ] == '=' ):
                # num_param = num_param + 1 
        self.query_letter_count = query_letter_count 
        self.query_digit_count = query_digit_count
        # self.num_param = num_param  
    def display( self ):
        print( "url:" + self.url ) 
        print( "protocol:" + self.protocol ) 
        print( "domain:" + self.domain ) 
        print( "path:" + self.path ) 
        print( "1.num_digits:" + str( self.num_digits ) ) 
        print( "2.num_letters:" + str( self.num_letters ) )
        print( "3.num_dots:" + str( self.num_dots ) )
        print( "4.num_special_char:" + str( self.num_special_char ) ) 
        print( "5.entropy:" + str( self.entropy ) ) 
        print( "6.path_len:" + str( self.path_len ) )
        print( "7.num_layer_path:" + str( self.num_layer_path ) ) 
        print( "8.domain_len:" + str( self.domain_len ) )
        print( "9.num_level_domain:" + str( self.num_level_domain ) ) 
        print( "10.query_len:" + str( self.query_len  ) )
        print( "11.query_digit_count:" + str( self.query_digit_count ) )
        print( "12.query_letter_count:" + str( self.query_letter_count ) )
        print( "13.domain_token_count:" + str( self.domain_token_count ) )
        print( "14.path_token_count:" + str( self.path_token_count ) )

        print("Additional features:")                                    
        print( "1.file_ext:" + self.file_ext ) 
        print( "2.num_param:" + str( self.num_param ) )  
    def getFeatureList( self ):
        list = [ 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. ]
        list[ 0 ] = self.query_len 
        list[ 1 ] = self.domain_token_count 
        list[ 2 ] = self.path_token_count
        list[ 3 ] = self.domain_len 
        list[ 4 ] = self.path_len  
        list[ 5 ] = self.num_dots 
        list[ 6 ] = self.num_digits
        list[ 7 ] = self.num_letters 
        list[ 8 ] = self.num_special_char 
        return list 
    def getFeatureList2( self ):
        list = [ 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0.]
        list[ 0 ] = self.domain_entropy
        list[ 1 ] = self.argPathRatio 
        list[ 2 ] = self.ArgUrlRatio
        list[ 3 ] = self.ArgDomanRatio
        list[ 4 ] = self.pathurlRatio
        list[ 5 ] = self.CharacterContinuityRate
        list[ 6 ] = self.NumberRateFileName
        list[ 7 ] = self.domainUrlRatio
        list[ 8 ] = self.NumberRateURL
        list[ 9 ] = self.PathDomainRatio 
        list[ 10 ] =  self.NumberRateAfterPath
        list[ 11 ] = self.avgpathtokenlen 
        return list 
    
'''
EntropyDomain, argPathRatio, ArgUrlRatio,
ArgDomanRatio, pathurlRatio,

!!! CharacterContinuityRate, NumberRateFileName, !!!

domainUrlRatio, NumberRateURL, PathDomainRatio, NumberRateAfterPath, avgpathtokenlen
'''
# [ 0 , 1 , 2 , 20 , 21 , 34 , 38 , 44 , 57 , 73 ] 
'''
1.	Query Length(A)(0)
2.	Domain Token Count(B)(1)
3.	Path Token Count(C)(2)
4.	Domain Length(U)(20)
5.	Path Length(V)(21)
6.	Entropy(BV)(73)
7.	URL Digit Count(AM)(38)
8.	URL Letter Count(AS)(44)
9.	Number of Special Characters in URL(BF)(57)
10.	Number of dots in URL(AI)(34)

'''