#  Upper()
# The upper() method converts a string to upper case.
name = "Dipesh"
print(name.upper())

# lower()
# The lower() method converts a string to lower case.
name = "Dipesh"
print(name.lower())

# strip() :
# The strip() method removes any white spaces before and after the string.
name = "  Dipesh  "
print(name.strip())

# rstrip() :
# the rstrip() removes any trailing characters.
# but it doesn't removes any trailing characters before the string.
name = "!!!Dipesh!!!"
print(name.rstrip("!"))

# replace() :
# The replace() method replaces all occurences of a string with another string.
name = "!!!Dipesh!!!"
print(name.replace("!","-"))

# split() :
# The split() method splits the given string at the specified instance and returns the separated strings as list items.
name = "!!! Dipesh !!!"
print(name.split(" "))

# capitalize() :
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
name = "dipeSH"
print(name.capitalize())

# count() :
# The count() method returns the number of times the given value has occurred within the given string.
name = "Dipesh,Dipesh,Dipesh"
print(name.count("Dipesh"))

# endswith() :
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
name = "Dipesh!!!"
print(name.endswith("!"))
