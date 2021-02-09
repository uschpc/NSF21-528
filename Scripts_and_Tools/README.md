## Command line scripts, utilities, etc

### Command line for tests using the USC Data Transfer Node as an example:

Ping and traceroute:
```
ping hpc-mdtn2.usc.edu
```
```
traceroute hpc-mdtn2.usc.edu
```

iperf3 with two streams (running concurrently, two processes at once)-
```
iperf3 -i 10 -t 20 -Z -P 2 -c hpc-mdtn2.usc.edu -T Stream1 -p 5101 &
iperf3 -i 10 -t 20 -Z -P 2 -c hpc-mdtn2.usc.edu -T Stream2 -p 5102
```

#### It's suggested to cut and paste the above script in a BASH or other shell script and execute it so two streams are running *at the same time.*

### iperf3 Ports
On the USC DTN, iperf3 is running on ports 5101-5120. Only one iperf3 port can be used at a time, so if two people try to run the iperf3 tests you might get an error that the port is in use. In that case, try using ports 5103 and 5104, for instance. *NB: The iperf3 tests just take a few seconds to run*

### We are collecting the outputs in the *Results-and-Metrics* folder in this repo. I have created some subfolders for each institution to upload data, please feel free to create one if you don't see yours. Or, email or message me the output on Slack and I can upload it.

## If time permits, file transfer using bbcp (we are focusing on ping, traceroute and iperf3 right now)

bbcp-
https://www.slac.stanford.edu/~abh/bbcp/

Scroll down to the 'Download' section:

https://www.slac.stanford.edu/~abh/bbcp/bin/

```
bbcp -v -f -P 8 -r -s 4 -F <CLIENT FILESYSEM>/100G.dat <TARGET DTN>:<TARGET FILESYSTEM>
```  
Also you can say:
```
bbcp -v -f -P 8 -r -s 4 -F <CLIENT FILESYSEM>/nsf21-528-100g <TARGET DTN>:<TARGET FILESYSTEM>
```
That will copy the nsf21-528-100g directory and all it's contents to the target.
