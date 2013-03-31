turing
======

Turing machine in Python.


blank symbol is #
turing machine starts on the leftmost symbol of a tape, blank if tape is empty

turing.py [config [input tapes]]
config: in case config does not exist required values will be requested and written to new conifg file
input tapes: values initially on tapes, if more than 1 tape, seperated by space (e.g. '000001 0000')


examples:
turing.py
starts turing machine with a default config with two tapes

turing.py test
starts turing machine with test configuration with one tape

turing.py test 00001000000
starts turing machine with input

turing.py new-config
file 'new-config.conf' will be created (if it does not exist already) for config required parameters will be requested.
transitions can be read from file or entered manually. format see turing1_trans_string.
