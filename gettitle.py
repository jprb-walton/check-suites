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


def gettitle(suitename):

  # Get the title of the suite.  suitename is the name of the suite in the form u-aa999.
  
  # This is the orignal form of the command; this doesn't work when spawned - possibly because 
  # of the quotes in the sed command.
  #
  #svn cat https://code.metoffice.gov.uk/svn/roses-u/b/g/4/6/9/trunk/rose-suite.info | grep title | sed 's/title=//'
   
  # Pull off the id.
  suiteid = suitename.split('-')[1]
  
  # Build up the command.  We use svn to list the rose-suite.info file for the suite, and
  # extract the line containing 'title'.
  command = "svn cat https://code.metoffice.gov.uk/svn/roses-u/"
  for c in suiteid:
    command = command + c + "/"
  command = command + "trunk/rose-suite.info | grep title"
  line = spawn_command(command)
  
  # line is of the form title=foo.  Pull off the first part.
  title = line.replace("title=", "")
  
  # Return the title, with trailing whitespace (including newline characters) removed.
  return title.rstrip()


def main():

  # List the suites to be processed.
  suites = [
  "u-bg469" ,
  "u-bg567" ,
  "u-bg568" ,
  "u-bg569" ,
  "u-bg570" ,
  "u-bg467" ,

  "u-bf741" ,
  "u-bf742" ,
  "u-bf743" ,
  "u-bf744" ,

  "u-bg466" ,
  "u-bg468" ,
  "u-bg469" ,

  "u-bf699" ,

  "u-bg586" ,
  "u-bg587" ,
  "u-bg588" ,
  "u-bg589" ,

  "u-bf353" ,
  "u-bf354" ,

  "u-bg617" 
  ]
  
  # Process each one.  Output is formatted for cutting and pasting into 
  # a dictionary (in e.g. checksuites.py).
  for suite in suites:
    print "  \"" + suite + "\" : \"" + gettitle(suite) + "\" ,"


if __name__ == '__main__':
  main()
