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
    -The dataset contains 494021 rows of entries and 42 attributes.
    -The dataset contain a total of 24 training attack types, with an additional 14 types in the test dataset only.
    
Approach:
    
    -First we have started with some Exploratory Data Analysis(EDA) using pandas to see what type of dataset we are working with 
     and get familiar with it. And to see what are the various attributes considered in the dataset.
    -Then accordingly we will build a machine learning model classifier to classify the entries into Normal or Attack.
    -We will be using Scikit-learn python machine learning module to implement the project.
    
Start:

    1.First run icmp_attack.ipynb file present in jupyter-notebooks directory.
        
        - Here we are assigning all the attributes names to the dataset. And refinig the dataset with Exploratory Data Analysis    (EDA).

        - We are separating all the icmp protocol based data into different dataset and naming it revised_icmp_dataset.

        - Then out of all the features we are only selecting 7 features they are:
            ["duration","service","src_bytes","wrong_fragment","count","urgent","num_compromised","srv_count"]

        -Then we are spliting the dataset into training and testing dataset with the test_size of 30% of original datatset.

        -Then we training the dataset with different algorithms they are:
            [LogisticRegression, KNeighborsClassifier,MLPClassifier,DecisionTreeClassifier]

        
    2.Then run train.py file present in train_test_python_files directory.

        - Here we taking user input for what type of user wants to train the data on.

        - Training the model "python train.py icmp 0" this will actually train the data set on icmp protocol with the KNN model.

        - TRAINING OUR MODEL "python train.py icmp 1" this will actually train the data set on icmp protocol with the      DecisionTreeClassifier model.