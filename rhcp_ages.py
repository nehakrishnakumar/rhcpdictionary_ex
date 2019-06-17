Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> rhcp_ages = {"Anthony" : 56, "Flea" : 56, "Chad" : 57, "Josh" : 39}
>>> for i in rhcp_ages
SyntaxError: invalid syntax
>>> for i in rhcp_ages {
	
SyntaxError: invalid syntax
>>> # do not press enter after creating a for loop, and do not try to make brackets similar to how it works in Java
>>> for i in rhcp_ages
	print(i)
	
SyntaxError: invalid syntax
>>> # forgot to include colons lol
>>> for i in rhcp_ages:
	print(i)
	if rhcp_ages.get (i) >= 65:
		print (i + " qualifies for Medicare")
	else:
		print (i + " does not qualify for Medicare")

Anthony
Anthony does not qualify for Medicare
Flea
Flea does not qualify for Medicare
Chad
Chad does not qualify for Medicare
Josh
Josh does not qualify for Medicare
>>> # based on the value for their ages, print whether they qualify for Medicare or not
z = rhcp_age.popItem()
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    z = rhcp_age.popItem()
NameError: name 'rhcp_age' is not defined
>>> # whoops
>>> z = rhcp_ages.popItem()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    z = rhcp_ages.popItem()
AttributeError: 'dict' object has no attribute 'popItem'
>>> # popitem is not lower camel case, whoops again
>>> z = rhcp_ages.popitem();
>>> print z;
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(z)?
>>> print (z)
('Josh', 39)
>>> # prints the key and the value
>>> # ditch the semicolons please haha
