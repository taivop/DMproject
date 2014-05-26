

from helpers.datahandler import DataHandler

handler = DataHandler()

handler.originalFileToProcessedFiles()

genders, ages, diagnoses = handler.getTrainingData()

print(genders[1,:])
print(ages[1,:])
print(diagnoses[1,:])

print(ages)