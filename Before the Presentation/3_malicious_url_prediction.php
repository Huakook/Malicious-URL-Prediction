<!DOCTYPE html>
<html style="background-color: black">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <meta charset = "utf-8"/>
    <title>Malicious URL Prediction</title>
    <link rel = "stylesheet" type = "text/css" href = "3_rwd.css"/>
    <link rel = "icon" type = "image/x-icon" href = "icon.png" />
    <back>
</head>
<body>
<?php
    include_once "connect_server.php";
?>    
    <div class="desktop-menuitem">
        <div class="menu">
                <div class="LOGO", onclick="Home();" onmouseover="LogoOver(this);", onmouseout="LogoOut(this);">NDHUCSIE</div>
                <div class="menuitem", onclick="Home();" , onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">HOME</div>
                <div class="menuitem", onclick="Modal();", onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">Modal</div>
                <div class="menuitem", onclick="Question();", onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">Question</div>
                <div class="menuitem", onclick="About();", onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">ABOUT</div>
        </div>
    </div>

    <div class="mobile-menuitem">
        <div class = "menu">
            <div class="LOGO", onmouseover="LogoOver(this);", onmouseout="LogoOut(this);">NDHUCSIE</div>
            <div class="menuitem">
                <div id = "MenuDiv" , onclick = "menuClick();", onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">Menu</div>
                <div id = "menuListDiv", onmouseover = "menuDisplay();">
                    <div onclick="Home();", onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">HOME</div>
                    <div onclick="Modal();", onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">Modal</div>
                    <div onclick="Question();", onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">Question</div>
                    <div onclick="About();", onmouseover="menuListOver(this);" , onmouseout="menuListOut(this);">ABOUT</div>
                </div>
            </div>
        </div>
    </div>
    <hr/>
    <div id = "HOMEDiv", class = "menuListItem">
        Malicios URL Prediction
        <form method = "get" action="predict.php">
            
            <form method = "post" action="checkSubmission();" onsubmit="alert('submitted sucessfully!');">
            Enter the URL you want to predict:
            <br/>
            <input name="url" type="url" placeholder="http://localhost/Big%20Data%20Final%20Project/malicious_url_prediction.php" minlength="10" style="margin:5px;" required></input> <br/>
            
            <input type="submit" value="submit"></input>
        </form>
    </div>

    <div id = "ModalDiv", class = "menuListItem">
        <div> Training </div>
    </div>
    <div id = "QuestionDiv", class="menuListItem">
            <div > Question </div>
    </div>

    <div id = "ABOUTDiv", class = "menuListItem">
        <div > About </div>
    </div>

    <script>
        let menuClickTimes = 0 ; 
        function Home()
        {
            let homee = document.querySelector("#HOMEDiv");
            let modal = document.querySelector("#ModalDiv");
            let question = document.querySelector("#QuestionDiv");
            let about = document.querySelector("#ABOUTDiv");

            homee.style.display = "block";
            modal.style.display = "none";
            question.style.display = "none";
            about.style.display = "none";
        }
        Home();
        function Modal()
        {
            let homee = document.querySelector("#HOMEDiv");
            let modal = document.querySelector("#ModalDiv");
            let question = document.querySelector("#QuestionDiv");
            let about = document.querySelector("#ABOUTDiv");

            homee.style.display = "none";
            modal.style.display = "block";
            question.style.display = "none";
            about.style.display = "none";
        }
        function Question()
        {
            let homee = document.querySelector("#HOMEDiv");
            let modal = document.querySelector("#ModalDiv");
            let question = document.querySelector("#QuestionDiv");
            let about = document.querySelector("#ABOUTDiv");

            homee.style.display = "none";
            modal.style.display = "none";
            question.style.display = "block";
            about.style.display = "none";
        }
        function About()
        {
            
            let homee = document.querySelector("#HOMEDiv");
            let modal = document.querySelector("#ModalDiv");
            let question = document.querySelector("#QuestionDiv");
            let about = document.querySelector("#ABOUTDiv");

            homee.style.display = "none";
            modal.style.display = "none";
            question.style.display = "none";
            about.style.display = "block";
        }
        function menuClick()
        {
            if( menuClickTimes % 2 == 1 ) menuDisplay() ; 
            else menu_not_Display() ;  
            menuClickTimes = ( menuClickTimes + 1 ) % 2 ; 
        }
        function menuDisplay()
        {
            let menulist = document.querySelector("#menuListDiv");
            menulist.style.display = "block";
        }
        function menu_not_Display()
        {
            let menulist = document.querySelector("#menuListDiv");
            menulist.style.display = "none";
        }
        function menuListOver( elem )
        {
            elem.style.backgroundColor = "rgb(43, 43, 43)";
            elem.style.color = "rgb(270, 230, 150)";
        }
        function menuListOut( elem )
        {
            elem.style.backgroundColor = "black" ;
            elem.style.color = "white";
        }
        function LogoOver( elem )
        {
            elem.style.backgroundColor = "rgb(270, 230, 150)";
            elem.style.color = "darkcyan";
        }
        function LogoOut( elem )
        {
            elem.style.backgroundColor = "darkcyan" ; 
            elem.style.color = "rgb(270, 230, 150)";
        }
    </script>
    <?php
    include_once "predict.php" ;
    function checkSubmission()
    {
        echo "Hiiiiiiiiiiiiiiiiiiiiiiiiiiii" ;
    }
/*        function consoleLog( $str )
        {
            echo '<script type="text/javascript">' . 'console.log("' . $str . '");</script>';
        }
        if( $_SERVER["REQUEST_METHOD"] == "POST" )
        {
            $email = $_POST['email'];
            $passw = $_POST['passw'];
            $tell = $_POST['tell'];

            if( !empty($email) && !empty($passw) && !empty($tell) )
            {
                //$conn -> query( "insert into account_info values({$email}, {$passw}, {$tell})");
                //$check = $conn -> query("select * from account_info" );
                $query = $conn -> prepare( "insert into account_info values(:email, :passw, :tell)");
                try{
                        $check = $query -> execute(array(
                        ':email' => $email ,
                        ':passw' => $passw ,
                        ':tell' => $tell 
                    ));
                }catch( PDOexception $e ){
                    //echo consoleLog( $e );
                    echo consoleLog('The username has been singed up!');
                }
            }
        }
*/
    ?>
</body>
</html>
