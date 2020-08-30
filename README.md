There are two parts to generating files:
    1. A Golang program called file_gopher
    2. A Python3 wrapper called generate_files_<type>_v3.py that calls the file_gopher
    
The reason there is a Python3 wrapper is that the file_gopher creates files in a single top-level directory. Say you want to create a set of files in /tmp/test_dir. If you ran the file_gopher to create files in /tmp/test_dir underneath it would only create a directory at /tmp/test_dir/dir0 and all files and subdirectories underneath it.

The generate_files Python script simply helps create a file system "width" in /tmp/test_dir. Imagine you want to create 100 million files in /tmp/test_dir. You probably wouldn't want them all created in dir0 as that would be a ton of files in a single top-level directory. You would create them in let's say 1,000 top-level directories. That is what the Python wrapper does. In this particular case the "number of files would be 100000000 and the width 1000."

------------------------------------------------------------

Here is an example of using the file_gopher binary by itself
Usage:
  file_gopher [flags]

Flags:
  -d, --directory string     Working directory path for the data generation operation
  -n, --num-files uint       Total object (files/links) count
  -D, --dirs uint            Total directory depth
  -s, --size uint            Total size (bytes) of data set
  -l, --links uint8          Percentage of file count (--num-files) to be created as functional links
  -b, --dead-links uint8     Percentage of file count (--num-files) to be created as dead links
  -c, --compressible uint8   Percentage of data (--size) which should be compressible (approximate, Default: 50) (default 50)
  -x, --file-ext string      File extension for generated files (Default: .dat) (default ".dat")
  -f, --file-names string    File name prefix for generated files (Default: File) (default "File")
  -h, --help                 help for file_gopher

Required flag `size` has not been set
------------------------------------------------------------

Here is an example of using the generate_files_<type>_v3.py script:

> python.exe .\generate_files_win_v3.py -n 200 -w 2 -s 2048 -c 44 -d "C:\File Gopher Test4\p"
C:\File Gopher Test4\p44


Loaded Configuration:
----------------------------------------

Working Path: C:\File Gopher Test4\p44
Number of Files/Links: 100
Directory Depth:   8
Total Size: 204800
Percentage of Links: 0
Percentage of Dead Links: 0
Percentage of Compressible Data: 50

----------------------------------------
Starting in 10 seconds...

Created: C:\File Gopher Test4\p44\dir0\dir1\dir2\dir3\dir4\dir5\dir6/File0.dat
Created: C:\File Gopher Test4\p44\dir0\dir1\dir2\dir3\dir4/File1.dat
Created: C:\File Gopher Test4\p44\dir0\dir1\dir2\dir3\dir4\dir5/File2.dat
etc.

---> In this case the generate_files script created 200 files (-n 200) in two top level directories (-w 2) starting at directory count 44 (-c 44, this is denoted by the p44
-------------------------------------------------------------
