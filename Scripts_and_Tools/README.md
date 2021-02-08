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
iperf3 -i 10 -t 20 -Z -P 2 -c <TARGET DTN> -T Stream1 -p 5101 &
iperf3 -i 10 -t 20 -Z -P 2 -c <TARGET DTN> -T Stream2 -p 5102
```
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
