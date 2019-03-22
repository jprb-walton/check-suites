# Find the titles of a set of suites.

import sys
import subprocess


def spawn_command(command):

  # This routine spawns subprocess(es) to execute command.  If command contains pipes
  # then we reproduce the pipeline by creatin several subprocesses and chaining their
  # inputs and outputs together.

  pipeCommands = command.split('|')
  proc = subprocess.Popen(pipeCommands[0].split(), stdout = subprocess.PIPE)
  if len(pipeCommands) > 1:
    for pipe_command in pipeCommands[1:]:
      proc2 = subprocess.Popen(pipe_command.split(), stdin = proc.stdout, stdout = subprocess.PIPE)
      proc = proc2
  return proc.communicate()[0]


def getparam(suitename, parameter):

  # Get the value of a suite parameter.
  # suitename is the name of the suite in the form u-aa999.
  # parameter is an entry in rose-suite.info (e.g. title, owner).
  
  # This is the orignal form of the command; this doesn't work when spawned - possibly
  # because of the quotes in the sed command.
  #
  #svn cat https://code.metoffice.gov.uk/svn/roses-u/b/g/4/6/9/trunk/rose-suite.info | grep title | sed 's/title=//'
   
  # Pull off the id.
  suiteid = suitename.split('-')[1]
  
  # Build up the command.  We use svn to list the rose-suite.info file for the
  # suite, and extract the line containing 'title'.
  command = "svn cat https://code.metoffice.gov.uk/svn/roses-u/"
  for c in suiteid:
    command = command + c + "/"
  command = command + "trunk/rose-suite.info | grep " + parameter
  line = spawn_command(command)
  
  # line is of the form parameter=foo.  Pull off the first part.
  firstpart = parameter + '='
  result = line.replace(firstpart, "")
  
  # Return the title, with trailing whitespace (including newline characters) removed.
  return result.rstrip()


def main():

  # List the suites to be processed.
  suites = [

  # eroberts
  "u-bc930" ,
  "u-bd531" ,
  "u-bd532" ,
  "u-bd533" ,
  "u-bf916" ,
  "u-bf917" ,
  "u-bf980" ,
  "u-bf981" ,


  # hadaw
  "u-bd531" ,
  "u-bf965" ,
  "u-bf967" ,
  "u-bf968" ,

  "u-bf938" ,

  "u-bg203" ,
  "u-bg204" ,
  "u-bg205" ,
  "u-bg206" ,
  "u-bg207" ,
  "u-bg208" ,

  "u-bg512" ,
  

  # hadfo
  "u-bf531" ,
  "u-bf534" ,
  "u-bf535" ,
  "u-bg738" ,


  # hadgf
  "u-bf659" ,
  "u-bg634" ,


  # hadjr
  "u-bf772" ,


  # hadsl
  "u-bc235" ,
  "u-bc253" ,
  "u-be909" ,
  "u-bg017" ,
  "u-bg246" ,
  "u-bg258" ,
  "u-bg510" ,

  # rsmith
  "u-bc590" ,
  "u-bd727" ,
  "u-bd729" ,
  "u-be760" ,
  "u-bf918" ,
  "u-bg539" ,


  # ukcmip6
  "u-be372" ,
  "u-be488" ,

  "u-bf351" ,
  "u-bf352" ,
  "u-bf353" ,
  "u-bf354" ,
  
  "u-bf699" ,

  "u-bf741" ,
  "u-bf742" ,
  "u-bf743" ,
  "u-bf744" ,

  "u-bg101" ,
  "u-bg103" ,
  
  "u-bg466" ,
  "u-bg468" ,
  "u-bg467" ,
  "u-bg469" ,
  "u-bg470" ,

  "u-bg555" ,
  
  "u-bg567" ,
  "u-bg568" ,
  "u-bg569" ,
  "u-bg570" ,

  "u-bg572" ,
  "u-bg573" ,
  "u-bg574" ,


  "u-bg586" ,
  "u-bg587" ,
  "u-bg588" ,
  "u-bg589" ,

  "u-bg617" , 
  "u-bg618" , 

  "u-bg881" ,
  "u-bg882" ,
  "u-bg883" ,
  "u-bg884" ,

  "u-bh010" ,
  "u-bh109" ,
  "u-bh114" ,


  # ukesm
  "u-aq281" ,
  "u-bf467" ,
  "u-bf590" ,
  "u-bf785" ,
  "u-bf786" ,


  ]
  
  # Process each one.  Output is formatted for cutting and pasting into 
  # a dictionary (in e.g. checksuites.py).
  for suite in suites:
    print "  \"" + suite + "\" : [\"" + getparam(suite, "owner") + "\" , \"" + getparam(suite, "title") + "\"] ,"

if __name__ == '__main__':
  main()
