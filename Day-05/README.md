COMMAND LINE ARGUMENTS & ENVIRONMENT VARIABLES
-----------------------------------------------------------------------------

Command-Line Arguments:-

# Passing the arguments (command-line arguments) when executing the program itself
Running the script:     
python calc.py 2 add 5
# python - command to execute python programs 
# calc.py - python script to be executed
# 2, add, 5 - command line arguments (which are passed along with the script)

We use built-in "sys" module to read command line arguments with "argv[]" function with argument # being passed inside []

Code example-

import sys

# reading 1st command-line argument, converted to float and assigned to variable num1
num1 = float(sys.argv[1])   
# reading 2nd command-line argument, and assigned to variable Num1
operation = sys.argv[2]     
# reading 3rd command-line argument, converted to float and assigned to variable num2
num2 = float(sys.argv[3])   

................................................................


Environment variables:-

Always use environment variables to store or pass (instead of CL args) or use any sensitive info (ex. Password, api token, certs etc.) in your program do that no one else using the code can see it.

In Linux OS based VM-

Command to view all the env vars: 
env

Command to create/define env var named 'password' with a value of "abhishek": 
export password="abhishek"

How to directly read environment variables in your code:

import os

# reading the value of environment variables - password and token
Password = os.getenv(password)  # to read the value of the environment variable named 'password' from os
ApiToken = os.getenv(token)     # to read the value of the environment variable named 'password' from os

We use/refer Pypi - to install modules using pip
pypi - open source (anyone can write modules and contribute to it. Ex aws has provided boto3 module to interact with aws services using python)

pip - package manager for python, similar to yum in linux

os module - to talk to os

--------------------------------------------------------------------------------------


To open python prompt/command-line/terminal: 
python

To exit out if the python command line: 
cntr+d or exit()
