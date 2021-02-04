####

```
$ iperf3 -i 10 -t 20 -Z -P 2 -c hpc-mdtn2.usc.edu -T Stream1 -p 5101
Stream1:  Connecting to host hpc-mdtn2.usc.edu, port 5101
Stream1:  [  5] local 134.173.65.144 port 34116 connected to 68.181.11.10 port 5101
Stream1:  [  7] local 134.173.65.144 port 34118 connected to 68.181.11.10 port 5101
Stream1:  [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
Stream1:  [  5]   0.00-10.00  sec   831 MBytes   697 Mbits/sec  323    441 KBytes       
Stream1:  [  7]   0.00-10.00  sec   596 MBytes   500 Mbits/sec  923    251 KBytes       
Stream1:  [SUM]   0.00-10.00  sec  1.39 GBytes  1.20 Gbits/sec  1246             
Stream1:  - - - - - - - - - - - - - - - - - - - - - - - - -
Stream1:  [  5]  10.00-20.00  sec   840 MBytes   704 Mbits/sec  453    265 KBytes       
Stream1:  [  7]  10.00-20.00  sec   600 MBytes   503 Mbits/sec  244    394 KBytes       
Stream1:  [SUM]  10.00-20.00  sec  1.41 GBytes  1.21 Gbits/sec  697             
Stream1:  - - - - - - - - - - - - - - - - - - - - - - - - -
Stream1:  [ ID] Interval           Transfer     Bitrate         Retr
Stream1:  [  5]   0.00-20.00  sec  1.63 GBytes   701 Mbits/sec  776             sender
Stream1:  [  5]   0.00-20.00  sec  1.63 GBytes   700 Mbits/sec                  receiver
Stream1:  [  7]   0.00-20.00  sec  1.17 GBytes   502 Mbits/sec  1167             sender
Stream1:  [  7]   0.00-20.00  sec  1.17 GBytes   501 Mbits/sec                  receiver
Stream1:  [SUM]   0.00-20.00  sec  2.80 GBytes  1.20 Gbits/sec  1943             sender
Stream1:  [SUM]   0.00-20.00  sec  2.80 GBytes  1.20 Gbits/sec                  receiver
Stream1:  
Stream1:  iperf Done.


$ iperf3 -i 10 -t 20 -Z -P 2 -c hpc-mdtn2.usc.edu -T Stream2 -p 5102
Stream2:  Connecting to host hpc-mdtn2.usc.edu, port 5102
Stream2:  [  5] local 134.173.65.144 port 52948 connected to 68.181.11.10 port 5102
Stream2:  [  7] local 134.173.65.144 port 52950 connected to 68.181.11.10 port 5102
Stream2:  [ ID] Interval           Transfer     Bitrate         Retr  Cwnd
Stream2:  [  5]   0.00-10.00  sec  1015 MBytes   851 Mbits/sec  567    309 KBytes       
Stream2:  [  7]   0.00-10.00  sec   503 MBytes   422 Mbits/sec  311    317 KBytes       
Stream2:  [SUM]   0.00-10.00  sec  1.48 GBytes  1.27 Gbits/sec  878             
Stream2:  - - - - - - - - - - - - - - - - - - - - - - - - -
Stream2:  [  5]  10.00-20.00  sec  1.03 GBytes   888 Mbits/sec  236    398 KBytes       
Stream2:  [  7]  10.00-20.00  sec   539 MBytes   452 Mbits/sec  300    313 KBytes       
Stream2:  [SUM]  10.00-20.00  sec  1.56 GBytes  1.34 Gbits/sec  536             
Stream2:  - - - - - - - - - - - - - - - - - - - - - - - - -
Stream2:  [ ID] Interval           Transfer     Bitrate         Retr
Stream2:  [  5]   0.00-20.00  sec  2.02 GBytes   870 Mbits/sec  803             sender
Stream2:  [  5]   0.00-20.00  sec  2.02 GBytes   869 Mbits/sec                  receiver
Stream2:  [  7]   0.00-20.00  sec  1.02 GBytes   437 Mbits/sec  611             sender
Stream2:  [  7]   0.00-20.00  sec  1.02 GBytes   437 Mbits/sec                  receiver
Stream2:  [SUM]   0.00-20.00  sec  3.04 GBytes  1.31 Gbits/sec  1414             sender
Stream2:  [SUM]   0.00-20.00  sec  3.04 GBytes  1.31 Gbits/sec                  receiver
Stream2:  
Stream2:  iperf Done.
```
