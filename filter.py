import os
import sys
import subprocess

# global paths --> will need to make general
os.chdir(os.path.expanduser('~'))
user= os.getcwd()
home = os.path.join(user, 'synthesis')
logs = os.path.join(home, 'logs')
reducedLog = os.path.join(home, 'reducedLogs')

# take in warning list file & file to modify
args = sys.argv

def obtain_list(list_file):
    remove_file = open(list_file, 'r')
    remove_list = remove_file.readlines()
    remove_file.close()

    warning_list = []
    for item in remove_list:
        item = item[:-1]
        warning_list.append(item)
    return warning_list


def filter(warning_list, input_file, output_file):
    # obtain file contents to parse
    log_lines = open(input_file, 'r')
    file_to_filter = log_lines.readlines()
    log_lines.close()
    
    # create reduced file
    reduced_file = open(output_file, 'w')

    # look for keywords in every line
    i = 0 # line counter
    while i < len(file_to_filter):
        match = 0
        for keyword in warning_list:
            if keyword in file_to_filter[i]: 
                # remove file
                print(f'Keyword: {keyword} \t MATCH')
                match += 1
                break
        if match < 1:
            reduced_file.write(file_to_filter[i])
        i = i + 1



if __name__ == "__main__":
    os.chdir(home)
    list_file = args[1] # path to warning_list file
    input_file = args[2] # path to input file
    output_file = args[3] # path to destination of output
    warning_list = obtain_list(list_file)
    filter(warning_list, input_file, output_file)
