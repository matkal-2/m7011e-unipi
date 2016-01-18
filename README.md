# m7011e-unipi

#Dependencies
##Webserver
* Python 3.0+ 
* LAMP https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-debian

##Python script
* Quick2wire-python-api https://github.com/quick2wire/quick2wire-python-api/blob/master/doc/getting-started-with-i2c.md
* PyMySQL https://github.com/PyMySQL/PyMySQL

#Setup

##Webserver
1. Install LAMP
2. Make sure the apache2 service is running by typing 'service apache2 status'
3. Place the index.phtml file in /var/bin/www/

##Python script
1. Make sure to follow the installation instructions for quick2wire-python-api
2. Direct the import path towards quick2wire-python-api at the top of the script incase the module was not imported properly on first try.
3. Install PyMySQL in order to be able to store data in the database. 
4. Run the script

#API
* **/** - Returns the last 1000 datapoints which represent the last 1000 minutes.
* **?date=year-month-day** - returns the every minute of sample from that specific day.
* **?format=hour** - returns the last 24 datapoints which represent the last 24 hours.
