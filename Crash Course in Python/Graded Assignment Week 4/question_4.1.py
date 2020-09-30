def format_address(address_string):
 # Declare variables
 home_no = 0
 home_address = ' '
 parts = address_string.split()
 # Separate the address string into parts
 for part in parts:
   if part.isdigit():
     home_no = part
   else:
     home_address += part + ' '
 # Traverse through the address parts
 
   # Determine if the address part is the
   # house number or part of the street name
 # Does anything else need to be done  
 # before returning the result?
 
 # Return the formatted string  
 return "house number {} on street named {}".format(home_no, home_address)
print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"