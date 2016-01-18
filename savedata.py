import quick2wire.i2c as i2c
import pymysql
import time
import datetime
import random

adc_address1 = 0x68
adc_address2 = 0x68

adc_channel1 = 0x98
adc_channel2 = 0xB8
adc_channel3 = 0xD8
adc_channel4 = 0xF8

db_host = 'localhost'
db_user = 'root'
db_password = 'MammaMu'
db_database = 'power_data'

def getadcreading(address, channel):
	bus = i2c.I2CMaster(1)
	bus.transaction(i2c.writing_bytes(address, channel))
	time.sleep(0.001) 
	h, l, r = bus.transaction(i2c.reading(address,3))[0]
	t = (h << 8 | 1)
	#multiplication factor gotten through experiment, is based on what type of resistor is in the unipi
	v =(t*0.003472825143254)
	return v

#returns a list with two lists containing sample data
def getSamples():
	i=0
	list1 = []

	while(i < 100):
		voltage_ai1 = getadcreading(adc_address1, adc_channel1)
		list1.append(voltage_ai1)
		time.sleep(0.01)
		i = i + 1
	return list1

def average(array):
	return sum(array)/(len(array))

def compute():
	i = 0
	average_array = []
	while(i<60):
		average_array.append(average(getSamples()))
		i = i+1
	return average_array

def storeDb(volt):
	#connect to database
	connection = pymysql.connect(
		host=db_host, user=db_user, password=db_password, db = db_database, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cursor
			sql = ("INSERT INTO " . db_database . ".voltage (datetimem voltage)"
			"VALUES (%s, %s)")

			date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:00")
			data = (date, volt)

			cursor.execute(sql, data)
			connection.commit()

	finally:
		connection.close()

def main():
	while True:
		#computation of one minute of total voltage during that minute of data
		voltMinute = sum(compute())
		storeDb(voltMinute)
