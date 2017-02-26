# WebCat
A web server that runs [LOLCODE](http://lolcode.org/)

# About
Tired of writing PHP, Python, or Javascript? Do you want to have some fun while writing your code? WebCat is the web server for you!<br/>
Webcat is powered by [Justin Meza's](http://justinmeza.com/) LOLCODE interpreter [lci](https://github.com/justinmeza/lci)

# What does WebCat do?
 Webcat renders the lolcode inside .lol files

## You write your regular HTML and put your code between the `<lolxd>` tags like this
```html
<!DOCTYPE html>
<html>
<head>
	<title>LOLCODE POWRD WEBZITE!</title>
</head>
<body>
    <h1>
    <lolxd>
      HAI 1.2
      VISIBLE "HELLO VISITOR"
      KTHXBYE
    </lolxd>
    </h1>
</body>
</html>
```
## Result
```html
<!DOCTYPE html>
<html>
<head>
	<title>LOLCODE POWRD WEBZITE!</title>
</head>
<body>
<h1>HELLO VISITOR</h1>
</body>
</html>
```
You can refer to the LOLCODE 1.2 language spec [here](https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md)

# Installing

#### There are only two requirements to run WebCat
* You must have [lci](https://github.com/justinmeza/lci) installed on your system and be able to run it globally from the command line
* python 3.x (**It must be python 3.x since WebCat runs using http.server which is not supported in python 2.x**)

#### After you have those you can just follow these steps
* Clone this repository
* Go into the WebCat folder
* Run webcat.py with either `python webcat.py` if you set up python3 correctly on windows or `python3 webcat.py` on linux. You should see the server starting up in your command line
* Go to localhost:8000 on your web browser, if everything is working you should see a webpage

# Using WebCat
* Put your files in the LOLCODE directory where webcat is installed, make sure they have the .lol extension even if they don't contain any LOLCODE. Eventually WebCat will support serving plain HTML files
* You should have an index.lol file which is served as the home page

### Any other file you add can be accesed by going to localhost:8000/filename (do not put .lol at the end or it won't work
For example if you have a file named admin.lol you can access it by going to localhost:8000/admin on your browser.

# WebCat is still in a very early stage
I've spent a total of maybe 3 hours on this so far so a lot of features might not be there.
# Contributing
If you want to contribute make sure to submit a pull request if you want to help me make a little part of the web powered by LOLCODE. Also, I will be writing a detailed description of the inner workings of WebCat in the [wiki](https://github.com/javif89/webcat/wiki) so it's easier to understand and contribute to the project so make sure to check that out.
