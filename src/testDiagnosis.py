
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

codeString = 'B34.9|E11|G45|G56.0|I10|I11|I11.9|J04|J20|J34.2|K35|K35.9|M10|M25.8|M54.9|M72.0|M77.2|M77.3|M79.6'
diag.diagnosisCodesToIndices(codeString)