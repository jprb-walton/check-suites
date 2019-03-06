# 

import sys


def main():

  # Dictionary of suites and titles, generated by gettitle.py
  suiteTitles = {
  "u-bf353" : "HadGEM3-GC3.1 N216ORCA025 HIST #3 for CMIP6 : With redistributed ozone - all stash - 1950+" ,
  "u-bf354" : "HadGEM3-GC3.1 N216ORCA025 HIST #4 for CMIP6 : With redistributed ozone - all stash - 1950+" ,
  "u-bf699" : "HadGEM3-GA7.1 N216 AMIP CMIP6 Master Suite" ,
  "u-bf741" : "HadGEM3-GA7.1 N96 AMIP CMIP6 spinup # 1 : with ozone redistribution" ,
  "u-bf742" : "HadGEM3-GA7.1 N96 AMIP CMIP6 spinup # 2 : with ozone redistribution" ,
  "u-bf743" : "HadGEM3-GA7.1 N96 AMIP CMIP6 spinup # 3 : with ozone redistribution" ,
  "u-bf744" : "HadGEM3-GA7.1 N96 AMIP CMIP6 spinup # 4 : with ozone redistribution" ,
  "u-bg103" : "HadGEM3-GC3.1 N216ORCA025 abrupt-4xCO2 for CMIP6" ,
  "u-bg466" : "HadGEM3-GC3.1 N96ORCA1 HIST run CMIP6 member #1 : 1875+" ,
  "u-bg468" : "HadGEM3-GC3.1 N96ORCA1 HIST run CMIP6 member #3 : 1875+" ,
  "u-bg467" : "HadGEM3-GC3.1 N96ORCA1 HIST run CMIP6 member #2 : 1875+" ,
  "u-bg469" : "HadGEM3-GC3.1 N96ORCA1 HIST run CMIP6 member #4 : 1875+" ,
  "u-bg470" : "HadGEM3-GC3.1 N96ORCA1 HIST run CMIP6 member #5 : 1875+" ,
  "u-bg567" : "CMIP6 DECK HadGEM3-GC3.1 N96ORCA1 1pctCO2 #1" ,
  "u-bg568" : "CMIP6 DECK HadGEM3-GC3.1 N96ORCA1 1pctCO2 #2" ,
  "u-bg569" : "CMIP6 DECK HadGEM3-GC3.1 N96ORCA1 1pctCO2 #3" ,
  "u-bg570" : "CMIP6 DECK HadGEM3-GC3.1 N96ORCA1 1pctCO2 #4" ,
  "u-bg572" : "HadGEM3-GC3.1 N216ORCA025 HIST MASTER for CMIP6 : With redistributed ozone - all stash except COSP" ,
  "u-bg573" : "AerChemMIP UKESM1-AMIP piClim-anthro" ,
  "u-bg574" : "HadGEM3-GC3.1 N216ORCA025 HIST MASTER for CMIP6 : With redistributed ozone - all stash except COSP" ,
  "u-bg586" : "HadGEM3-GA7.1 N216 AMIP CMIP6 spinup # 1 : with ozone redistribution" ,
  "u-bg587" : "HadGEM3-GA7.1 N216 AMIP CMIP6 spinup # 2 : with ozone redistribution" ,
  "u-bg588" : "HadGEM3-GA7.1 N216 AMIP CMIP6 spinup # 3 : with ozone redistribution" ,
  "u-bg589" : "HadGEM3-GA7.1 N216 AMIP CMIP6 spinup # 4 : with ozone redistribution" ,
  "u-bg617" : "CMIP6 DECK HadGEM3-GC3.1 N216ORCA025 abrupt-4xCO2" ,
  }


  for line in sys.stdin:
    # Emsure that the line contains the details about a job (starts with xxxxxx.xcs00).
    if ".xcs" not in line:
      continue
    
    # Extract the number of nodes and jobname (of the form foo.bar.suite).
    items = line.split()
    nodes = int(items[5])
    jobName = items[3]
    
    # Extract the suite from the jobname, then get its title.
    suite = jobName.split('.')[2]
    
    if suite in suiteTitles:    
      title = suiteTitles[suite]
    else:
      title = ""
      print "No title for ", suite

    # Output results for this suite.
    print("{0:3d}  {1:>35s}  {2:<50s}").format(nodes, jobName, title)



if __name__ == '__main__':
  main()
