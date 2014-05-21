
# Do a quick test on the Diagnosis class

from helpers.diagnosis import Diagnosis

# Create a Diagnosis class. It loads the necessary dictionaries from disk.
diag = Diagnosis()

print('We have {0} different diagnoses.'.format(diag.numberOfDiagnoses))

print('id {0} -> code {1}'.format(156, diag.getCodeFromId('156')))
print('code {0} -> id {1}'.format('B82', diag.getIdFromCode('B82')))
print('id {0} -> label "{1}"'.format(156, diag.getLabelFromId('156')))
print('code {0} -> label "{1}"'.format('B82', diag.getLabelFromCode('B82')))

print(diag.diagnosisCodeIsBasic('A04.5'))
print(diag.diagnosisCodeToBasic('A04.5'))
print(diag.diagnosisCodeToBasic('A04,5'))
print(diag.diagnosisCodeIsBasic('A00-08'))
#print(diag.diagnosisCodeToBasic('A00-08')) # should throw an exception