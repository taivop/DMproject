import numpy as np

from helpers.evaluator import Evaluator


e = Evaluator()

p = np.asarray([[1],[1],[0]])

print(e.genders_fscore(p))