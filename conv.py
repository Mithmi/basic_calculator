import math
import re
#Done:
#Base Function Lenght, Weight, Time, Temp, Speed, Capacity, Area, Sound, Power, Radiation

#Work:
#Make Test, End Programm, Debug
#Make GUI -> combobox
#Make Presentation

def main():
	a = Question(re.compile(r"^[0-9\ ]+$"), " Input Value ")
	a_list = a.split(' ')
	print a_list

	b = raw_input('  Choose  category: Lenght , Temperature , Time , Speed , Weight , Capacity , Area , Sound , Power , Radiation	')
	if b == 'Lenght':
		Lenght(a_list)
	elif b == 'Temperature':
		Temp(a_list)
	elif b == 'Time':
		Time(a_list)
	elif b == 'Speed':
		Speed(a_list)
	elif b == 'Weight': 
		Weight(a_list)
	elif b == 'Capacity':
		Capacity(a_list)
	elif b == 'Area':
		Area(a_list)
	elif b == 'Sound':
		Sound(a_list)
	elif b == 'Power':
		Power(a_list)
	elif b == 'Radiation':
		Radiation(a_list)
		
def Question(regex, question_str):
	FLAG = False
	a = ""
	while not FLAG:
		a = raw_input(question_str).strip()
		if regex.match(a):
			FLAG = True
	return a
 

def Lenght(a_list):
	i = 0
	while i < len(a_list):
		val = float(a_list[i])
		n = raw_input('  Choose const: 1 - mm, 2 - inch, 3 - cm, 4 - meters, 5 - kilometers   ')
		
		if n == '1': ## defun Millimeters
				inch = val/25.4 # Millimeters to Inch 
				cm = val/10 # Millimeters to Centimeters
				m = cm/100 # Millimeters to Meters
				km = m/1000 # Millimeters to Kilometers
				print 	'millimeters	' , val
				print   'inch	' ,	inch
				print	'centimeters	' ,	cm
				print	'meters	' ,	m
				print	'kilometers	' ,	km
			
		if n == '2': ## defun Inch
				mm = val*25.4 # Inch to Millimeters
				cm = mm/10 # Inch to Centimeters
				m = cm/100 # Inch to Meters
				km = m/1000 # Inch to Kilometers
				print   'millimeters	', mm
				print	'inch	' , val
				print	'centimeters	', cm
				print	'meters	',	m
				print	'kilometers	',	km

		if n == '3': ## defun centimeters
				mm = val*10 # Centimeters to Millimeters
				inch = mm/25.4 # Centimeters to Inch
				m = val/100 # Centimeters to Meters
				km = m/1000 # Centimeters to Kilometers
				print   'millimeters	', mm
				print	'inch	', inch
				print	'centimeters	', val
				print	'meters	',	m
				print	'kilometers	',	km

		if n == '4': ## defun meters
				cm = val*100 # Meters to Millimeters
				mm = cm*10 # Meters to Inch
				inch = mm/25.4 # Meters to Centimeters
				km = val/1000 # Meters to Kilometers
				print   'millimeters	' , mm
				print	'centimeters	' , cm
				print	'inch	' ,	inch
				print	'meters	' ,	val
				print	'kilometers	' ,	km

		if n == '5': ## defun kilometers
				m = val*1000 # Kilometers to Meters
				cm = m*100 # Kilometers to Centimeters
				mm = cm*10 # Kilometers to Millimeters
				inch = mm/25.4 # Kilometers to Inch
				print   'millimeters	', mm
				print	'inch	', inch
				print	'cm	',	cm
				print	'meters	',	m
				print	'kilometers	' , val
		i =i +1
           

