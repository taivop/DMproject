from helpers.diagnosis import Diagnosis
import numpy as np

class DataHandler():

    diag = None

    def __init__(self):
        # Create a new Diagnosis object (loads necessary mappings from file on creation).
        self.diag = Diagnosis()


    # Read in data from original file to numpy array.
    def originalFileToProcessedFiles(self):
        # 161430
        filepath = '../data/other/age_predict_data.txt'
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
            indices = self.diag.diagnosisCodesToIndices(codeString)
            diagnoses[i, indices] = 1
            genderStr = str(arr[i]['gender'][0]).strip("b'")
            genders[i] = (genderStr == 'M')

        # partition into training set (80%) and test set (20%)
        train_size = int(0.8 * arr.shape[0])
        indices = np.random.permutation(arr.shape[0])
        train_ind = indices[:train_size]
        test_ind = indices[train_size:]

        print('Training set size: {0} examples'.format(train_ind.shape[0]))
        print('Test set size: {0} examples'.format(test_ind.shape[0]))

        # Save arrays to files.
        np.save('../data/processed/genders_train.npy', genders[train_ind,:])
        np.save('../data/processed/ages_train.npy', ages[train_ind,:])
        np.save('../data/processed/diagnoses_train.npy', diagnoses[train_ind,:])

        np.save('../data/processed/genders_test.npy', genders[test_ind,:])
        np.save('../data/processed/ages_test.npy', ages[test_ind,:])
        np.save('../data/processed/diagnoses_test.npy', diagnoses[test_ind,:])

        np.save('../data/processed/train_indices.npy', train_ind)
        np.save('../data/processed/test_indices.npy', test_ind)


        print('Files saved.')


        return


    # Read in training data from files and return the corresponding arrays
    def getTrainingData(self):
        genders_train = np.load('../data/genders_train.npy')
        ages_train = np.load('../data/ages_train.npy')
        diagnoses_train = np.load('../data/diagnoses_train.npy')

        return genders_train, ages_train, diagnoses_train

    # Read in test data from files and return the corresponding arrays
    def getTestData(self):
        genders_test = np.load('../data/genders_test.npy')
        ages_test = np.load('../data/ages_test.npy')
        diagnoses_test = np.load('../data/diagnoses_test.npy')

        return genders_test, ages_test, diagnoses_test

    def getTrainingIndices(self):
        return np.load('../data/train_indices.npy')

    def getTestIndices(self):
        return np.load('../data/test_indices.npy')




