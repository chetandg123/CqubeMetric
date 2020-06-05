CqubeMetric is a test script which is used to calculate the metrics, by using the queries and json files(s3 output bucket json files).
This provides the report based on the student attendance report,crc and semester
To run this test script,json_data should be downloaded from s3 output bucket and stored in the local machine.

Fill the Details in crc_ini 
[url] 
domain=                                 # ex : https://cqube.tibilprojects.com/api/ or http://<ip>:4200/api/
email=                                  # Enter email address for login to cqube application
password=                               # Enter password for login to cqube application

Fill the Details in Database.ini

[pgsql] 
host=                                   # hostname for connecting to postgres (ex : <ip> )
port=5432                               # Port number for postgres
database=                               # Enter the Database name for postgres which is provided in the config.yml while installing
user=                                   # Enter the username name for postgres which is provided in the config.yml while installing
password=                               # Enter the password for postgres which is provided in the config.yml while installing

Fill the Details in json_data.ini

[jsondata] 
district_attendance_2019_8=             #Download the file from s3 output bucket and provide the Absolute path
district_attendance_2019_9=             #Download the file from s3 output bucket and provide the Absolute path
district_attendance_2019_10=            #Download the file from s3 output bucket and provide the Absolute path

block_attendance_2019_8=                #Download the file from s3 output bucket and provide the Absolute path
block_attendance_2019_9=                #Download the file from s3 output bucket and provide the Absolute path
block_attendance_2019_10=               #Download the file from s3 output bucket and provide the Absolute path

cluster_attendance_2019_8=              #Download the file from s3 output bucket and provide the Absolute path
cluster_attendance_2019_9=              #Download the file from s3 output bucket and provide the Absolute path
cluster_attendance_2019_10=             #Download the file from s3 output bucket and provide the Absolute path

school_attendance_2019_8=               #Download the file from s3 output bucket and provide the Absolute path
school_attendance_2019_9=               #Download the file from s3 output bucket and provide the Absolute path
school_attendance_2019_10=              #Download the file from s3 output bucket and provide the Absolute path

district_semester=                      #Download the file from s3 output bucket and provide the Absolute path  
block_semester=                         #Download the file from s3 output bucket and provide the Absolute path
cluster_semester=                       #Download the file from s3 output bucket and provide the Absolute path
school_semester=                        #Download the file from s3 output bucket and provide the Absolute path

Run the test script by using the run_tests.py 

Location of the file CqubeMetric -> RunTestScripts -> run.tests.py

Note : Recommended Environment for running the test scripts are ubuntu 18.0.4.LTS or above and open the Project in the Pycharm IDE.
