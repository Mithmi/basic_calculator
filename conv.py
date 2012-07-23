import math
import re
#Done:
#Base Function Lenght, Weight, Time, Temp, Speed, Capacity, Area, Sound, Power, Radiation
#Debug

#Work:
#Make Test, End Programm
#Make GUI -> combobox
#Make Presentation

def main():
	Value = Checkvalue(re.compile(r"^[0-9\ ]+$"), " Input Value ")
	Value_list = Value.split(' ')
	print Value_list

	point = Checkpoint(re.compile(r"^[0-9\ ]+$"),"  Choose  category: \n Lenght - 0 \n Temperature - 1 \n Time - 2 \n Speed - 3 \n Weight - 4 \n Capacity - 5 \n Area - 6 \n Sound - 7 \n Power - 8 \n Radiation - 9 \n	")
	if point == '0':
		Lenght(Value_list)
	elif point == '1':
		Temp(Value_list)
	elif point == '2':
		Time(Value_list)
	elif point == '3':
		Speed(Value_list)
	elif point == '4': 
		Weight(Value_list)
	elif point == '5':
		Capacity(Value_list)
	elif point == '6':
		Area(Value_list)
	elif point == '7':
		Sound(Value_list)
	elif point == '8':
		Power(Value_list)
	elif point == '9':
		Radiation(Value_list)
		
def Checkvalue(regex, checkvalue_str):
	FLAG = False
	Value = ""
	while not FLAG:
		Value = raw_input(checkvalue_str).strip()
		if regex.match(Value):
			FLAG = True
	return Value
 
def Checkpoint(regex, checkpoint_str):
	FLAG = False
	point = ""
	while not FLAG:
		point = raw_input(checkpoint_str).strip()
		if regex.match(point):
			FLAG = True
	return point

def Checknewpoint(regex, checknewpoint_str):
	FLAG = False
	newpoint = ""
	while not FLAG:
		newpoint = raw_input(checknewpoint_str).strip()
		if regex.match(newpoint):
			FLAG = True
	return newpoint

def Lenght(Value_list):
	i = 0
	while i < len(Value_list):
		val = float(Value_list[i])
		newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'  Choose const: \n mm - 0 \n inch - 1 \n cm - 2 \n meters - 3 \n kilometers - 4	')
		
		if newpoint == '0': ## defun Millimeters
				inch = val/25.4 # Millimeters to Inch 
				cm = val/10 # Millimeters to Centimeters
				m = cm/100 # Millimeters to Meters
				km = m/1000 # Millimeters to Kilometers
				print 	'millimeters' , val,'\n' 'inch' ,	inch,'\n' 'centimeters' ,cm ,'\n' 'meters' ,	m,'\n' 'kilometers' ,	km
			
		if newpoint == '1': ## defun Inch
				mm = val*25.4 # Inch to Millimeters
				cm = mm/10 # Inch to Centimeters
				m = cm/100 # Inch to Meters
				km = m/1000 # Inch to Kilometers
				print 	'millimeters' , mm,'\n' 'inch' ,	val,'\n' 'centimeters' ,cm ,'\n' 'meters' ,	m,'\n' 'kilometers' ,	km
				
		if newpoint == '2': ## defun centimeters
				mm = val*10 # Centimeters to Millimeters
				inch = mm/25.4 # Centimeters to Inch
				m = val/100 # Centimeters to Meters
				km = m/1000 # Centimeters to Kilometers
				print 	'millimeters' , mm,'\n' 'inch' ,	inch,'\n' 'centimeters' ,val ,'\n' 'meters' ,	m,'\n' 'kilometers' ,	km

		if newpoint == '3': ## defun meters
				cm = val*100 # Meters to Millimeters
				mm = cm*10 # Meters to Inch
				inch = mm/25.4 # Meters to Centimeters
				km = val/1000 # Meters to Kilometers
				print 	'millimeters' , mm,'\n' 'inch' ,	inch,'\n' 'centimeters' ,cm ,'\n' 'meters' ,	val,'\n' 'kilometers' ,	km

		if newpoint == '4': ## defun kilometers
				m = val*1000 # Kilometers to Meters
				cm = m*100 # Kilometers to Centimeters
				mm = cm*10 # Kilometers to Millimeters
				inch = mm/25.4 # Kilometers to Inch
				print 	'millimeters' , mm,'\n' 'inch' ,	inch,'\n' 'centimeters' ,cm ,'\n' 'meters' ,	m,'\n' 'kilometers' ,	val
				
		i =i +1
           