def Temp(a_list):
	i = 0
	while i < len(a_list):
		val = float(a_list[i])
		n = raw_input('  Choose const: 1 - Celsius, 2 - Fahrenheit, 3 - Kelvin   ')
		
		if n == '1': #defun Celsius
			CK = val + 273.15 # Celsius to Kelvin 
			CF = val*33.8 # Celsius to Fahrenheit
			print	'Celsius	' , val
			print	'Kelvin	' , CK
			print	'Fahrenheit	' , CF

		if n == '2': #defun Fahrenheit
			FC = val/33.8 # Fahrenheit to Celsius 
			FK = FC + 273.15 # Fahrenheit to Kelvin
			print	'Celsius	' , FC
			print	'Kelvin	' , FK
			print	'Fahrenheit	' , val

		if n == '3': #defun Kelvin   
			KC = val - 273.15 # Kelvin to Celsius 
			KF = KC*33.8 # Kelvin to Fahrenheit
			print	'Celsius	' , KC
			print	'Kelvin	' , val
			print	'Fahrenheit	' , KF
		i =i +1


def Time(a_list):
	i = 0
	while i < len(a_list):
		val = float(a_list[i])
	
             
		n = raw_input('  Choose const: 1 - milliseconds, 2 - seconds, 3 - minutes, 4 - hour, 5 - day  ')

		if n == '1': #defun milliseconds
			sec = val/1000 # Milliseconds to Seconds
			mints = sec/60 # Milliseconds to Minutes
			hour = mints/60 # Milliseconds to Hour
			day = hour/24 # Milliseconds to Day
			print	'milliseconds	' , val
			print	'seconds	' ,	sec
			print	'minutes	' ,	mints
			print	'hour	' ,	hour	
			print	'day	' ,	day

		if n == '2': #defun seconds
			ms = val*1000 # Seconds to Milliseconds
			mints = val/60 # Seconds to Minutes
			hour = mints/60 # Seconds to Hour
			day = hour/24 # Seconds to Day
			print	'milliseconds	' ,	ms
			print	'seconds	' ,	val
			print	'minutes	' ,	mints
			print	'hour	' ,	hour
			print	'day	' ,	day

		if n == '3': #defun minutes 
			sec = val*60 # Minutes to Seconds
			ms = sec*1000 # Minutes to Milliseconds
			hour = val/60 # Minutes to Hour
			day = hour/24 # Minutes to Day
			print	'milliseconds	' ,	ms
			print	'seconds	' ,	sec
			print	'minutes	' ,	val
			print	'hour	' ,	hour
			print	'day	' ,	day

		if n == '4': #defun hour 
			mints = val*60 # Hour to Minutes
			sec = mints*60 # Hour to Seconds
			ms = sec*1000 # Hour to Milliseconds
			day = val/24 # Hour to Day
			print	'milliseconds	' ,	ms
			print	'seconds	' ,	sec
			print	'minutes	' ,	mints
			print	'hour	' , val
			print	'day	' ,	day

		if n == '5': #defun day 
			hour = val*24 # Day to Hour
			mints = hour*60 # Day to Minutes
			sec = mints*60 # Day to Seconds
			ms = sec*1000 # Day to Milliseconds
			print	'milliseconds	' ,	ms
			print	'seconds	' ,	sec
			print	'minutes	' ,	mints
			print	'hour	' ,	hour
			print	'day	' ,	val
		i =i +1


def Speed(a_list):
	i = 0
	while i < len(a_list):
		val = float(a_list[i])
		n = raw_input('  Choose const: 1 - m/s, 2 - km/h, 3 - knot , 4 - miles/h	')

		if n == '1': #defun meters per second
			km = val*3.6 # Meters per Second to Kilometers per Hour
			knot = km/1.852 # Meters per Second to Knot
			miles = km/1.6093 # Meters per Second to Miles per Hour
			print	'm/s	' , val
			print	'km/h	' ,	km
			print	'knot	' ,	knot
			print	'miles/h	' ,	miles	
	

		if n == '2': #defun kilometers per hour
			mes = val/3.6 # Kilometers per Hour to Meters per Second
			knot = val/1.852 # Kilometers per Hour to Knot
			miles = val/1.6093 # Kilometers per Hour to Miles per Hour
			print	'm/s	' ,	mes
			print	'km/h	' ,	val
			print	'knot	' ,	knot
			print	'miles/h	' ,	miles

		if n == '3': #defun knot 
			km = val*1.852 # Knot to Kilometers per Hour
			mes = km/3.6 # Knot to Meters per Second
			miles = km/1.6093 # Knot to Miles per Hour
			print	'm/s	' ,	mes
			print	'km/h	' ,	km
			print	'knot	' ,	val
			print	'miles/h	' ,	miles

		if n == '4': #defun miles per hour
			km = val*1.6093 # Miles per Hour to Kilometers per Hour
			mes = km/3.6 # Miles per Hour to Meters per Second
			knot = km/1.852 # Miles per Hour to Knot
			print	'm/s	' ,	mes
			print	'km/h	' ,	km
			print	'knot	' ,	knot
			print	'miles/h	' , val
		i =i +1

