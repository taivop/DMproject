import json


def preprocessDiagnoses():

    # read file
    filename = '../data/rhk.txt'
    f = open(filename, encoding='utf-8')
    lines = f.readlines()
    f.close()

    # initialise dictionary
    diagnoses = dict()

    # go through every diagnosis
    for line in lines:
        stringlist = line.strip().replace(u'\ufeff', '').split()

        # if it is a general diagnosis (code doesn't contain a '.' or '-'), add it to dictionary
        if stringlist[0].find('.') == -1 and stringlist[0].find('-') == -1:
            # add to dictionary
            diagnoses[stringlist[0]] = ' '.join(stringlist[1:])

    # save the dictionary into a file
    filename = '..\data\codeToLabel.dict'
    f = open(filename,'w')
    print(json.dumps(diagnoses))
    f.write(json.dumps(diagnoses))     # json format
    f.close()

    return


def getDiagnosesDictionary():
    # read dict from file
    filename = '..\data\diagnoses.dict'
    f = open(filename)
    line = f.readline()
    f.close()

    # turn string into python dict
    diagnoses = json.loads(line.strip())

    return diagnoses

preprocessDiagnoses()