def Temp(Value_list):
	i = 0
	while i < len(Value_list):
		val = float(Value_list[i])
		newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'  Choose const: \n Celsius - 1 \n Fahrenheit - 2 \n Kelvin - 3	')
		
		if newpoint == '1': #defun Celsius
			CK = val + 273.15 # Celsius to Kelvin 
			CF = val*33.8 # Celsius to Fahrenheit
			print	'Celsius' , val ,'\n','Kelvin' , CK,'\n','Fahrenheit' , CF

		if newpoint == '2': #defun Fahrenheit
			FC = val/33.8 # Fahrenheit to Celsius 
			FK = FC + 273.15 # Fahrenheit to Kelvin
			print	'Celsius' , FC ,'\n','Kelvin' , FK,'\n','Fahrenheit' , val

		if newpoint == '3': #defun Kelvin   
			KC = val - 273.15 # Kelvin to Celsius 
			KF = KC*33.8 # Kelvin to Fahrenheit
			print	'Celsius' , KC ,'\n','Kelvin' , val,'\n','Fahrenheit' , KF
		i =i +1


def Time(Value_list):
	i = 0
	while i < len(Value_list):
		val = float(Value_list[i])
		newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'  Choose const: \n milliseconds - 1 \n seconds - 2 \n minutes - 3 \n hour - 4 \n day - 5	')

		if newpoint == '1': #defun milliseconds
			sec = val/1000 # Milliseconds to Seconds
			mints = sec/60 # Milliseconds to Minutes
			hour = mints/60 # Milliseconds to Hour
			day = hour/24 # Milliseconds to Day
			print	'milliseconds' , val, '\n' , 'seconds' , sec, '\n', 'minutes' , mints, '\n', 'hour' , hour, '\n', 'day' , day

		if newpoint == '2': #defun seconds
			ms = val*1000 # Seconds to Milliseconds
			mints = val/60 # Seconds to Minutes
			hour = mints/60 # Seconds to Hour
			day = hour/24 # Seconds to Day
			print	'milliseconds' , ms, '\n' , 'seconds' , val, '\n', 'minutes' , mints, '\n', 'hour' , hour, '\n', 'day' , day
			
		if newpoint == '3': #defun minutes 
			sec = val*60 # Minutes to Seconds
			ms = sec*1000 # Minutes to Milliseconds
			hour = val/60 # Minutes to Hour
			day = hour/24 # Minutes to Day
			print	'milliseconds' , ms, '\n' , 'seconds' , sec, '\n', 'minutes' , val, '\n', 'hour' , hour, '\n', 'day' , day
			
		if newpoint == '4': #defun hour 
			mints = val*60 # Hour to Minutes
			sec = mints*60 # Hour to Seconds
			ms = sec*1000 # Hour to Milliseconds
			day = val/24 # Hour to Day
			print	'milliseconds' , ms, '\n' , 'seconds' , sec, '\n', 'minutes' , mints, '\n', 'hour' , val, '\n', 'day' , day
			
		if newpoint == '5': #defun day 
			hour = val*24 # Day to Hour
			mints = hour*60 # Day to Minutes
			sec = mints*60 # Day to Seconds
			ms = sec*1000 # Day to Milliseconds
			print	'milliseconds' , ms, '\n' , 'seconds' , sec, '\n', 'minutes' , mints, '\n', 'hour' , hour, '\n', 'day' , val
			
		i =i +1


