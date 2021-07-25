import numpy as np
import sys
import pickle
    
def icmp_test(attributes):
    model = pickle.load(open("/home/mk/Documents/final_year_project/Intrusion_detection_ML/src/train_test_python_files/models_after_trained/icmp_data1.sav", 'rb'))
    result = model.predict([attributes])
    if result[0] == 0:
        print("The Input is Normal")
    else:
        print("The Input is Attack")

if __name__ == "__main__":
    if sys.argv[1] == "icmp": 
        icmp_test(sys.argv[2:])
    else:
        sys.exit("Incorrect protocol has been chosen for testing. Try again.")