def Weight(a_list):
	weight = 453.59237
	i = 0
	while i < len(a_list):
		val = float(a_list[i])
		n = raw_input('  Choose const: 1 - gram, 2 - kilogram, 3 - pound , 4 - tonne		')

		if n == '1': #defun Gram
			kg = val/1000 # Gram to Kilogram
			pound = val/weight # Gram to Pound
			tonne = kg/1000 # Gram to Tonne
			print	'gram	',	val
			print	'kilogram	',	kg
			print	'pound	',	pound
			print	'tonne	',	tonne	
	

		if n == '2': #defun Kilogram
			gram = val*1000 # Kilogram to Gram
			pound = gram/weight # Kilogram to Pound
			tonne = val/1000 # Kilogram to Tonne
			print	'gram	' ,	gram
			print	'Kilogram	' , val
			print	'pound	' ,	pound
			print	'tonne	' ,	tonne	

		if n == '3': #defun pound 
			gram = val*weight # Pound to Gram
			kg = gram/1000 # Pound to Kilogram
			tonne = kg/1000 # Pound to Tonne
			print	'gram	' ,	gram
			print	'kilogram	' ,	kg
			print	'pound	' ,	val
			print	'tonne	' ,	tonne	

		if n == '4': #defun tonne
			kg = val*1000 # Tonne to Kilogram
			gram = kg*1000 # Tonne to Gram
			pound = gram/weight # Tonne to Pound
			print	'gram	' ,	gram
			print	'pound	' ,	pound
			print	'kilogram	' ,	kg
			print	'tonne	' , val
		i =i +1

