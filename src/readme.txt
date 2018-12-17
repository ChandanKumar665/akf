Warning! 

Before running the app we have to migrate our Models classes as the DB table into
our Database.
Db used: mysql
check setting.py for DB setup
Follow these commands steps:
-- cd project_location\akf\src
-- py manage.py makemigrations akf_app
-- py manage.py makemigrations
-- py manage.py migrate

The above steps will help to create all the required tables in the DB.
For runnig the server:
-- py manage.py runserver

It is highly recommended to use raw content url of file and first import( 
	https://raw.githubusercontent.com/klpdotorg/interview-challenge/master/boundaries.csv)
boundries date file and then 
(https://raw.githubusercontent.com/klpdotorg/interview-challenge/blob/master/gp_contests.csv)
student_report file url because student_report table contains foreign key (distric_id) refenrence to geo_info table.
Other wise you will get an error 

