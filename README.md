# Python module

# Pavel_Karunas_Day3_Snapshots Application

Description:
1. This application takes following system metrics: CPU load percent, Disk space used, RAM used, Disk IO write time and Net packets send.
2. Application recives two parameters:interval betveen snapshots (default value 300 in seconds) and output file format extension (possible options txt and json (default is txt)).
3. After application is statrted, file result.txt/json with system diagnostic information will be created in current folder.

Requirements:
Python version 3.6 or above
Installed psutil with pip

Installation:
Clone the repo and navigate to this folder.

  $ pip install .

  $ snapshot


Uninstallation:

  $ pip uninstall zoo-example

Examples of use:

  $ snapshot

  $ snapshot 60 json

  $ snapshot 20 txt

