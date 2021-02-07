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

Before I fully understood the scope of the project, I created the following ERD:
