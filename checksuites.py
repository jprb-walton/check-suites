# 

import sys
import json

from os import access, R_OK
from os.path import isfile

def main():

  # Read dictionary of suites and parameters from file.
  fileName = "suiteParams.txt"
  print fileName, isfile(fileName), access(fileName, R_OK)
  assert isfile(fileName) and access(fileName, R_OK), \
         "File {0} doesn't exist or isn't readable".format(fileName)

  suiteParams = json.load(open(fileName, "r"))


  nodesTotal = 0
  print "User     Nodes             Task                Queued? Owner            Suite title"
  for line in sys.stdin:
    # Emsure that the line contains the details about a job (starts with xxxxxx.xcs00).
    if ".xcs" not in line:
      continue
    
    # Extract the number of nodes and jobname (of the form foo.bar.suite).
    items = line.split()
    nodes = int(items[5])
    jobName = items[3]

    # Extract the jobname (of the form foo.bar.suite).
    jobName = items[3]
    
    # Extract the username.
    user = items[1]

    # Extract the queueing indicator.
    queueLabel = items[9]

    # Extract the suite from the jobname, then get its parameters.
    suite = jobName.split('.')[2]
    if suite in suiteParams:
      title = suiteParams[suite][1]
      owner = suiteParams[suite][0]
    else:
      title = ""
      owner = ""
      print "No parameters for ", suite

    # Output results for this suite.
    print("{0:<8s} {1:3d}  {2:>35s} {3:<2s}   {4:<15s} {5:<50s}").format(user,
      nodes, jobName, queueLabel, owner, title)
    nodesTotal += nodes

  print("Total number of nodes {}\n").format(nodesTotal)


if __name__ == '__main__':
  main()
