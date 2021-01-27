Scroll down to see notes-

```
$ ./simple_test.py
Enter test description: "Test run on local LAN at USC."
Test(s) to run ("iperf3"/"bbcp"/"all"): all
----------------------------------------
Running script at Wed Jan 27 13:41:43 2021
Testing: "Test run on local LAN at USC."
----------------------------------------
*** All tests selected. ***
Running bbcp copying /mnt/chris_xfer/100G.dat to hpc-transfer1.usc.edu:/project/hpcroot/christay/chris_xfer
----------------------------------------
Command line: bbcp -v -f -P 8 -r -s 4 -F /mnt/chris_xfer/100G.dat hpc-transfer1.usc.edu:/project/hpcroot/christay/chris_xfer
bbcp: Indexing files to be copied...
bbcp: Copying 0 files and 0 links in 0 directories.
bbcp: Creating /project/hpcroot/christay/chris_xfer/100G.dat
bbcp: 210127 13:41:56  8% done; 1006.2 MB/s, avg 1006.2 MB/s
bbcp: 210127 13:42:03  15% done; 1013.6 MB/s, avg 1009.7 MB/s
bbcp: 210127 13:42:10  23% done; 1.0 GB/s, avg 1018.1 MB/s
```
   *** edited for brevity ***
```
bbcp: 210127 13:43:00  78% done; 1.0 GB/s, avg 1.0 GB/s
bbcp: 210127 13:43:07  86% done; 1.0 GB/s, avg 1.0 GB/s
bbcp: 210127 13:43:14  94% done; 1.0 GB/s, avg 1.0 GB/s
File /project/hpcroot/christay/chris_xfer/100G.dat created; 100000000000 bytes at 1.0 GB/s
1 file copied at effectively 978.0 MB/s
----------------------------------------
Running bbcp copying /mnt/chris_xfer/nsf21-528-100g to hpc-transfer1.usc.edu:/project/hpcroot/christay/chris_xfer
----------------------------------------
Command line: bbcp -v -f -P 8 -r -s 4 -F /mnt/chris_xfer/nsf21-528-100g hpc-transfer1.usc.edu:/project/hpcroot/christay/chris_xfer
bbcp: Indexing files to be copied...
bbcp: Copying 100 files and 0 links in 1 directory.
bbcp: Creating /project/hpcroot/christay/chris_xfer/nsf21-528-100g/1G1.dat
File /project/hpcroot/christay/chris_xfer/nsf21-528-100g/1G1.dat created; 1000000000 bytes at 1.2 GB/s
bbcp: Creating /project/hpcroot/christay/chris_xfer/nsf21-528-100g/1G2.dat
File /project/hpcroot/christay/chris_xfer/nsf21-528-100g/1G2.dat created; 1000000000 bytes at 1.0 GB/s
```
    *** edited for brevity ***
