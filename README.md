# bartlb the scribbler
Import spreadsheets into database tables, fast. This relies heavily on how
awesome pandas is, so there's not much to this code, but it may be a handy
solution for people.

### Files
* bartlb.py - module that contains scribbler class for importing data from
csv and exporting to MySQL DB.
* example.py - example use of bartlb.py
* env.example.py - sensitive configuration file. Rename as env.py and fill in
with database credentials or pass them directly to scribbler constructor if you
don't care about security. (But seriously, don't put credentials in code).
* requirements.txt - python requirements

### Required python modules
* pandas
* sqlalchemy
