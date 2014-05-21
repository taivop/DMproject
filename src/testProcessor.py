

from helpers.processor import Processor



codeString = 'B34.9|E11|G45|G56.0|I10|I11|I11.9|J04|J20|J34.2|K35|K35.9|M10|M25.8|M54.9|M72.0|M77.2|M77.3|M79.6'

proc = Processor()

proc.diagnosisCodesToIndices(codeString)

proc.originalFileToProcessedFiles()