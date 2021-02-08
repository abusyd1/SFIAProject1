# Football Transfer Cenral
### _A site showcasing Football teams, with the ability to add new teams, and add players to those teams._


## Project Brief
According to the project specification, the objective of this project is to 'create a CRUD application with utilisation of supporting tools, methodologies, and tehcnologies that encapsulate all core modules covered during training.' CRUD is an accronym which stands for 'Create, Read, Update, Delete' - these features should be implemented within the application as well as encapsulating the following throughout the duration of the project:

* Kanban board
* ERD Diagrams
* CI Pipeline
* Relational database with minimum 2 tables
* Design documentation including README file which covers all relevant content
* Risk Assessment
* Python Programming
* Fully designed test suites with high test coverage
* Front end design with Flask and HTML
* Version Control with Git
* CI Server with Jenkins
* Use of a Cloud Server GCP

In my project, I will try to create a application which showcases football teams, where the user can view these teams, add new teams, view players within the teams, and edit or delete players from the teams.

The main tools that I used to create the application include Flask micro-framework (Python Based), Jinja2, mySQL. Flask was ideal for this small project as there are many extensions such as FlaskSQLAlchemy which I also used in the project. In the 'requirements.txt' file, all extextensions used can be seen. 

## Initial Project Planning
To begin with, I used Kanbanize to create a KANBAN board. This helped to organise and visualise tasks throughout the duration of the project. My inital KANBAN board can be seen below:
![image](https://user-images.githubusercontent.com/77271496/107160200-afc20c80-698c-11eb-9051-363fe9ff9ce4.png)

The initial board was created before I had fully decided on my project idea, so I listed generic tasks without much depth to begin with. As you read along, you will find how this board slowly evolves, with the number of tasks increasing as well as the number of User Stories.


Once I had decided on my project idea, I then went on to update my board as I went along and completed some of the tasks, which resulted with the following: 
![image](https://user-images.githubusercontent.com/77271496/107160971-6d4efe80-6991-11eb-9221-2d0a8d394b08.png)

As can be seen, the sections are split into REQUESTED - tasks which should be completed to achieve MVP, IN PROGRESS - tasks which are currently being worked on and DONE - tasks which have been completed. Each 'card' has subtasks which I can also tick as I go along. These subtasks can help to further divide the tasks into smaller tasks, to provide a more clear and coherent structure to the project process.

## ERD Diagram
As mentioned in my KANBAN Board, I had to create ERD Diagrams. ERD stands for Entity Relationship Diagram. The purpose of an ERD is to show the relationship between 2 or more tables within a database. I hosted my database on an AWS EC2 instance, on which I had mySQL installed. Within this database, I created 2 tables, which can be seen in my 'models.py' file. To initially populate my databases, I wrote some code within my 'create.py' file, all accessible within this repository. 

Below can be seen the ERD:

![image](https://user-images.githubusercontent.com/77271496/107164266-3fc08000-69a6-11eb-82fb-81c9b6dedb91.png)

I used the same ERD diagram throughout the project as it covered the MinimumViableProduct of the project. At a later date, this can be updated if need be. Currently, this diagram is sufficient for the content of the application. 

As can be seen, my ERD consists of 2 tables, one for a Football Team and one for Players. There is a one to many relationship between the tables, 1 team for many players within that team. The ID of the Football Team (or 'Parent' as I named in my 'models.py') is the Primary Key, whilst the ID of the Player is the Foreign Key. This pair establishes the relationship between the two tables. Each new Player added to a Parent will have a new ID, so that querying is a little easier when adding, editing or deleting the Player. 

The Football Team table consists of the teams name and league, whilst the Player table consists of name, age and position. The name, league and position fields are all String Fields, whilst the age field is for Integer, all of which are nullable.  

## Initial Risk Assessment
In the earlier stages of the project, I created the following Risk Assessment to the best of my knowledge at the time. Again, this changed over time, as the more deep you delve into coding, the higher the chances of error get and the more you learn about potential risks. 

![image](https://user-images.githubusercontent.com/77271496/107168011-5ec50f00-69b2-11eb-98f8-0262b2623d82.png)
As you can see, during the initial stages, the risks assosciated with programming weren't too apparent to myself, and I could only think of some very generic, basic issues and fixes. However, as I grew deeper into the project and my knowledge expanded, other inside issues became more apparent and any mitigating actions more technical, as can be seen below.
![image](https://user-images.githubusercontent.com/77271496/107167817-ba42cd00-69b1-11eb-8f73-468dd9f8a821.png)

## CI Pipeline
Below is a diagram of the CI Pipeline I have tried to follow in this project. This Pipeline demonstrates the relationship between the software used and how they all interconnect. The main clog of the Pipeline is CI Server 'Jenkins', which is a free to use and user friendly server, and allows for automated building and testing of the application. This allows for a thorough checking of the app at each increment. 

![image](https://user-images.githubusercontent.com/77271496/107166445-f5db9800-69ad-11eb-8f19-416807b8fcb7.png)
The top of the Pipeline exhibits the links between GitBash, GitHub and Kanbanize. GitBash was used to run linux commands (e.g. SSH to AWS, pip3 install etc.) as well as using the vim editor to create all of the Python files with Flask. Every time a certin task was completed, it was then pushed to the Version Control System. In this case, I used GitHub, as it is free and open source, and can be viewed publicly. GitHub served as the repository for the project, as well as maintaning all changes made within branches to make debugging a little easier. 

The middle of the Pipeline delves more into the DevOps side of things. Using a webhook, the repository within GitHub can be pulled into the Jenkins server automatically with each update. The Jenkins server then 'builds' the application, using Pytest to check that the defined tests are still passing with each new update, whilst the Pytest Coverage Report depicts a percetage to show how much of the code has been covered. If the Jenkins build returns as a fail, it means that all tests have not been passed, or that the app cannot be run. This then returns an error which is debugged in the VSC. Anything generated from this build returns a HTML report, which is the 'artefact' for the build. 

The last section of the Pipeline connects the Artefact to AWS, a human tester and then if all is well, it is finally pushed to a live environment, also on AWS. Once the artefact is checked, it is run on the AWS environment. If this is done succesfully, it is then tested by a human to check quality, and if they approve, it is pushed to a live envioronment. The difference between the test envioronment and live environment is that the test environment contains a debug mode, to be able to generate error reports.

## Testing
For this project, the testing will be handled using Pytest, which is a Python based testing framework which tests funcitonality. It is widely extensible with a variety of seperate modules which can be installed onto it. One of the modules used in this project is Pytest-cov, which is an extension that allows for a calculation of percentages to show how much of a file has been tested. Pytest-cov allows for the generation of a HTML report, which is perfect for Jenkins as it can read this file easily. The type of testing to be used is Unit Testing, where the CRUD functionality would be tested.

The test code which was written for this project was purely made to test the CRUD functionality, making sure that each function/URL did what it was supposed to do, whether it be create, read, update or delete. Within my test file, I created test databases with test tables, so that the actual database doesn't get tampered with, and rather some dummy databases. I started with some simple tests applied to each page, which was just able to prove that each page could be reached successfully without returning an error. Next, I tested the contents of the home page, to make sure that certain data which was meant to be shown, would be shown. I then went on to test the update and delete functionalities, making sure that certain data was edited upon request and then deleted upon request.

Below can be seen the report from the Jenkins console output:
![image](https://user-images.githubusercontent.com/77271496/107177480-da7e8600-69c9-11eb-8898-b6ed8eee9069.png)

As you can see, 86% of my files are covered, which suggests a good depth of the application has been tested, making it relatively successful test.

##Front End
The front end of my project is rather basic, using basic HTML. This is because the visual side wasn't a very big factor for this particular project, rather the functionality was most important. It is black and white text, with titles and all data presented in a tabular form, as can be seen below. 

![image](https://user-images.githubusercontent.com/77271496/107178750-bf614580-69cc-11eb-8c62-20d26c3d46ba.png)

an to check quality, and if they approve, it is pushed to a live envioronment. The difference between the test envioronment and live environment is that the test environment contains a debug mode, to be able to generate error reports.

## Testing
For this project, the testing will be handled using Pytest, which is a Python based testing framework which tests funcitonality. It is widely extensible with a variety of seperate modules which can be installed onto it. One of the modules used in this project is Pytest-cov, which is an extension that allows for a calculation of percentages to show how much of a file has been tested. Pytest-cov allows for the generation of a HTML report, which is perfect for Jenkins as it can read this file easily. The type of testing to be used is Unit Testing, where the CRUD functionality would be tested.

The test code which was written for this project was purely made to test the CRUD functionality, making sure that each function/URL did what it was supposed to do, whether it be create, read, update or delete. Within my test file, I created test databases with test tables, so that the actual database doesn't get tampered with, and rather some dummy databases. I started with some simple tests applied to each page, which was just able to prove that each page could be reached successfully without returning an error. Next, I tested the contents of the home page, to make sure that certain data which was meant to be shown, would be shown. I then went on to test the update and delete functionalities, making sure that certain data was edited upon request and then deleted upon request.

Below can be seen the report from the Jenkins console output:
![image](https://user-images.githubusercontent.com/77271496/107177480-da7e8600-69c9-11eb-8898-b6ed8eee9069.png)

As you can see, 86% of my files are covered, which suggests a good depth of the application has been tested, making it relatively successful test.

##Front End
The front end of my project is rather basic, using basic HTML. This is because the visual sid
e wasn't a very big factor for this particular project, rather the functionality was most imp
ortant. It is black and white text, with titles and all data presented in a tabular form, as
can be seen below.

![image](https://user-images.githubusercontent.com/77271496/107178750-bf614580-69cc-11eb-8c62-20d26c3d46ba.png)


![image](https://user-images.githubusercontent.com/77271496/107178807-e6b81280-69cc-11eb-8c25-96871046f017.png)

![image](https://user-images.githubusercontent.com/77271496/107178845-f5062e80-69cc-11eb-8c5f-57b8294c6789.png)

##Evaluation

### Difficulties
The main difficulty with this project was the timing in which we had to complete it. Within a week we had to create the app and all the documentation; this was difficult as we had issues regarding the Cloud Servers. We used GCP initially and I started some of my work there, however, due to the small computer sizes, the servers would crash. Therefore, I had to swith to using AWS EC2 instance instead, this took a little bit of getting used to. I am also using free trial status, so if I have to stop the instance, the process would not be automated.

Other difficulties I encountered were with the Primary Keys and Foreign Keys of my 2 tables. I used 'id' for both PK and FK, so when it came to referencing them in my routes, it sometimes got confusing and I would think an outside person would also get confused by this initially.

### Improvements
If I was to do anything differently, I would use AWS from the beginning as I know it is capable of hosting all the tools we needed to build and deploy this app. Other improvements could include making the app more eye-catching for the user, with more advanced Front-End code. I could perhaps add further tables to differentiate Teams by their Leagues, rather than have them all on the same table.

### Licensing 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

This permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Acknowledgements
I would like to thank my trainers for providing me with a good understanding and quality of teaching before and during the project. Special mentions to Luke Benson, Raji Kolluru and Peter Rhodes. Additionally, thank you to all the cohort members for providing continious and making this learning environment fun and friendly.
