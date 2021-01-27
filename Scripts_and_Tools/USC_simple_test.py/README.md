## simple_test.py to run iperf3 and bbcp tests

This is not the most beautiful Python script anybody has ever written but I've found a version of it to be really handy with some tests we've been running on the USC campus network. Use at your own risk! That being said, it's pretty straightforward to customize and test locally, and it prints out (among other things) the 'iperf3' and 'bbcp' command line it runs.

### Customize target (server) node and files to transfer

Near the top, change the DEST variable to the target node for transfers. Around line 27, change the path to the test data for transfers. In this example I'm transferring a 100G.dat, and the contents of a directory called '/mnt/chris_xfer/nsf21-528-100g'. On the next line change DESTfile to where files will be copied on the target (server) node. Please customize for your DTN.

This example is using one of our other DTNs at USC as the target, not the hpc-mdtn2.usc.edu we'll be using for the NSF testing.

### Requirements on target DTN

Besides iperf3 and bbcp being installed, you need an account on the target DTN for bbcp to write the files in the filesystem path specified in 'DESTfile'. I use my userid with a SSH key installed for passwordless access.

This script runs two parallel iperf3 streams on ports 5101 and 5102, so on the target (server) DTN, run a command something like
```
iperf3 -s -p 5101 &
iperf3 -s -p 5102 &
```
You probably have to ```systemctl stop firewalld``` to avoid any errors on your sending (client) DTN. It will bomb out with something like
```
iperf3: error - unable to connect to server: No route to host
```