def Speed(Value_list):
	i = 0
	while i < len(Value_list):
		val = float(Value_list[i])
		newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'  Choose const: \n m/s - 1 \n km/h - 2 \n knot - 3 \n miles/h - 4	')

		if newpoint == '1': #defun meters per second
			km = val*3.6 # Meters per Second to Kilometers per Hour
			knot = km/1.852 # Meters per Second to Knot
			miles = km/1.6093 # Meters per Second to Miles per Hour
			print	'm/s' , val, '\n', 'km/h' ,	km, '\n', 'knot' ,	knot, '\n', 'miles/h' ,	miles			
			
		if newpoint == '2': #defun kilometers per hour
			mes = val/3.6 # Kilometers per Hour to Meters per Second
			knot = val/1.852 # Kilometers per Hour to Knot
			miles = val/1.6093 # Kilometers per Hour to Miles per Hour
			print	'm/s' , mes, '\n', 'km/h' ,	val, '\n', 'knot' ,	knot, '\n', 'miles/h' ,	miles
			
		if newpoint == '3': #defun knot 
			km = val*1.852 # Knot to Kilometers per Hour
			mes = km/3.6 # Knot to Meters per Second
			miles = km/1.6093 # Knot to Miles per Hour
			print	'm/s' , mes, '\n', 'km/h' ,	km, '\n', 'knot' ,	val, '\n', 'miles/h' ,	miles
			
		if newpoint == '4': #defun miles per hour
			km = val*1.6093 # Miles per Hour to Kilometers per Hour
			mes = km/3.6 # Miles per Hour to Meters per Second
			knot = km/1.852 # Miles per Hour to Knot
			print	'm/s' , mes, '\n', 'km/h' ,	km, '\n', 'knot' ,	knot, '\n', 'miles/h' ,	val
			
		i =i +1

def Weight(Value_list):
	weight = 453.59237
	i = 0
	while i < len(Value_list):
		val = float(Value_list[i])
		newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'  Choose const: \n gram - 1 \n kilogram - 2 \n pound - 3 \n tonne - 4	')

		if newpoint == '1': #defun Gram
			kg = val/1000 # Gram to Kilogram
			pound = val/weight # Gram to Pound
			tonne = kg/1000 # Gram to Tonne
			print	'gram',	val, '\n', 'kilogram',	kg, '\n', 'pound',	pound , '\n', 'tonne',	tonne	
	

		if newpoint == '2': #defun Kilogram
			gram = val*1000 # Kilogram to Gram
			pound = gram/weight # Kilogram to Pound
			tonne = val/1000 # Kilogram to Tonne
			print	'gram',	gram, '\n', 'kilogram',	val, '\n', 'pound',	pound , '\n', 'tonne',	tonne

		if newpoint == '3': #defun pound 
			gram = val*weight # Pound to Gram
			kg = gram/1000 # Pound to Kilogram
			tonne = kg/1000 # Pound to Tonne
			print	'gram',	gram, '\n', 'kilogram',	kg, '\n', 'pound',	val , '\n', 'tonne',	tonne

		if newpoint == '4': #defun tonne
			kg = val*1000 # Tonne to Kilogram
			gram = kg*1000 # Tonne to Gram
			pound = gram/weight # Tonne to Pound
			print	'gram',	gram, '\n', 'kilogram',	kg, '\n', 'pound',	pound , '\n', 'tonne',	val
			
		i =i +1

