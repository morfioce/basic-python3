# basic-python3
A collection of beginner python3 exercises

# How to do the exercises

## 1. Installing Python 3
You need to make sure that you have python 3 installed on your computer.

### 1.1 Windows users
To check if you already have python 3 in your computer, open a terminal (`win + r` then type `cmd`).  
Now type the following command: `python --version`.  
You should see something like this.  
![Python version 6][py-version]


I highly recommend that you install the anaconda distribution from [here][download-anacoda-win]

## 1.2 Linux users  
If you are using ubuntu chances are you have already python 3 installed.  
To check if you already have python 3 in your computer, open a terminal (`ctr + alt + t`).  
Now type the following command:  `python3 --version`.  

If you are using ubuntu 16.10 or newer install python 3 with the following command:  
`sudo apt-get update`  
`sudo apt-get install python3.6`  

I highly recommend that you install the anaconda distribution from [here][download-anaconda-linux]

## 2. Attempting the exercises

## 2.1 open the exercise in your favorite code editor (Sublime Text, Atome, vim)
Fill in the function according to the specification on top of it's definition.  
For example here I implement the `function donuts`:  
![Example of code][py-example]

## 2.2 Running the test
To check that the code you write is correct and behave as expected, you need to pass all the tests (written at the bottom of each file).  
For example here I run the test for the code I wrote for `function donuts`:  
![Exemple of test][py-test]


[py-version]: ./img/py-version.jpg "Python version 6"  
[py-example]: ./img/py-example.jpg "Python example"  
[py-test]: ./img/py-test.jpg "Python test"
[download-anaconda-win]: https://www.continuum.io/downloads  
[download-anaconda-linux]: https://docs.continuum.io/anaconda/install/linux  
