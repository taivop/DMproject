from helpers.diagnosis import Diagnosis
import numpy as np

class Processor():

    diag = None

    def __init__(self):
        # Create a new Diagnosis object (loads necessary mappings from file on creation).
        self.diag = Diagnosis()



    # Read in data from original file to numpy array.
    def originalFileToProcessedFiles(self):
        # 161430
        filepath = '../data/age_predict_data.txt'
        data = np.loadtxt(filepath, delimiter='\t', skiprows=0, usecols=[],
                          dtype={'names': ('gender', 'age', 'diagnoses', 'prescriptions'),'formats': ('S1', 'i3', 'object', 'object')})

        # Filter rows with no diagnoses and no recipes
        toBeKept = []
        for ii in range(1,len(data)):
            row = data[ii]
            # if BOTH diagnoses and prescriptions exist, keep the row
            if row[2] != "b'NONE'" and row[3] != "b'NONE'":
                toBeKept.append(ii)

        filtered = data[toBeKept]
        arr = filtered.view(np.ndarray).reshape(len(filtered), -1)

        # Create separate arrays for ages, sexes, diagnoses and prescriptions
        ages = arr['age']

        # create empty arrays and populate with data
        genders = np.zeros((arr.shape[0], 1), np.dtype('b1'))
        diagnoses = np.zeros((arr.shape[0], self.diag.numberOfDiagnoses),np.dtype('b1'))

        for i in range(0,arr.shape[0]):
            codeString = arr[i]['diagnoses'][0].strip("b'")
            indices = self.diagnosisCodesToIndices(codeString)
            diagnoses[i, indices] = 1
            genderStr = str(arr[i]['gender'][0]).strip("b'")
            genders[i] = (genderStr == 'M')


        # Save arrays to files.
        np.save('../data/processed/genders.npy', genders)
        np.save('../data/processed/ages.npy', ages)
        np.save('../data/processed/diagnoses.npy', diagnoses)

        print('Files saved.')


        return

    # Get one string of diagnoses (e.g. 'A01|Z00|R12') and turn it into a binary vector (for each diagnosis: 1 if exists
    #  in string, 0 otherwise).
    def diagnosisCodesToIndices(self, codeString):

        length = self.diag.numberOfDiagnoses
        vector = np.zeros((1, length),np.dtype('b1'))

        # Split into a list of diagnosis codes
        codes = codeString.strip().split('|')


        # Make every diagnosis in the list basic and turn it into the corresponding diagnosis id
        ids = []
        for code in codes:
            try:
                id = self.diag.getIdFromCode(self.diag.diagnosisCodeToBasic(code))
                ids.append(id)
            except KeyError:    # if there is no such diagnosis, let's not take it into account
                pass


        # Set vector values to 1 for ids for which a diagnosis existed
        #vector[0,ids] = 1

        return ids



