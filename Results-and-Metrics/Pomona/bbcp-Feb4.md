# bbcp

Pomona bbcp version:

```
14.04.14.00.1
```

100 GB file:

![slooooow](https://github.com/uschpc/NSF21-528/blob/main/Results-and-Metrics/Pomona/Screen%20Shot%202021-02-04%20at%203.54.50%20PM.png)

```
$ bbcp -v -f -P 8 -r -s 4 -F 100G.dat hpc-mdtn2.usc.edu:/tmp/pomona
bbcp: Indexing files to be copied...
bbcp: Copying 0 files in 0 directories.
bbcp: Warning: pom-itb-dgx01.campus.pomona.edu is running an older version of bbcp
bbcp: Creating /tmp/pomona
bbcp: 210204 16:05:23  1% done; 157.4 MB/s, avg 157.4 MB/s
bbcp: 210204 16:05:30  2% done; 164.7 MB/s, avg 160.9 MB/s
bbcp: 210204 16:05:37  3% done; 164.2 MB/s, avg 162.0 MB/s
bbcp: 210204 16:05:44  4% done; 163.1 MB/s, avg 162.3 MB/s
bbcp: 210204 16:05:51  6% done; 163.6 MB/s, avg 162.5 MB/s
bbcp: 210204 16:05:58  7% done; 164.1 MB/s, avg 162.8 MB/s
bbcp: 210204 16:06:05  8% done; 161.5 MB/s, avg 162.6 MB/s
bbcp: 210204 16:06:12  9% done; 169.1 MB/s, avg 163.4 MB/s
bbcp: 210204 16:06:19  10% done; 167.5 MB/s, avg 163.9 MB/s
bbcp: 210204 16:06:26  12% done; 169.3 MB/s, avg 164.4 MB/s
bbcp: 210204 16:06:33  13% done; 166.8 MB/s, avg 164.6 MB/s
bbcp: 210204 16:06:40  14% done; 167.7 MB/s, avg 164.9 MB/s
bbcp: 210204 16:06:47  15% done; 162.3 MB/s, avg 164.7 MB/s
bbcp: 210204 16:06:54  17% done; 163.6 MB/s, avg 164.6 MB/s
bbcp: 210204 16:07:01  18% done; 170.0 MB/s, avg 165.0 MB/s
bbcp: 210204 16:07:08  19% done; 159.3 MB/s, avg 164.6 MB/s
bbcp: 210204 16:07:15  20% done; 165.6 MB/s, avg 164.7 MB/s
bbcp: No space left on device writing /tmp/pomona
```
