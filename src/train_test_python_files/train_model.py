import numpy as np
import pandas as pd
import sys
import pickle
from sklearn.neighbors import KNeighborsClassifier


print('TRAINING OUR MODEL "python train.py icmp 0" this will actually train the data set on icmp protocol with the KNN model.')
print('If you wish to use the second model type "python train.py icmp 1" it uses DecisionTreeClassifier.')

df = pd.read_csv("/home/noroot/Documents/final_year_project/Intrusion_detection_ML/dataset/revised_kddcup_dataset.csv",index_col=0)

def train_icmp(df, classifier=0):

    icmp_df = df[df.loc[:,"protocol_type"] == "icmp"]
    icmp_feat = ["duration","service","src_bytes","wrong_fragment","count","urgent","num_compromised","srv_count"]
    icmp_target = "result"
    X = icmp_df.loc[:,icmp_feat]
    y = icmp_df.loc[:,icmp_target]
    
    X['duration'] = X['duration'].astype('float')
    X['src_bytes'] = X['src_bytes'].astype('float')
    X['wrong_fragment'] = X['wrong_fragment'].astype('float')
    X['count'] = X['count'].astype('float')
    X['urgent'] = X['urgent'].astype('float')
    X['num_compromised'] = X['num_compromised'].astype('float')
    X['srv_count'] = X['srv_count'].astype('float')
    
    classes = np.unique(y)
    for i in range(len(classes)):
        if i == 2:
            X = X.replace(classes[i], 0)
        else:
            X = X.replace(classes[i], 1)

    #turning the service attribute to categorical values
    X = X.replace("eco_i",-0.1)
    X = X.replace("ecr_i",0.0)
    X = X.replace("tim_i",0.1)
    X = X.replace("urp_i",0.2)
    

    y = icmp_df.loc[:,icmp_target] #updating the y variables
    print("Data preprocessing done.")

    #choose KNN if classifier == 0 else choose ID3
    if str(classifier) == "0":
        k = 3
        model = KNeighborsClassifier(n_neighbors=k)
    elif str(classifier) == "1":
        from sklearn.tree import DecisionTreeClassifier
        model = DecisionTreeClassifier()
    else:
        print("Wrong model chosen! Placing default model 0 to model training!")
        k = 3
        model = KNeighborsClassifier(n_neighbors=k)
    
    
    #fitting our model
    model.fit(X,y)
    print("The model has been fit.")
    
    print("Save the fitted model?(y/n):")
    choice = input().lower()
    if choice == "y":
        pickle.dump(model, open("/home/noroot/Documents/final_year_project/Intrusion_detection_ML/src/train_test_python_files/models_after_trained/icmp_data.sav", 'wb'))




if __name__ == "__main__":
    if str(sys.argv[1]) == "icmp":
        train_icmp(df,sys.argv[2])
    else:
        print("Did not select correct protocol. Try again.")
        