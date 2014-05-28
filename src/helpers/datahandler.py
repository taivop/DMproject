from helpers.diagnosis import Diagnosis
from helpers.age import Age
import numpy as np

class DataHandler():

    diag = None

    def __init__(self):
        # Create a new Diagnosis object (loads necessary mappings from file on creation).
        self.diag = Diagnosis()


    # Read in data from original file to numpy array.
    def originalFileToProcessedFiles(self):
        # 161430
        filepath = '../../data/other/age_predict_data.txt'
        data = np.loadtxt(filepath, delimiter='\t', skiprows=0, usecols=[],
                          dtype={'names': ('gender', 'age', 'diagnoses', 'prescriptions'),'formats': ('S1', 'i3', 'object', 'object')})

        # Filter rows with no diagnoses and no recipes
        toBeKept = []
        for ii in range(1,len(data)):
            row = data[ii]
            # if diagnoses exist, keep the row
            if row[2] != "b'NONE'":
                toBeKept.append(ii)

        filtered = data[toBeKept]
        arr = filtered.view(np.ndarray).reshape(len(filtered), -1)

        # Create separate arrays for ages, sexes, diagnoses and prescriptions
        ages = np.zeros((arr.shape[0],1))

        agehandler = Age()

        # create empty arrays and populate with data
        genders = np.zeros((arr.shape[0], 1), np.dtype('b1'))
        diagnoses = np.zeros((arr.shape[0], self.diag.numberOfDiagnoses),np.dtype('b1'))

        for i in range(0,arr.shape[0]):
            codeString = arr[i]['diagnoses'][0].strip("b'")
            indices = self.diag.diagnosisCodesToIndices(codeString)
            diagnoses[i, indices] = 1
            genderStr = str(arr[i]['gender'][0]).strip("b'")
            genders[i] = (genderStr == 'M')
            ages[i] = agehandler.getBinFromAge(int(arr[i]['age'][0]))

        # partition into training set (80%), validation set (20%) and test set (20%)
        train_size = int(0.6 * arr.shape[0])
        indices = np.random.permutation(arr.shape[0])
        train_ind = indices[:train_size]
        test_size = int(0.2 * arr.shape[0])
        test_ind = indices[train_size:train_size+test_size]
        valid_ind = indices[train_size+test_size:]

        print('Training set size: {0} examples'.format(train_ind.shape[0]))
        print('Test set size: {0} examples'.format(test_ind.shape[0]))
        print('Validation set size: {0} examples'.format(valid_ind.shape[0]))

        # Save arrays to files.
        np.save('../../data/processed/genders.npy', genders)
        np.save('../../data/processed/ages.npy', ages)
        np.save('../../data/processed/diagnoses.npy', diagnoses)

        np.save('../../data/processed/genders_train.npy', genders[train_ind,:])
        np.save('../../data/processed/ages_train.npy', ages[train_ind,:])
        np.save('../../data/processed/diagnoses_train.npy', diagnoses[train_ind,:])

        np.save('../../data/processed/genders_test.npy', genders[test_ind,:])
        np.save('../../data/processed/ages_test.npy', ages[test_ind,:])
        np.save('../../data/processed/diagnoses_test.npy', diagnoses[test_ind,:])

        np.save('../../data/processed/genders_validation.npy', genders[valid_ind,:])
        np.save('../../data/processed/ages_validation.npy', ages[valid_ind,:])
        np.save('../../data/processed/diagnoses_validation.npy', diagnoses[valid_ind,:])

        np.save('../../data/processed/train_indices.npy', train_ind)
        np.save('../../data/processed/test_indices.npy', test_ind)

        print('Files saved.')
        return

    def hasAtLeastNDiagnoses(self, array, n):
        """ Return a vector of same length as # of rows in n. k-th element is True iff k-th row in array contains at
         least n diagnoses.
        """
        s = np.sum(array, axis=1)
        return s >= n

    def removeLessThanNDiagnoses(self, data_tuple, n):
        genders, ages, diagnoses = data_tuple

        mask = np.squeeze(self.hasAtLeastNDiagnoses(diagnoses, n))

        genders2 = genders[mask]
        ages2 = ages[mask]
        diagnoses2 = diagnoses[mask,:]

        return genders2, ages2, diagnoses2


    def removeAgesAbove100(self, data_tuple):
        genders, ages, diagnoses = data_tuple

        mask = np.squeeze(np.asarray(ages <= 100))

        genders2 = genders[mask]
        ages2 = ages[mask]
        diagnoses2 = diagnoses[mask,:]

        return genders2, ages2, diagnoses2


    # Read in and return whole dataset
    def getAllData(self):
        genders = np.load('../../data/genders.npy')
        ages = np.load('../../data/ages.npy')
        diagnoses = np.load('../../data/diagnoses.npy')

        return genders, ages, diagnoses

    # Read in training data from files and return the corresponding arrays
    def getTrainingData(self):
        genders_train = np.load('../../data/genders_train.npy')
        ages_train = np.load('../../data/ages_train.npy')
        diagnoses_train = np.load('../../data/diagnoses_train.npy')

        return genders_train, ages_train, diagnoses_train

    # Read in test data from files and return the corresponding arrays
    def getTestData(self):
        genders_test = np.load('../../data/genders_test.npy')
        ages_test = np.load('../../data/ages_test.npy')
        diagnoses_test = np.load('../../data/diagnoses_test.npy')

        return genders_test, ages_test, diagnoses_test

    def getValidationData(self):
        genders_validation = np.load('../../data/genders_validation.npy')
        ages_validation = np.load('../../data/ages_validation.npy')
        diagnoses_validation = np.load('../../data/diagnoses_validation.npy')

        return genders_validation, ages_validation, diagnoses_validation

    def getTrainingIndices(self):
        return np.load('../data/train_indices.npy')

    def getTestIndices(self):
        return np.load('../data/test_indices.npy')