def Capacity(Value_list):
	i = 0
	GCS = 2.6417205e-07 # Gallon Const US
	GCK = 2.1996925e-07 # Gallon Const UK
	BCK = 6.1102569e-09 # Barrel Const UK
	BCS = 8.3864144e-09 # Barrel Const US
	while i < len(Value_list):
		val = float(Value_list[i])
		newpoint = Checknewpoint(re.compile(r"^[0-9\ ]+$"),'Choose Unit: \n cubic mm - 1 \n cubic cm - 2 \n cubic meter - 3 \n liter - 4 \n gallon - 5 \n barrel - 6	')
		if newpoint == '1': #defun cubic millimeters
			ccm = val/1000 #cubic millimeters to cubic centimeters
			cm = val*1.0e-09 #cubic millimeters to cubic meters
			lit = val*1.0e-06 #cubic millimeters to liter
			gUK = val*GCK #cubic millimeters to Gallon UK
			gUS = val*GCS #cubic millimeters to Gallon US
			bUK = val*BCK #cubic millimeters to Barrel UK
			bUS = val*BCS #cubic millimeters to Barrel US
			print 'cubic millimeters', val,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS 
			
		if newpoint == '2': #defun cubic centimeters
			cmm = val*1000 # cubic centimeters to cubic millimeters
			cm = val*1.0e-06 # cubic centimeters to cubic meters
			lit = val/1000 # cubic centimeters to liters
			gUK = cmm*GCK # cubic centimeters to Gallon UK
			gUS = cmm*GCS # cubic centimeters to Gallon US
			bUK = cmm*BCK # cubic centimeters to Barrel UK
			bUS = cmm*BCS # cubic centimeters to Barrel US
			print 'cubic millimeters', cmm,'\n','cubic centimeters', val,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS
		
		if newpoint == '3': #defun cubic meters
			lit = val*1000 # cubic meters to liters
			ccm = lit*1000 # cubic meters to cubic centimeters
			cmm = ccm*1000 # cubic meters to cubic millimeters
			gUK = cmm*GCK # cubic meters to Gallon UK
			gUS = cmm*GCS # cubic meters to Gallon US
			bUK = cmm*BCK # cubic meters to Barrel UK
			bUS = cmm*BCS # cubic meters to Barrel US 
			print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', val,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS

		
		if newpoint == '4': #defun liter
			ccm = val*1000 # liter to cubic centimeters
			cmm = ccm*1000 # liter to cubic millimeters
			cm = val/1000 # liter to cubic meters
			gUK = cmm*GCK # liter to Gallon UK
			gUS = cmm*GCS # liter to Gallon US
			bUK = cmm*BCK # liter to Barrel UK
			bUS = cmm*BCS # liter to Barrel US
			print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', val,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS

			
		if newpoint == '5': #defun Gallon
			m = raw_input(' UK or US ')
			UK = 0
			US = 0
			if m == 'UK':
				lit = val*4.54609 # Gallon UK to Liter
				ccm = lit*1000 # Gallon UK to cubic centimeter
				cmm = ccm*1000 # Gallon UK to cubic millimeters
				cm = lit/1000 # Gallon UK to cubic meters
				gUS = cmm*GCS # Gallon UK to Gallon US
				bUK = cmm*BCK # Gallon UK to Barrel UK
				bUS = cmm*BCS # Gallon UK to Barrel US
				print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', val,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', bUS		
			UK = 1
			
			if m == 'US':
				lit = val*3.7854118 # Gallon US to Liter
				ccm = lit*1000 # Gallon US to cubic centimeters
				cmm = ccm*1000 # Gallon US to cubic millimeters
				cm = lit/1000 # Gallon US to cubic meters
				gUK = cmm*GCK # Gallon US to Gallon UK
				bUK = cmm*BCK # Gallon US to Barrel UK
				bUS = cmm*BCS # Gallon US to Barrel US
				print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', val,'\n','Barrel UK', bUK,'\n','Barrel US', bUS
			US = 1
		##	if US  UK :
		##		print "Error #0: Try to Input: UK or US "
			
		if newpoint == '6': #defun Barrel
			m = raw_input(' UK or US ')
			
			
			if m == 'UK':
				lit = val*163.65924 # Barrel UK to Liter
				ccm = lit*1000 # Barrel UK to cubic centimeters
				cm = lit/1000 # Barrel UK to cubic meters
				cmm = ccm*1000 # Barrel UK to cubic millimeters
				gUS = cmm*GCS # Barrel UK to Gallon US
				gUK = cmm*GCK # Barrel UK to Gallon UK
				bUS = cmm*BCS # Barrel UK to Barrel US
				print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', val,'\n','Barrel US', bUS
			elif m <> 'UK':	
				print "Error #0: Try to Input: UK "

			if m == 'US':
				lit = val*119.2404712 # Barrel US to Liter
				ccm = lit*1000 # Barrel US to cubic centimeters
				cm = lit/1000 # Barrel US to cubic meters
				cmm = ccm*1000 # Barrel US to cubic millimeters
				gUS = cmm*GCS # Barrel US to Gallon US
				gUK = cmm*GCK # Barrel US to Gallon UK
				bUK = cmm*BCK # Barrel US to Barrel UK
				print 'cubic millimeters', cmm,'\n','cubic centimeters', ccm,'\n','cubic meters', cm,'\n','liters', lit,'\n','Gallon UK', gUK,'\n','Gallon US', gUS,'\n','Barrel UK', bUK,'\n','Barrel US', val
			elif m <> 'US':
				print "Error #0: Try to Input: US "	
				
		i = i+1
			
