## Architecture overview

### The application is comprised of 1 primary and several ancillary components:
- csv5.py
- bonus.py
- plate_generator.py
- splunk files
- test

### Component overview
#### csv5.py
Main file performing data processing and writing.

#### bonus.py
Produces an alternate CSV file blueprint.

#### plate_generator.py
Not used in the current iteration due to the significant CSV generation slow down
even when processing as few as 3 numbers. Remains as a proof of concept.

#### splunk_files
Contains the dashboard xml, the search app .spl file, and the PDF version of the dashboard.

### Testing
Testing is implemented using the python standard library testing framework -- unittest.
Tests can be run by ```cd```ing into the version1 directory and running the command:
```
py -m unittest
```
