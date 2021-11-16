# ReduceSynthesisLogs

This repository contains the necessary set up environment and script to be able to parse a synthesis output log file and remove a set of warnings that are deemed "okay." Currently, there is an example of the warning list and log that is valid for running. 

# Provided Environment consists of: 
  1. Python script
  2. "Warning_list" which contains the lines that are deemed "okay" to remove from the log


# Python Arguments
  filter.py takes in 3 arguments: the warning_list text file, the path to the file to be parsed, and the path to the destination output file
  EXAMPLE: ~/synthesis$: python3 filter.py warning_list logs/check_design.rpt reducedLogs/check_designR.rpt
  
  

