from helpers.datahandler import DataHandler

handler = DataHandler()

# get training set
genders, ages, diagnoses = handler.getTrainingData()

# get test set
# although this shouldn't be necessary since the Evaluator class loads test data and calculates necessary measures
genders_test, ages_test, diagnoses_test = handler.getTestData()