def Capacity(a_list):
	i = 0
	GCS = 2.6417205e-07 # Gallon Const US
	GCK = 2.1996925e-07 # Gallon Const UK
	BCK = 6.1102569e-09 # Barrel Const UK
	BCS = 8.3864144e-09 # Barrel Const US
	while i < len(a_list):
		val = float(a_list[i])
		n = raw_input('Choose Unit: 1 - cubic mm, 2 - cubic cm, 3 - cubic meter, 4 - liter ,5 - gallon, 6 - barrel		')
		if n == '1': #defun cubic millimeters
			ccm = val/1000 #cubic millimeters to cubic centimeters
			cm = val*1.0e-09 #cubic millimeters to cubic meters
			lit = val*1.0e-06 #cubic millimeters to liter
			gUK = val*GCK #cubic millimeters to Gallon UK
			gUS = val*GCS #cubic millimeters to Gallon US
			bUK = val*BCK #cubic millimeters to Barrel UK
			bUS = val*BCS #cubic millimeters to Barrel US
			print 'cubic millimeters	' , val
			print 'cubic centimeters	' , ccm
			print 'cubic meters	' , cm
			print 'liters	' , lit
			print 'Gallon UK	' , gUK
			print 'Gallon US	' , gUS
			print 'Barrel UK	' , bUK
			print 'Barrel US	' , bUS
			
		if n == '2': #defun cubic centimeters
			cmm = val*1000 # cubic centimeters to cubic millimeters
			cm = val*1.0e-06 # cubic centimeters to cubic meters
			lit = val/1000 # cubic centimeters to liters
			gUK = cmm*GCK # cubic centimeters to Gallon UK
			gUS = cmm*GCS # cubic centimeters to Gallon US
			bUK = cmm*BCK # cubic centimeters to Barrel UK
			bUS = cmm*BCS # cubic centimeters to Barrel US
			print 'cubic millimeters	' , cmm
			print 'cubic centimeters	' , val
			print 'cubic meters	' , cm
			print 'liters	' , lit
			print 'Gallon UK	' , gUK
			print 'Gallon US	' , gUS
			print 'Barrel UK	' , bUK
			print 'Barrel US	' , bUS
		
		if n == '3': #defun cubic meters
			lit = val*1000 # cubic meters to liters
			ccm = lit*1000 # cubic meters to cubic centimeters
			cmm = ccm*1000 # cubic meters to cubic millimeters
			gUK = cmm*GCK # cubic meters to Gallon UK
			gUS = cmm*GCS # cubic meters to Gallon US
			bUK = cmm*BCK # cubic meters to Barrel UK
			bUS = cmm*BCS # cubic meters to Barrel US 
			print 'cubic millimeters	' , cmm
			print 'cubic centimeters	' , ccm
			print 'cubic meters	' , val
			print 'liters	' , lit
			print 'Gallon UK	' , gUK
			print 'Gallon US	' , gUS
			print 'Barrel UK	' , bUK
			print 'Barrel US	' , bUS

		
		if n == '4': #defun liter
			ccm = val*1000 # liter to cubic centimeters
			cmm = ccm*1000 # liter to cubic millimeters
			cm = val/1000 # liter to cubic meters
			gUK = cmm*GCK # liter to Gallon UK
			gUS = cmm*GCS # liter to Gallon US
			bUK = cmm*BCK # liter to Barrel UK
			bUS = cmm*BCS # liter to Barrel US
			print 'cubic millimeters	' , cmm
			print 'cubic centimeters	' , ccm
			print 'cubic meters	' , cm
			print 'liters	' , val
			print 'Gallon UK	' , gUK
			print 'Gallon US	' , gUS
			print 'Barrel UK	' , bUK
			print 'Barrel US	' , bUS

			
		if n == '5': #defun Gallon
			m = raw_input(' UK or US ')
			if m == 'UK':
				lit = val*4.54609 # Gallon UK to Liter
				ccm = lit*1000 # Gallon UK to cubic centimeter
				cmm = ccm*1000 # Gallon UK to cubic millimeters
				cm = lit/1000 # Gallon UK to cubic meters
				gUS = cmm*GCS # Gallon UK to Gallon US
				bUK = cmm*BCK # Gallon UK to Barrel UK
				bUS = cmm*BCS # Gallon UK to Barrel US
				print 'cubic millimeters	' , cmm
				print 'cubic centimeters	' , ccm
				print 'cubic meters	' , cm
				print 'liters	' , lit
				print 'Gallon UK	' , val
				print 'Gallon US	' , gUS
				print 'Barrel UK	' , bUK
				print 'Barrel US	' , bUS

			
			
			if m == 'US':
				lit = val*3.7854118 # Gallon US to Liter
				ccm = lit*1000 # Gallon US to cubic centimeters
				cmm = ccm*1000 # Gallon US to cubic millimeters
				cm = lit/1000 # Gallon US to cubic meters
				gUK = cmm*GCK # Gallon US to Gallon UK
				bUK = cmm*BCK # Gallon US to Barrel UK
				bUS = cmm*BCS # Gallon US to Barrel US
				print 'cubic millimeters	' , cmm
				print 'cubic centimeters	' , ccm
				print 'cubic meters	' , cm
				print 'liters	' , lit
				print 'Gallon UK	' , gUK
				print 'Gallon US	' , val
				print 'Barrel UK	' , bUK
				print 'Barrel US	' , bUS

			
		if n == '6': #defun Barrel
			m = raw_input(' UK or US ')
			
			
			if m == 'UK':
				lit = val*163.65924 # Barrel UK to Liter
				ccm = lit*1000 # Barrel UK to cubic centimeters
				cm = lit/1000 # Barrel UK to cubic meters
				cmm = ccm*1000 # Barrel UK to cubic millimeters
				gUS = cmm*GCS # Barrel UK to Gallon US
				gUK = cmm*GCK # Barrel UK to Gallon UK
				bUS = cmm*BCS # Barrel UK to Barrel US
				print 'cubic millimeters	' , cmm
				print 'cubic centimeters	' , ccm
				print 'cubic meters	' , cm
				print 'liters	' , lit
				print 'Gallon UK	' , gUK
				print 'Gallon US	' , gUS
				print 'Barrel UK	' , val
				print 'Barrel US	' , bUS

			if m == 'US':
				lit = val*119.2404712 # Barrel US to Liter
				ccm = lit*1000 # Barrel US to cubic centimeters
				cm = lit/1000 # Barrel US to cubic meters
				cmm = ccm*1000 # Barrel US to cubic millimeters
				gUS = cmm*GCS # Barrel US to Gallon US
				gUK = cmm*GCK # Barrel US to Gallon UK
				bUK = cmm*BCK # Barrel US to Barrel UK
				print 'cubic millimeters	' , cmm
				print 'cubic centimeters	' , ccm
				print 'cubic meters	' , cm
				print 'liters	' , lit
				print 'Gallon UK	' , gUK
				print 'Gallon US	' , gUS
				print 'Barrel UK	' , bUK
				print 'Barrel US	' , val
			i = i+1
			
