Processing data set from New York City traffic website using Hadoop MapReduce to yield the count of vehicles 
involved in an incident and analyze the type of vehicles, which contributed to a maximum number of accidents.
Technology used: AWS, Apache Hadoop, Python


Steps/commands used to run the files on Hadoop

1. Copy the mapper.py and reducer.py to your home directory

2. Run the below command by replacing the $user with your username

   The input data file path for this project is /data/nyc/nyc-traffic.csv

   hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
	-file /home/$user/mapper.py    -mapper /home/$user/mapper.py \
	-file /home/$user/reducer.py   -reducer /home/$user/reducer.py \
	-input /data/nyc/nyc-traffic.csv  -output /user/$user/outputresult

3. Access the results file using the following command 

	hadoop fs -cat /user/$user/outputresult/*
	
	