def Area(Value_list):
	i = 0
	val = float(Value_list[i])
	while i < len(Value_list):
		n = raw_input('Choose Unit: \n square centimeter - 1 \n square meter - 2 \n square kilometer - 3 \n hectare - 4 \n are - 5		')
		
		if n =='1': #defun Square Centimeter
			sqm = val*0.0001 # Square Centimeter to Square Meter
			sqkm = val*1.0e-10 # Square Centimeter to Square Kilometer
			hec = val*1.0e-08 # Square Centimeter to Hectare
			are = val*1.0e-06 # Square Centimeter to Are
			print 'Square Centimeter',	val,'\n','Square Meter',	sqm,'\n','Square Kilometer',	sqkm,'\n','Hectare',	hec,'\n','Are',	are
			
		if n =='2': #defun Square Meter
			sqcm = val*10000 # Square Meter to Square Centimeter
			sqkm = val*1.0e-06 # Square Meter to Square Kilometer
			hec = val*0.0001 # Square Meter to Hectar
			are = val*0.01 # Square Meter to Are
			print 'Square Centimeter',	sqcm,'\n','Square Meter',	val,'\n','Square Kilometer',	sqkm,'\n','Hectare',	hec,'\n','Are',	are
			
		if n =='3': #defun Square Kilometer
			sqcm = val*1.0e+10 # Square Kilometer to Square Centimeter 
			sqm = val**1000000 # Square Kilometer to Square Meter
			hec = val*100 # Square Kilometer to Hectar
			are = val*10000 # Square Kilometer to Are
			print 'Square Centimeter',	sqcm,'\n','Square Meter',	sqm,'\n','Square Kilometer',	val,'\n','Hectare',	hec,'\n','Are',	are
			
		if n == '4': #defun Hectare
			sqcm = val*1.0e+08 # Hectare to Square Centimeter
			sqm = val*10000 # Hectare to Square Meter
			sqkm = val*0.01 # Hectare to Square Kilometer
			are = val*100 # Hectare to Are
			print 'Square Centimeter',	sqcm,'\n','Square Meter',	sqm,'\n','Square Kilometer',	sqkm,'\n','Hectare',	val,'\n','Are',	are
			
		if n =='5': #defun Are
			sqcm = val*1000000 # Are to Square Centimeter
			sqm = val*100 # Are to Square Meter
			sqkm = val*0.0001 # Are to Square Kilometer
			hec = val*0.01 # Are to Hectare
			print 'Square Centimeter',	sqcm,'\n','Square Meter',	sqm,'\n','Square Kilometer',	sqkm,'\n','Hectare',	hec,'\n','Are',	val
			
		i = i+1
		
def Sound(Value_list):
	i = 0
	val = float(Value_list[i])
	while i < len(Value_list):
		n = raw_input('Choose Unit: \n Bel - 1 \n Decibel - 2 \n Neper - 3	')
		
		if n == '1': #defun Bel
			decibel = val*10 # Bel to Decibel
			neper = val*1.1512779 # Bel to Neper
			print 'Bel', val,'\n','Decibel', decibel,'\n','Neper', neper
			
			
		if n == '2': #defun Decibel
			bel = val/10 # Decibel to Bel
			neper = val*0.1151278 # Decibel to Neper
			print 'Bel', bel,'\n','Decibel', val,'\n','Neper', neper
			
		if n == '3': # defun Neper
			bel = val*0.8686 # Neper to Bel
			decibel = val*8.686 # Neper to Decibel
			print 'Bel', bel,'\n','Decibel', decibel,'\n','Neper', val
			
		i = i+1
		