def Area(a_list):
	i = 0
	val = float(a_list[i])
	while i < len(a_list):
		n = raw_input('Choose Unit: 1 - square centimeter, 2 - square meter, 3 - square kilometer, 4 - hectare, 5 - are		')
		
		if n =='1': #defun Square Centimeter
			sqm = val*0.0001 # Square Centimeter to Square Meter
			sqkm = val*1.0e-10 # Square Centimeter to Square Kilometer
			hec = val*1.0e-08 # Square Centimeter to Hectare
			are = val*1.0e-06 # Square Centimeter to Are
			print 'Square Centimeter	' ,	val
			print 'Square Meter	' ,	sqm
			print 'Square Kilometer	' ,	sqkm
			print 'Hectare	' ,	hec
			print 'Are	' ,	are
			
		if n =='2': #defun Square Meter
			sqcm = val*10000 # Square Meter to Square Centimeter
			sqkm = val*1.0e-06 # Square Meter to Square Kilometer
			hec = val*0.0001 # Square Meter to Hectar
			are = val*0.01 # Square Meter to Are
			print 'Square Centimeter	' ,	sqcm
			print 'Square Meter	' ,	val
			print 'Square Kilometer	' ,	sqkm
			print 'Hectare	' ,	hec
			print 'Are	' ,	are
			
		if n =='3': #defun Square Kilometer
			sqcm = val*1.0e+10 # Square Kilometer to Square Centimeter 
			sqm = val**1000000 # Square Kilometer to Square Meter
			hec = val*100 # Square Kilometer to Hectar
			are = val*10000 # Square Kilometer to Are
			print 'Square Centimeter	' ,	sqcm
			print 'Square Meter	' ,	sqm
			print 'Square Kilometer	' ,	val
			print 'Hectare	' ,	hec
			print 'Are	' ,	are
			
		if n == '4': #defun Hectare
			sqcm = val*1.0e+08 # Hectare to Square Centimeter
			sqm = val*10000 # Hectare to Square Meter
			sqkm = val*0.01 # Hectare to Square Kilometer
			are = val*100 # Hectare to Are
			print 'Square Centimeter	' ,	sqcm
			print 'Square Meter	' ,	sqm
			print 'Square Kilometer	' ,	sqkm
			print 'Hectare	' ,	val
			print 'Are	' ,	are
			
		if n =='5': #defun Are
			sqcm = val*1000000 # Are to Square Centimeter
			sqm = val*100 # Are to Square Meter
			sqkm = val*0.0001 # Are to Square Kilometer
			hec = val*0.01 # Are to Hectare
			print 'Square Centimeter	' ,	sqcm
			print 'Square Meter	' ,	sqm
			print 'Square Kilometer	' ,	sqkm
			print 'Hectare	' ,	hec
			print 'Are	' ,	val
		i = i+1
		
def Sound(a_list):
	i = 0
	val = float(a_list[i])
	while i < len(a_list):
		n = raw_input('Choose Unit: 1 - Bel, 2 - Decibel, 3 - Neper	')
		
		if n == '1': #defun Bel
			decibel = val*10 # Bel to Decibel
			neper = val*1.1512779 # Bel to Neper
			print 'Bel	' ,	val
			print 'Decibel	' , decibel
			print 'Neper	' , neper
			
		if n == '2': #defun Decibel
			bel = val/10 # Decibel to Bel
			neper = val*0.1151278 # Decibel to Neper
			print 'Bel	' , bel
			print 'Decibel	' , val
			print 'Neper	' ,	neper
			
		if n == '3': # defun Neper
			bel = val*0.8686 # Neper to Bel
			decibel = val*8.686 # Neper to Decibel
			print 'Bel	' , bel
			print 'Decibel	' , decibel
			print 'Neper	' , val
		i = i+1
		
