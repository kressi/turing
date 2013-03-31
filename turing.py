from turing_machine import TuringMachine
import sys
import ast
import os


# ********************************
# prepare config 
# ********************************
config = {}

#default values
config["tapeCount"] = 2
config["transitions"] = {'0-00':'0-00RN', '0-#0':'0-00RR'}
config["tapesInput"] = ["00000", "000000"]


def writeConfig(handle):
    # write config file from stdin
    config = {}
    config["tapeCount"] = int(input("number of tapes? "))
    #config["initState"] = 1
    config["transitions"] = {}
    if raw_input("from file? Y n ") == "n":
        trans_string = raw_input("transitions? ")
    else:
        with open(raw_input("filename? "),'r') as trans_f:
            trans_string = trans_f.read()
    for trans in trans_string.split(","):
        parts = trans.split(":")
        config["transitions"][parts[0]] = parts[1]
    if config:
        handle.write(str(config))

if len(sys.argv) > 1:
    if sys.argv[1] + ".conf" in os.listdir(os.getcwd()):
        # read config file
        with open(sys.argv[1] + ".conf", 'r') as config_f:
            config = ast.literal_eval(config_f.read())
    else:
        with open(sys.argv[1] + ".conf", 'w') as config_f:
            writeConfig(config_f)
    if len(sys.argv) > 2:
        # read tapes input from argument values
        config["tapesInput"] = []
        for i in range(2,len(sys.argv)):
            config["tapesInput"].append(sys.argv[i])
    else:
        # read tapes input from stdin
        config["tapesInput"] = str(raw_input("content of tapes? ")).split(" ")



# ********************************
# run turing machine
# ********************************
t = TuringMachine(**config)
t.show()
# t.step(True) to list transition key and value of transitions
while t.step():
    # next step with enter
    #raw_input()
    t.show()

