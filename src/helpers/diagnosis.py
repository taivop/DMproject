# Terminology used:
# Diagnosis ID: 5
# Diagnosis code: "Z01"
# Diagnosis label: "Bad case of Freemanic Paracusia"

class Diagnosis():

    numberOfDiagnoses = 0
    idsToCodes = dict()
    codesToIds = dict()
    codesToLabels = dict()


    def __init__(self):
        import json

        # Read mappings from file
        filename = '..\maps\codesToLabels.dict'
        f = open(filename)
        line = f.readline()
        f.close()
        self.codesToLabels = json.loads(line)

        # Read mappings from file
        filename = '..\maps\idsToCodes.dict'
        f = open(filename)
        line = f.readline()
        f.close()
        self.idsToCodes = json.loads(line)

        # Read mappings from file
        filename = '..\maps\codesToIds.dict'
        f = open(filename)
        line = f.readline()
        f.close()
        self.codesToIds = json.loads(line)

        # Save the number of different diagnoses we have for later use
        self.numberOfDiagnoses = len(self.codesToLabels)


    def getCodeFromId(self, id):
        # Get diagnosis code from diagnosis id.
        return self.idsToCodes[id]

    def getIdFromCode(self, code):
        # Get diagnosis id from diagnosis code.
        return int(self.codesToIds[code])

    def getLabelFromCode(self, code):
        # Get diagnosis label from diagnosis code.
        return self.codesToLabels[code]

    def getLabelFromId(self, id):
        # Get diagnosis label from diagnosis id.
        return self.codesToLabels[self.idsToCodes[id]]


    def preprocessDiagnoses(self):
        # Turns the original diagnoses file into three pretty dictionaries and saves them.
        # This method should not be called after the files have been created initially.
        import json

        # read file
        filename = '../data/rhk.txt'
        f = open(filename, encoding='utf-8')
        lines = f.readlines()
        f.close()

        diagnoses = self.codesToLabels

        # go through every diagnosis
        for line in lines:
            stringlist = line.strip().replace(u'\ufeff', '').split()

            # if it is a general diagnosis (code doesn't contain a '.'), add it to dictionary
            if stringlist[0].find('.') == -1 and stringlist[0].find('-') == -1:
                # add to dictionary
                diagnoses[stringlist[0]] = ' '.join(stringlist[1:])

        # save the dictionary into a file
        filename = '..\maps\codesToLabels.dict'
        f = open(filename,'w')
        #print(json.dumps(diagnoses))
        f.write(json.dumps(diagnoses))     # json format
        f.close()

        # Create a mapping of id -> code and code -> id
        numKeys = len(diagnoses)    # count how many possible diagnoses do we have?
        i = 0
        for key in sorted(diagnoses.keys()):
            self.idsToCodes[str(i)] = key
            self.codesToIds[key] = str(i)
            i += 1

        # Write the two mappings into files
        filename = '..\maps\idsToCodes.dict'
        f = open(filename,'w')
        f.write(json.dumps(self.idsToCodes))     # json format
        f.close()

        filename = '..\maps\codesToIds.dict'
        f = open(filename,'w')
        f.write(json.dumps(self.codesToIds))     # json format
        f.close()
        return

    def diagnosisCodeIsBasic(self, diagnosisCode):
        # Returns true iff the diagnosis code is basic, i.e. contains no dots (.) or dashes (-).
        if(diagnosisCode.find('.') == -1 and diagnosisCode.find(',') == -1 and diagnosisCode.find('-') == -1):
            return True
        else:
            return False

    def diagnosisCodeToBasic(self, diagnosisCode):
        # Returns the basic part of a diagnosis, i.e. for input 'A03.5' it returns 'A03'.
        if(self.diagnosisCodeIsBasic(diagnosisCode)):
            return diagnosisCode
        elif(diagnosisCode.find('-') != -1):
            raise Exception('Diagnosis code contains a dash ("-").')
        else:
            base = diagnosisCode
            dot = diagnosisCode.find('.')
            comma = diagnosisCode.find(',')
            if dot != -1:
                base = base[:dot]
            if comma != -1:
                base = base[:comma]
            return base