```
bbcp: Creating /project/hpcroot/christay/chris_xfer/nsf21-528-100g/1G99.dat
File /project/hpcroot/christay/chris_xfer/nsf21-528-100g/1G99.dat created; 1000000000 bytes at 1.3 GB/s
bbcp: Creating /project/hpcroot/christay/chris_xfer/nsf21-528-100g/1G100.dat
File /project/hpcroot/christay/chris_xfer/nsf21-528-100g/1G100.dat created; 1000000000 bytes at 1.2 GB/s
100 files copied at effectively 1.1 GB/s
----------------------------------------
----------------------------------------
Running iperf3 from localhost to hpc-transfer1.usc.edu
----------------------------------------
Command line: iperf3 -i 10 -t 20 -Z -P 2 -c hpc-transfer1.usc.edu -T Stream1 -p 5101
----------------------------------------
Command line: iperf3 -i 10 -t 20 -Z -P 2 -c hpc-transfer1.usc.edu -T Stream2 -p 5102
----------------------------------------

Stream2:  Connecting to host hpc-transfer1.usc.edu, port 5102
Stream1:  Connecting to host hpc-transfer1.usc.edu, port 5101
[christay@hpc-mdtn2 Work]$ Stream2:  [  4] local 68.181.11.10 port 44186 connected to 68.181.11.5 port 5102
Stream1:  [  4] local 68.181.11.10 port 50122 connected to 68.181.11.5 port 5101
Stream1:  [  6] local 68.181.11.10 port 50124 connected to 68.181.11.5 port 5101
Stream2:  [  6] local 68.181.11.10 port 44192 connected to 68.181.11.5 port 5102
Stream1:  [ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
Stream2:  [ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
Stream1:  [  4]   0.00-10.00  sec  12.7 GBytes  10.9 Gbits/sec   69   4.94 MBytes
Stream2:  [  4]   0.00-10.00  sec  12.3 GBytes  10.5 Gbits/sec   52   1.56 MBytes
Stream1:  [  6]   0.00-10.00  sec  12.7 GBytes  10.9 Gbits/sec  119   4.20 MBytes
Stream2:  [  6]   0.00-10.00  sec  12.3 GBytes  10.5 Gbits/sec  137   1.53 MBytes
Stream1:  [SUM]   0.00-10.00  sec  25.4 GBytes  21.8 Gbits/sec  188
Stream2:  [SUM]   0.00-10.00  sec  24.5 GBytes  21.1 Gbits/sec  189
Stream1:  - - - - - - - - - - - - - - - - - - - - - - - - -
Stream1:  [  4]  10.00-20.00  sec  12.7 GBytes  10.9 Gbits/sec   64   5.29 MBytes
Stream1:  [  6]  10.00-20.00  sec  12.7 GBytes  10.9 Gbits/sec  170   4.26 MBytes
Stream1:  [SUM]  10.00-20.00  sec  25.3 GBytes  21.7 Gbits/sec  234
Stream1:  - - - - - - - - - - - - - - - - - - - - - - - - -
Stream1:  [ ID] Interval           Transfer     Bandwidth       Retr
Stream1:  [  4]   0.00-20.00  sec  25.3 GBytes  10.9 Gbits/sec  133             sender
Stream1:  [  4]   0.00-20.00  sec  25.3 GBytes  10.9 Gbits/sec                  receiver
Stream1:  [  6]   0.00-20.00  sec  25.4 GBytes  10.9 Gbits/sec  289             sender
Stream1:  [  6]   0.00-20.00  sec  25.3 GBytes  10.9 Gbits/sec                  receiver
```
   This next line is important-
```
Stream1:  [SUM]   0.00-20.00  sec  50.7 GBytes  21.8 Gbits/sec  422             sender
Stream1:  [SUM]   0.00-20.00  sec  50.7 GBytes  21.8 Gbits/sec                  receiver
Stream1:
Stream1:  iperf Done.
Stream2:  - - - - - - - - - - - - - - - - - - - - - - - - -
Stream2:  [  4]  10.00-20.00  sec  12.3 GBytes  10.5 Gbits/sec   63   1.60 MBytes
Stream2:  [  6]  10.00-20.00  sec  12.3 GBytes  10.5 Gbits/sec  124   1.63 MBytes
Stream2:  [SUM]  10.00-20.00  sec  24.6 GBytes  21.1 Gbits/sec  187
Stream2:  - - - - - - - - - - - - - - - - - - - - - - - - -
Stream2:  [ ID] Interval           Transfer     Bandwidth       Retr
Stream2:  [  4]   0.00-20.00  sec  24.6 GBytes  10.5 Gbits/sec  115             sender
Stream2:  [  4]   0.00-20.00  sec  24.5 GBytes  10.5 Gbits/sec                  receiver
Stream2:  [  6]   0.00-20.00  sec  24.5 GBytes  10.5 Gbits/sec  261             sender
Stream2:  [  6]   0.00-20.00  sec  24.5 GBytes  10.5 Gbits/sec                  receiver
```
   And this one-
```
Stream2:  [SUM]   0.00-20.00  sec  49.1 GBytes  21.1 Gbits/sec  376             sender
Stream2:  [SUM]   0.00-20.00  sec  49.1 GBytes  21.1 Gbits/sec                  receiver
Stream2:
Stream2:  iperf Done.
```

Add the results from these two streams together:
```
Stream1:  [SUM]   0.00-20.00  sec  50.7 GBytes  21.8 Gbits/sec  422             sender
Stream2:  [SUM]   0.00-20.00  sec  49.1 GBytes  21.1 Gbits/sec  376             sender
```
So, I got 21.8 + 21.1 GBits/sec for 42.9 GBits/sec. Also take note of the retries (Retr) in the 2nd to last column. I get those when I'm saturating some part of the flow (but sometimes it's kind of hard to tell what part- it could be one of the many network hops, TCP or OS buffers on one of the endpoints... that's all part of the fun).


