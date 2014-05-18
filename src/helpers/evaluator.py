import numpy as np

class Evaluator():

    test_genders = np.asarray([[0],[1],[1]])

    def __init__(self):
        0
        # load test data

    def genders_fscore(self, predictions):
        foo = 0
        # not very useful in this case, maybe implement later
        #return fscore, precision, recall





    def genders_accuracy(self, predictions):
        size = predictions.shape[0]
        print(predictions == self.test_genders)
        acc = np.sum(predictions == self.test_genders) / size

        return acc

