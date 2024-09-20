

def fahr(c):
    fahrenheit = 9/5*c+32
    return fahrenheit
        
        
print("Celcius   Farenheit") 
for c in range (1,101):
   print ("%d          %.1d"% (c, (fahr(c))))
