# Malicious Activities Detection Using Machine Learning

Dataset link : https://www.kaggle.com/galaxyh/kdd-cup-1999-data

Its a piece of code that is used to detect intrusions in a network from unauthorized users.
The connections recoreded in the dataset is a sequence of TCP packets.

Attacks can be one of the following mentioned:

    -DOS: denial-of-service, e.g. syn flood;
    -R2L: unauthorized access from a remote machine, e.g. guessing password;
    -U2R:  unauthorized access to local superuser (root) privileges, e.g., various ``buffer overflow'' attacks;
    -probing: surveillance and other probing, e.g., port scanning.

Info on Dataset:

    -We have used reduced dataset i.e.,(10 percent dataset of the original dataset).
    -The dataset contains 494021 rows of entries.
    -The dataset contain a total of 24 training attack types, with an additional 14 types in the test dataset only.
    
Approach:
    
    -First we have started with some Exploratory Data Analysis(EDA) using pandas to see what type of dataset we are working with 
     and get familiar with it. And to see what are the various attributes considered in the dataset.
    -Then accordingly we will build a machine learning model classifier to classify the entries into Normal or Attack.
    -We will be using Scikit-learn python machine learning module to implement the project.
    