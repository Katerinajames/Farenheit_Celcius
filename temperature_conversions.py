def fahr(c):
    fahrenheit = 9/5*c+32
    return fahrenheit

def cel(c):
    celsius = 5.0 / 9.0 * ( c - 32 );
    return celsius


c=float(input("Enter temperature degrees \n"))

string=input("Enter the equivalent temperature you wish to calculate \n") 

if string=="Farenheit":
	print ("The temperature in Farenheit scale is %.2f"%( fahr(c)))

if string=="Celcius":
    print ("The temperature in Celcius scale is %.2f"%cel(c))
