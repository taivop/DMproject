import numpy as np
from helpers.datahandler import DataHandler

class Evaluator():

    test_genders = np.asarray([[0],[1],[1]])

    genders_test = None
    ages_test = None
    diagnoses_test = None

    def __init__(self):
        # load test data
        handler = DataHandler()
        self.genders_test, self.ages_test, self.diagnoses_test = handler.getTestData()

    def genders_fscore(self, predictions):
        foo = 0
        # not very useful in this case, maybe implement later
        #return fscore, precision, recall





    def genders_accuracy(self, predictions):
        size = predictions.shape[0]
        print(predictions == self.test_genders)
        acc = np.sum(predictions == self.test_genders) / size

        return acc

