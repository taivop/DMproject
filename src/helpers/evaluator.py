import numpy as np
from helpers.datahandler import DataHandler

class Evaluator():

    test_genders = np.asarray([[0],[1],[1]])

    genders_test = None
    ages_test = None
    diagnoses_test = None

    genders_all = None
    ages_all = None
    diagnoses_all = None

    handler = None

    def __init__(self):
        # load test data
        self.handler = DataHandler()
        self.genders_test, self.ages_test, self.diagnoses_test = self.handler.getTestData()
        self.genders_all, self.ages_all, self.diagnoses_all = self.handler.getAllData()

    def genders_fscore(self, predictions):
        foo = 0
        # not very useful in this case, maybe implement later
        #return fscore, precision, recall



    def accuracy(self, predicted_vals, true_vals):
        """ Get the accuracy given predicted classes and true classes.
        """
        correct = 0

        for i in range(0,len(predicted_vals)):
            if predicted_vals[i] == true_vals[i]:
                correct += 1

        return correct / predicted_vals.shape[0]

    def acc_genders_all(self, predicted_vals):
        return self.accuracy(predicted_vals, self.genders_all)

