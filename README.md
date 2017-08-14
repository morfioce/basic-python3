# basic-python3
A collection of beginner python3 exercises.  
The exercises are collected from various resources around the web.  
If you are serious about learning python 3 then you probably will find this collection very helpful.

I appreciate any suggestion to improve this repository  .  :smiley:

# How to do the exercises

## 1. Installing Python 3
You need to make sure that you have python 3 installed on your computer.

### 1.1 Windows users
To check if you already have python 3 in your computer, open a terminal (`win + r` then type `cmd`).  
Now type the following command: `python --version`.  
You should see something like this.  
![Python version 6][py-version]  

I highly recommend that you install the anaconda distribution from this [site][download-anaconda-win]  

## 1.2 Linux users  
If you are using ubuntu chances are you have already python 3 installed.  
To check if you already have python 3 in your computer, open a terminal (`ctr + alt + t`).  
Now type the following command:  `python3 --version`.  

If you are using ubuntu 16.10 or newer install python 3 with the following command:  
`sudo apt-get update`  
`sudo apt-get install python3.6`  

I highly recommend that you install the anaconda distribution from [here][download-anaconda-linux]

## 2. Attempting the exercises
In order to complete the exercises you need to pass all the tests successfully.

## 2.1 open the exercise in your favorite code editor (Sublime Text, Atome, vim)
Fill in the function according to the specification on top of it's definition.  
For example here I implement the `function donuts`:  
![Example of code][py-example]

## 2.2 Running the test
To check that the code you write is correct and behave as expected, you need to pass all the tests (written at the bottom of each file).  
For example here I run the test for the code I wrote for `function donuts`:  
![Exemple of test][py-test]


You see that my implementation of the `function donuts` failed at the first 2 test cases and succeded at the last 2 test cases.

## Good luck :thumbsup:

[py-version]: ./img/py-version.jpg "Python version 6"  
[py-example]: ./img/py-example.jpg "Python example"  
[py-test]: ./img/py-test.jpg "Python test"
[download-anaconda-win]: https://www.continuum.io/downloads  
[download-anaconda-linux]: https://docs.continuum.io/anaconda/install/linux  
