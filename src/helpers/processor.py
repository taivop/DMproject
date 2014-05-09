from helpers.diagnosis import Diagnosis
import numpy as np

class Processor():

    diag = None

    def __init__(self):
        # Create a new Diagnosis object (loads necessary mappings from file on creation).
        self.diag = Diagnosis()



    # Read in data from original file to numpy array.
    def getArrayFromFile(self):
        filepath = '../data/age_predict_data.txt'
        data = np.loadtxt(filepath, delimiter='\t', skiprows=161430, usecols=[],
                          dtype={'names': ('gender', 'age', 'diagnoses', 'prescriptions'),'formats': ('S1', 'i3', 'object', 'object')})

        # Filter rows with no diagnoses and no recipes
        toBeKept = []
        for ii in range(1,len(data)):
            row = data[ii]
            # if both diagnoses and prescriptions exist, keep the row
            if(row[2] != "b'NONE'" and row[3] != "b'NONE'"):
                toBeKept.append(ii)

        filtered = data[toBeKept]
        print("Filtering done.")
        arr = filtered.view(np.ndarray).reshape(len(filtered), -1)


        # create new empty array of zeros to keep diagnoses
        diagnoses = np.zeros((arr.shape[0], self.diag.numberOfDiagnoses),np.dtype('b1'))

        for i in range(0,arr.shape[0]):
            codeString = arr[i]['diagnoses'][0].strip("b'")
            print(codeString)
            diagnoses[i,self.diagnosisCodesToIndices(codeString)] = 1;

        print(sum(sum(diagnoses)))

        return

    # Get one string of diagnoses (e.g. 'A01|Z00|R12') and turn it into a binary vector (for each diagnosis: 1 if exists
    #  in string, 0 otherwise).
    def diagnosisCodesToIndices(self, codeString):

        length = self.diag.numberOfDiagnoses
        vector = np.zeros((1, length),np.dtype('b1'))

        # Split into a list of diagnosis codes
        codes = codeString.strip().split('|')
        # Make every diagnosis in the list basic and turn it into the corresponding diagnosis id
        ids = [self.diag.getIdFromCode(self.diag.diagnosisCodeToBasic(x)) for x in codes]

        # Set vector values to 1 for ids for which a diagnosis existed
        #vector[0,ids] = 1

        return ids





