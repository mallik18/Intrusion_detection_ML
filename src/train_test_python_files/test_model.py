import numpy as np
import sys
import pickle
    
def icmp_test(attributes):
    model = pickle.load(open("/home/noroot/Documents/final_year_project/Intrusion_detection_ML/src/train_test_python_files/models_after_trained/icmp_data.sav", 'rb'))
    result = model.predict([attributes])
    print(result)


if __name__ == "__main__":
    if sys.argv[1] == "icmp": 
        icmp_test(sys.argv[2:])
    else:
        sys.exit("Incorrect protocol has been chosen for testing. Try again.")