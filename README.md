# DevOps - Python Project
An application where people can write their name in and get a unique inidividual account number followed by a prize. There are several big surprises in this application which one can win. The prize is randomly generated and is not selected according to someones age or anything. 

# Prerequisite 
  1. Make sure the very first thing you do is __"sudo apt-get update"__
  2. Make sure you have __python3__ installed on your VM
  3. Install __pip3__
  4. Clone this repository to your machine
  5. run the command __pip install -r requirements.txt__  
  
  
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
 
