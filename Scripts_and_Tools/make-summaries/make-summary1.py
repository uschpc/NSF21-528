#!/usr/bin/python3 -u
import subprocess
import re
INST = ['Caltech',  'Claremont-HMC',  'KGI',  'LMU',  'Oxy',  'Pomona',  'USC']
PATH = '../../Results-and-Metrics/'

def printping():
  for i in INST:
    for ii in INST:
      filepath = PATH + i + '/ping_to_' + ii + '.txt'
      print(filepath)
      try:
        ping = open(filepath + '/ping_to_' + ii + '.txt', 'r')
      except:
        ping = None
      else:
        print('here')

  if ping:
    print(ping.read())

def main():
  printping()

if __name__ == '__main__':
  main()
