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
      print('ping from ' + i + ' to ' + ii + ': ', end ='  ')
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
      else:
        print('Not available.')

def printiperf():
  p = re.compile("(Stream.).*SUM.* (.* .bits/sec).*sender$")

  for i in INST:
    for ii in INST:
      inp_lst = []
      print('iperf3 from ' + i + ' to ' + ii + ': ')
      filepath = PATH + i + '/iperf3_to_' + ii + '.txt'
      try:
        iperf = open(filepath, 'r')
      except:
        iperf = None
      if iperf:
        iperfraw = iperf.readlines()
        for line in iperfraw:
          iperfstrm = p.search(line)
          if iperfstrm:
            print('  '+ iperfstrm.group(1) + ': ' +iperfstrm.group(2))
      else:
        print('Not available.')

def main():
  printping()
  printiperf()

if __name__ == '__main__':
  main()
