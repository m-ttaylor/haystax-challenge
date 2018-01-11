# haystax-challenge

* `/problem8/` contains solution to problem 8 and the script used to generate sample data
* `/problem9/` contains a single .html page with all necessary scripts
  * user data goes through simple validation before allowing the register button to be clicked
  * data is not saved or used, and no verification email/text is sent
* /tsearch/ contains a flask project for problem 10. 
  * API keys are expected in a file `tsearch/tsearch/config.py`. Application must be deployed locally, with own twitter API keys.