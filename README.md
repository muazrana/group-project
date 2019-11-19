# DevOps - Python Project
An application where people can write their name in and get a unique inidividual account number followed by a prize. There are several big surprises in this application which one can win. The prize is randomly generated and is not selected according to someones age or anything. 

# Prerequisite 
  1. Make sure the very first thing you do is __"sudo apt-get update"__
  2. Make sure you have __python3__ installed on your VM
  3. Install __pip3__
  4. Clone this repository to your machine
  5. run the command __"pip install -r requirements.txt"__  
  
  
 # Running the App in different ways

 ## On the Local Machine
  1. clone the group-project
  2. cd in the group-project
  3. type __"pip3 install -r requirements.txt"__
  4. use __"python3 run.py"__ to run the app
 
 ## Using Docker
  1. Docker can be uploaded to your machine using __curl https://get.docker.com | sudo bash__
  2. Once its installed you can run using the code, to build an image, __docker build -t group-project .__
  3. Next step after writing the code above to run it is __docker run -d -p 5000:5000 group-project__
 
# Using Lambda Branch on EC2
Using lambda function instead? Head to Lambda Branch and clone it. Later create these lambda functions on AWS. Search for Lambda and     start creating the following functions mentioned, with their code, below.
 
  ## Lambda function for Prize Generator 
   1. import random
   
   2. def lambda_handler(event, context):
   3.    prize_list = ['House', '£10,000', '£100,000', 'Car', 'Mac Computer', 'IPAD', 'Iphone 11 pro', 'Package holiday' ]
   4.   prize_won = (random.choice(prize_list))
   5.   return prize_won
      
  ## Lambda function for Letter Generator
   import random
  
   def lambda_handler(event, context):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    random_letter=''
    for i in range(3):
        random_letter += letters[random.SystemRandom().randint(0, 25)]
    return random_letter
    
  ## Lambda function for Number Generator
   import random
   
   def lambda_handler(event, context):
      random_number = ''
      for n in range(3):
        random_number += str(random.randint(0,9))
      return random_number
      
 ## Lambda function for Shuffle
 __"Suffle was a function created in order to combine 3 strings from both 'letter generator' & 'number generator' in order to get a unique id for each individual user. The code for shuffle file is written below:__
 
  import json
  import boto3
  import random
  def lambda_handler(event, context):
      awsFunction = boto3.client("lambda")
      numbers = awsFunction.invoke(
              FunctionName='number_gen',
              InvocationType='RequestResponse')
      num = numbers['Payload'].read()
      words = awsFunction.invoke(
              FunctionName='letter_gen',
              InvocationType='RequestResponse')
      wrd = words['Payload'].read()
      numwrd = str(wrd)[3:len(str(wrd))-2] + str(num)[3:len(str(wrd))-2]
      response = ''.join(random.sample(numwrd, len(numwrd)))
      return (response)
 
      c
   
 