def Power(Value_list):
	i = 0
	val = float(Value_list[i])
	while i < len(Value_list):
		n = raw_input('Choose Unit: \n Watt - 1 \n  Kilowatt - 2 \n  Megawatt - 3 \n  Horsepower - 4	')
		if n == '1': #Watt
			Kw = val*0.001 # Watt to Kilowatt
			Mw = val*1.0e-06 # Watt to Megawatt
			Hp = val*0.0013596 # Watt to Horsepower
			print 'Watt',	val,'\n','Kilowatt',	Kw,'\n','Megawatt',	Mw,'\n','Horsepower',	Hp
			
		if n == '2': #Kilowatt
			w = val*1000 # Kilowatt to Watt
			Mw = val*1.0e-03 # Kilowatt to Megawatt
			Hp = val*1.3596216 # Kilowatt to Horsepower
			print 'Watt',	w,'\n','Kilowatt',	val,'\n','Megawatt',	Mw,'\n','Horsepower',	Hp
			
		if n == '3': #Megawatt
			w = val*1.0e+06 # Megawatt to Watt
			Kw = val*1000 # Megawatt to Kilowatt
			Hp = val*1359.6216173 # Megawatt to Horsepower
			print 'Watt',	w,'\n','Kilowatt',	Kw,'\n','Megawatt', val,'\n','Horsepower',	Hp
			
		if n == '4': #Horsepower
			w = val*745.6998716 # Watt to Kilowatt
			Kw = val*0.7456999 # Watt to Megawatt
			Mw = val*0.0007457 # Watt to Horsepower
			print 'Watt',	w,'\n','Kilowatt',	Kw,'\n','Megawatt',	Mw,'\n','Horsepower',	val
			
		i = i+1
			
			
def Radiation(Value_list):
	i = 0
	val = float(Value_list[i])
	while i < len(Value_list):
		n = raw_input('Choose Unit: \n gray/sec - 1 \n rad/sec - 2 \n watt/kilogram - 3 \n rem/sec - 4	')
		
		if n == '1': # Gray/sec
			rad = val*100 # Gray per sec to Rad per sec
			watt = val # Gray per sec to Watt per Kilogram
			rem = val*100 # Gray per sec to Rem per sec
			print 'Gray/sec',	val,'\n','Rem/sec', rem,'\n','Watt/Kilogram', watt,'\n','Rad/sec',	rad
	
		if n == '2': # Rad/sec
			gray = val*0.01 # Rad per sec to Gray per sec
			watt = val*0.01 # Rad per sec to Watt per Kilogram
			rem = val # Rad per sec to Rem per sec
			print 'Gray/sec',	gray,'\n','Rem/sec', rem,'\n','Watt/Kilogram', watt,'\n','Rad/sec',	val
			
		if n == '3': # Watt/Kilogram
			rad = val*100 # Watt per Kilogram to Rad per sec
			gray = val # Watt per Kilogram to Gray per sec 
			rem = val*100 # Watt per Kilogram to Rem per sec
			print 'Gray/sec',	gray,'\n','Rem/sec', rem,'\n','Watt/Kilogram', val,'\n','Rad/sec',	rad
			
		if n == '4': # Rem/sec
			rad = val # Rem per sec to Rad per sec
			watt = val*0.01 # Rem per sec to Watt per Kilogram
			gray = val*0.01 # Rem per sec to Gray per sec 
			print 'Gray/sec',	gray,'\n','Rem/sec', val,'\n','Watt/Kilogram', watt,'\n','Rad/sec',	rad
				
		i = i +1
		
	
		
main()

