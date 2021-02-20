#!/usr/bin/python3 -u
import subprocess
import numpy
import re
INST = ['Caltech',  'Claremont-HMC',  'KGI',  'LMU',  'Oxy',  'Pomona',  'USC']
PATH = '../../Results-and-Metrics/'

def average(inp_lst):
  return round(numpy.average(inp_lst), 2)

def printping():
  p = re.compile(' time=([0-9]*\.[0-9]*) ms')

  for i in INST:
    for ii in INST:
      inp_lst = []
      print('ping from ' + i + ' to ' + ii + ':')
      filepath = PATH + i + '/ping_to_' + ii + '.txt'
      try:
        ping = open(filepath, 'r')
      except:
        ping = None
      if ping:
        pingraw = ping.readlines()
        for line in pingraw:
          pingtime = p.search(line)
          if pingtime:
            inp_lst.append(float(pingtime.group(1)))
        print(str(average(inp_lst)) + ' ms average')
        print('')
      else:
        print('Not available.')

def main():
  printping()

if __name__ == '__main__':
  main()
