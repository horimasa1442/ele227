import json
import sys
import copy
import os
from HelperFunc import *

if __name__ == "__main__":
    file = open(sys.argv[1])
    inputdic = json.load(file)

    print("translate 11 parameters to 27 parameters")
    orderOfParameters = [9, 1, 2, 3, 4, 5, 6, 7, 8, \
                            10, 1, 2, 3, 4, 5, 6, 7, 8, \
                            0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(len(inputdic)):
        illus = str2floatList(inputdic[i]["illumination"], " ")
        outputParam = ""
        for j in range(len(orderOfParameters) - 1):
            outputParam += str(illus[orderOfParameters[j]]) + " "

        outputParam += str(illus[orderOfParameters[len(orderOfParameters) - 1]])
        inputdic[i]["illumination"] = outputParam

    outputPath = os.path.join(os.path.dirname(sys.argv[1]), "out27.txt")
    outputFile = open(outputPath, "w")
    json.dump(inputdic, outputFile)