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
        ping.close()
      else:
        print('Not available.')

def printiperf():
  p = re.compile("(Stream.).*SUM.* (.* .bits/sec).*sender$")

  for i in INST:
    for ii in INST:
      print('iperf3 from ' + i + ' to ' + ii + ': ', end = ' ')
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
            print('  ' + iperfstrm.group(1) + ': ' +iperfstrm.group(2) + '  ', end = '')
        print('')
        iperf.close()
      else:
        print('Not available.')

def printbbcp():
  p = re.compile("^.*copied at effectively.*$")
  r = re.compile("effectively ")

  for i in INST:
    for ii in INST:
      print('bbcp from ' + i + ' to ' + ii + ': ', end =' ')
      filepath = PATH + i + '/bbcp_to_' + ii + '.txt'
      try:
        bbcp = open(filepath, 'r')
      except:
        bbcp = None
      if bbcp:
        bbcpraw = bbcp.readlines()
        for line in bbcpraw:
          bbcpline = p.search(line)
          if bbcpline:
            bbcplinex = r.sub('', bbcpline.group())
            print('  ' + bbcplinex + '  ', end ='')
        print('')
        bbcp.close()
      else:
        print('Not available.')

def printtrace():
  p = re.compile("\*\s*\*\s*\*|HANGS|!X")
  r = re.compile("^\s*([0-9]*)")

  for i in INST:
    for ii in INST:
      print('traceroute from ' + i + ' to ' + ii + ': ', end ='  ')
      filepath = PATH + i + '/traceroute_to_' + ii + '.txt'
      try:
        trace = open(filepath, 'r')
      except:
        trace = None
      if trace:
        traceraw = trace.readlines()
        lastline = traceraw[-1:]
        blockline = p.search(lastline[0])
        if blockline:
          print('Blocked or unreachable.' + ' (' + blockline.group() + ')')
        else:
          rl = r.search(lastline[0])
          if rl:
            print('  Hops: ' + rl.group(1))
            #print(lastline[0])
        trace.close()
      else:
        print('Not available.')

def main():
  printping()
  printtrace()
  printiperf()
  printbbcp()

if __name__ == '__main__':
  main()
