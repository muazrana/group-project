# DevOps - Python Project
An application where people can write their name in and get a unique inidividual account number followed by a prize. There are several big surprises in this application which one can win. The prize is randomly generated and is not selected according to someones age or anything. 

We recommend using the lambda branch to run the app. 
# Prerequisite 
  1. Make sure the very first thing you do is __"sudo apt-get update"__
  2. Make sure you have __python3__ installed on your VM
  3. Install __pip3__
  4. Clone this repository to your machine
  5. run the command __"pip install -r requirements.txt"__  
  6. An amazon account 
  
  
 # Running the App in different ways

 ## On the Local Machine
  1. clone the group-project
  2. cd in the group-project
  3. type __"pip3 install -r requirements.txt"__
  4. use __"python3 run.py"__ to run the app
 
 ## Using Docker
  1. Docker can be uploaded to your machine using __curl https://get.docker.com | sudo bash__
  2. Once its installed you can run using the code, to build an image, __docker build -t group-project .__
  3. Next step after writing the code above to run it, use the command, __docker run -d -p 5000:5000 group-project__

 ## Using Docker/Docker-compose on AWS
 __Open ec2 instance and write the following commands__
  1. sudo yum update 
  2. sudo amazon-linux-extras install docker 
  3. To install docker-compose - sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)"-o /usr/local/bin/docker-compose
  4. sudo usermod -aG docker $(whoami) - make sure to exit out of the EC2 instance for this to take effect 
  5. sudo chmod +x /usr/local/bin/docker-compose
  6. sudo yum install git
  7. git clone https://github.com/muazrana/group-project
  8. git checkout lambda 
  9. docker-compose up -d --build
  10. Copy and past the public url into the google search bar
  
  
# Using Lambda Branch on EC2
Using lambda function instead? Head to Lambda Branch and clone it. Later create these lambda functions on AWS. Search for Lambda and     start creating the following functions mentioned, with their code, below.
 
  ## Lambda function for Prize Generator 
   1. import random
   
   2. def lambda_handler(event, context):
   3.    prize_list = ['House', '£10,000', '£100,000', 'Car', 'Mac Computer', 'IPAD', 'Iphone 11 pro', 'Package holiday' ]
   4.   prize_won = (random.choice(prize_list))
   5.   return prize_won
      
  ## Lambda function for Letter Generator
   1. import random
  
   2. def lambda_handler(event, context):
   3.  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   4. random_letter=''
   5. for i in range(3):
   6.     random_letter += letters[random.SystemRandom().randint(0, 25)]
   7. return random_letter
    
  ## Lambda function for Number Generator
   1. import random
   
   2. def lambda_handler(event, context):
   3.   random_number = ''
   4.   for n in range(3):
   5.     random_number += str(random.randint(0,9))
   6.   return random_number
      
 ## Lambda function for Shuffle
 __"Shuffle was a function created in order to combine 3 strings from both 'letter generator' & 'number generator' in order to get a unique id for each individual user. The code for shuffle file is written below:__
 
  1. import json
  2. import boto3
  3. import random
  4. def lambda_handler(event, context):
  5.    awsFunction = boto3.client("lambda")
  6.    numbers = awsFunction.invoke(
  7.            FunctionName='number_gen',
  8.            InvocationType='RequestResponse')
  9.    num = numbers['Payload'].read()
 10.    words = awsFunction.invoke(
 11.            FunctionName='letter_gen',
 12.            InvocationType='RequestResponse')
 13.    wrd = words['Payload'].read()
 14.    numwrd = str(wrd)[3:len(str(wrd))-2] + str(num)[3:len(str(wrd))-2]
 15.    response = ''.join(random.sample(numwrd, len(numwrd)))
 16.    return (response)
 
 # IAM roles 
 
 IAM is a Amazon services and can be found on the management console 
 Shuffle needs to be given an IAM role to be able to access the other lambda functions. The IAM role given was Lambda_full_acess_4_Lambda
 The EC2 instance you have spin up to build the app image on also needs to be given an IAM role to be able to access the RDS you have made and the lambda functions. The roles given for EC2 was AmazonRDSFullAccess and AWSLambdaFullAccess. 
 
 # Security Groups
 Also a Amazon service and can be found on the management console 
 A security group needs to be created for your EC2 instance. In the inbound rule the type is HTTP, proctocol is TCP and port range is 80. Another inbound rule needs to be for this same security group.  The type is MYSQL/AURORA, proctocol is TCP and port range is 3306. Source for both rule is 0.0.0.0/0
 
 
# Using RDS (Amazon Relational Database Service)
__"Creating the database"__ In AWS console, search for RDS and create the database and follow the given steps:
  
 1. __Choose a daabase creation method__ "Standard Create"
 2. __Engine Option__ "MySQL"
 3. Leave the rest as it is and go to __Templates__ "Free tier"
 4. In __Settings__ Give your database a unique name
 5. __Master username__ "Add a login ID name"
 6. __Master password__ "Add a password to access your database" 
 7. Leave all the rest as it is and at the bottom click "Create database" 
   
 
Edit the __init__.py file to include your secret key and your database uri you have just created. The database uri is the endpoint to the database. 
After you have created your database in Amazon RDS you need to click the link VPC security group link. Another security group needs to be made with the type being MYSQL/AURORA, protocol is TCP and port range is 3306. Source is the group ID of the other secuirty group you made previously 

After all this has be implemented follow the instruction under the title # Using Docker/Docker-compose on AWS

# To Kill app
Stop and terminate the EC2 instance the app is running. 
