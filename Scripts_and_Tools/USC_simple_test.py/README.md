## simple_test.py to run iperf3 and bbcp tests

This is not the most beautiful Python script anybody has ever written but I've found a version of it to be really handy with some tests we've been running on the USC campus network. Use at your own risk! That being said, it's pretty straightforward to customize and test locally, and it prints out (among other things) the 'iperf3' and 'bbcp' command line it runs.

### Customize target (server) node and files to transfer

Near the top, change the DEST variable to the target node for transfers. Around line 27, change the path to the test data for transfers. In this example I'm transferring a 100G.dat, and the contents of a directory called '/mnt/chris_xfer/nsf21-528-100g'. Please customize for your DTN.


