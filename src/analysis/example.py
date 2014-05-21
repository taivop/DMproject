from helpers.datahandler import DataHandler

handler = DataHandler()

# get training set
genders, ages, diagnoses = handler.getTrainingData()

# get test set
genders_test, ages_test, diagnoses_test = handler.getTestData()