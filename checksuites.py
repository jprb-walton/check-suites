# 

import sys

def main():

  title = {
  "u-bg555" : "N96 abrupt4CO2", 

  "u-bg567" : "N96 1pctCO2 #1",
  "u-bg568" : "N96 1pctCO2 #2",
  "u-bg569" : "N96 1pctCO2 #3",
  "u-bg570" : "N96 1pctCO2 #4",

  "u-bg467" : "N96 Hist #2 1875+",

  "u-bf741" : "N96 AMIP spinup #1: with ozone redistribution",
  "u-bf742" : "N96 AMIP spinup #2: with ozone redistribution",
  "u-bf743" : "N96 AMIP spinup #3: with ozone redistribution",
  "u-bf744" : "N96 AMIP spinup #4: with ozone redistribution",

  "u-bg466" : "N96 Hist #1 1875+",
  "u-bg468" : "N96 Hist #3 1875+",
  "u-bg469" : "N96 Hist #4 1875+",

  "u-bf699" : "N216 AMIP Master suite",

  "u-bg586" : "N216 AMIP spinup #1: with ozone redistribution",
  "u-bg587" : "N216 AMIP spinup #2: with ozone redistribution",
  "u-bg588" : "N216 AMIP spinup #3: with ozone redistribution",
  "u-bg589" : "N216 AMIP spinup #4: with ozone redistribution",

  "u-bf353" : "N216 Hist #3 1950+",
  "u-bf354" : "N216 Hist #4 1950+",

  "u-bg617" : "N216 abrupt4CO2"
  }


  for line in sys.stdin:
    if ".xcs" not in line:
      continue
    items = line.split()
    jobname = items[3]
    nodes = items[5]
    suite = jobname.split('.')[2]
    
    if suite in title:    
      print("{0:3d}  {1:>35s}  {2:<50s}").format(int(nodes), jobname, title[suite])
    else:
      print "No title for ", suite


if __name__ == '__main__':
  main()