def Power(a_list):
	i = 0
	val = float(a_list[i])
	while i < len(a_list):
		n = raw_input('Choose Unit: 1 - Watt, 2 - Kilowatt, 3 - Megawatt, 4 - Horsepower	')
		if n == '1': #Watt
			Kw = val*0.001 # Watt to Kilowatt
			Mw = val*1.0e-06 # Watt to Megawatt
			Hp = val*0.0013596 # Watt to Horsepower
			print 'Watt	' ,	val
			print 'Kilowatt	' ,	Kw
			print 'Megawatt	' ,	Mw
			print 'Horsepower	' ,	Hp
			
		if n == '2': #Kilowatt
			w = val*1000 # Kilowatt to Watt
			Mw = val*1.0e-03 # Kilowatt to Megawatt
			Hp = val*1.3596216 # Kilowatt to Horsepower
			print 'Watt	' ,	w
			print 'Kilowatt	' ,	val
			print 'Megawatt	' ,	Mw
			print 'Horsepower	' ,	Hp
			
		if n == '3': #Megawatt
			w = val*1.0e+06 # Megawatt to Watt
			Kw = val*1000 # Megawatt to Kilowatt
			Hp = val*1359.6216173 # Megawatt to Horsepower
			print 'Watt	' ,	w
			print 'Kilowatt	' ,	Kw
			print 'Megawatt	' ,	val
			print 'Horsepower	' ,	Hp
			
		if n == '4': #Horsepower
			w = val*745.6998716 # Watt to Kilowatt
			Kw = val*0.7456999 # Watt to Megawatt
			Mw = val*0.0007457 # Watt to Horsepower
			print 'Watt	' ,	w
			print 'Kilowatt	' ,	Kw
			print 'Megawatt	' ,	Mw
			print 'Horsepower	' ,	val
		i = i+1
			
			
def Radiation(a_list):
	i = 0
	val = float(a_list[i])
	while i < len(a_list):
		n = raw_input('Choose Unit: 1 - gray/sec, 2 - rad/sec, 3 - watt/kilogram, 4 - rem/sec	')
		
		if n == '1': # Gray/sec
			rad = val*100 # Gray per sec to Rad per sec
			watt = val # Gray per sec to Watt per Kilogram
			rem = val*100 # Gray per sec to Rem per sec
			print 'Gray/sec	',	val
			print 'Rad/sec	',	rad
			print 'Watt/Kilogram	', watt
			print 'Rem/sec	', rem
	
		if n == '2': # Rad/sec
			gray = val*0.01 # Rad per sec to Gray per sec
			watt = val*0.01 # Rad per sec to Watt per Kilogram
			rem = val # Rad per sec to Rem per sec
			print 'Gray/sec	',	gray
			print 'Rad/sec	',	val
			print 'Watt/Kilogram	', watt
			print 'Rem/sec	', rem
			
		if n == '3': # Watt/Kilogram
			rad = val*100 # Watt per Kilogram to Rad per sec
			gray = val # Watt per Kilogram to Gray per sec 
			rem = val*100 # Watt per Kilogram to Rem per sec
			print 'Gray/sec	',	gray
			print 'Rad/sec	',	rad
			print 'Watt/Kilogram	', val
			print 'Rem/sec	', rem
			
		if n == '4': # Rem/sec
			rad = val # Rem per sec to Rad per sec
			watt = val*0.01 # Rem per sec to Watt per Kilogram
			gray = val*0.01 # Rem per sec to Gray per sec 
			print 'Gray/sec	',	gray
			print 'Rad/sec	',	rad
			print 'Watt/Kilogram	', watt
			print 'Rem/sec	', val	
		i = i +1
		
	
		
main()

