#!/usr/bin/python3 -u
import subprocess
import re
import tempfile
import datetime

DEST = 'hpc-transfer1.usc.edu' # Target node for transfers

def iperf3(DEST):
  print('-' * 40)
  print('Running iperf3 from localhost to ' + DEST)
  for stream in ['5101', '5102']:
    processI = ['iperf3', '-i', '10', '-t', '20', '-Z', '-P', '2']
    processI.extend(['-c', DEST, '-T', ('Stream' + str(int(stream) - 5100)), '-p', stream])
    subprocess.Popen(processI)
    print('-' * 40)
    print('Command line: ', end='')
    for n in processI:
      print(n + ' ', end='')
    print('')
  print('-' * 40)
  print(' ')

def bbcp(DEST):
  # Modify these lines for the files to be transferred from client,
  # and the destination directory on the target node.
  for xferfile in ['/mnt/chris_xfer/100G.dat', '/mnt/chris_xfer/nsf21-528-100g']:
    DESTfile = DEST + ':/project/hpcroot/christay/chris_xfer'
    print('Running bbcp copying ' + xferfile + ' to ' + DESTfile)
    processB = ['bbcp', '-v', '-f', '-P', '8', '-r', '-s', '4', '-F']
    processB.extend([xferfile, DESTfile])
    print('-' * 40)
    print('Command line: ', end='')
    for n in processB:
      print(n + ' ', end='')
    print('')
    bb50gcopy = subprocess.Popen(processB)
    bb50gcopy.wait()
    print('-' * 40)

def main():
  SITE = input('Enter test description: ')

  while True:
    TESTS = input('Test(s) to run ("iperf3"/"bbcp"/"all"): ')
    if TESTS.lower() not in ('iperf3', 'bbcp',  'all'):
        print("Please answer either \"iperf3\", \"bbcp\" or \"all\".")
    else:
        break

  print('-' * 40)
  T = (datetime.datetime.now()).strftime("%c")
  print('Running script at ' + T + '\nTesting: '+ SITE)
  print('-' * 40)

  if TESTS =='iperf3':
    print('*** iperf3 test selected. ***')
    iperf3(DEST)
  elif TESTS =='bbcp':
    print('*** bbcp test selected. ***')
    bbcp(DEST)
  else:
    print('*** All tests selected. ***')
    bbcp(DEST)
    # Have to run this last
    iperf3(DEST)

if __name__ == '__main__':
  main()
