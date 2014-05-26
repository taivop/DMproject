

from helpers.datahandler import DataHandler

handler = DataHandler()

handler.originalFileToProcessedFiles()

genders, ages, diagnoses = handler.getTrainingData()

print(genders[1,:])
print(ages[1,:])
print(diagnoses[1,:])

print(ages)


test_arr = [[1, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
#print(handler.hasAtLeastNDiagnoses(test_arr, 4))