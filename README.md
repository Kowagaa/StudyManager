# StudyManager
Allows for picking of random topics to study and tracking of performance across various topics
# HOW TO USE:
- execute setup.py to append to the df;
- the program will ask you to input three values
- Subject is the subject the topic is related to
- Topic is self explanatory
- Weight mod is a multiplier of the chances the topic has to appear (Note: dont change this value if you're bad at said topic as this change is permanent. instead; once you're done with a subject, change the avg performance to a lower value in order to increase its chances to appear (as of version 1.0 this isnt available yet)
- The controller has 4 sets of code with one function each; the name of the function is how ill refer to each one:
- loadStartDF is for loading the df created with setup.py (Note: executing this will reset the values to whatever is on startingdf.csv
- calcWeight recalculates the values of the weights of each record; I recommend doing so after each pickRandom
- pickRandom allows for the picking of a random record with bias of WEIGHT (equal to WEIGHT MOD / (AVG PERFORMANCE * (TIMES STUDIED + 1)) and the optional increment of TIMES STUDIED for said record
- subtractTimeStudied allows for the subtraction by 1 of any record for TIME STUDIED
