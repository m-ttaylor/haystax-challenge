## Steps to run flask application
* first, create the file `tsearch\tsearch\config.py`
  * this file should be formatted:
```CONSUMER_KEY = 'XXXXXXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXXXX'
ACCESS_KEY = 'XXXX-XXXXXXXXX'
ACCESS_SECRET = 'XXXXXXXXXXX'```
  with your twitter API credentials.

* then, in the root `tsearch` directory, run the following commands:
 ```export (on linux)/set (on windows) FLASK_APP = tsearch
 export/set TSEARCH_SETTINGS = config.py
 flask run```
 and navigate to the server's address as listed in the terminal.
