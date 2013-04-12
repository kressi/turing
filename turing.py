from turing_machine import TuringMachine
import ast
import argparse


# ********************************
# prepare config 
# ********************************
parser = argparse.ArgumentParser(description='Execute a turing machine.')
parser.add_argument('config',
                    help='name of turing configuration')
parser.add_argument('-s', '--step',
                    action='store_true',
                    help='step through with enter')
parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='print every step')
parser.add_argument('-t', '--tapes',
                    help='content of tapes seperated by comma (e.g. 00000,10000)')
    
args = parser.parse_args()
step = args.step
verbose = args.verbose

with open(args.config + ".conf", 'r') as config_f:
    config = ast.literal_eval(config_f.read())

if args.tapes:
    config['tapesInput'] = args.tapes.split(',')
else:
    config['tapesInput'] = str(raw_input("content of tapes? ")).split(" ")


# ********************************
# run turing machine
# ********************************
t = TuringMachine(**config)
print t

while t.step():
    # next step with enter
    if step:
        raw_input()
    if verbose:
        print t

char = '0'
print "{0} occurs {1} times".format(char, t.getCount(char))
print "Steps: {0}".format(t.getStepCount())

