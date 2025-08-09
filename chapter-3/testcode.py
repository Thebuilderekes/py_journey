
name = True
age = False
message = "eligible"
short_circuit_message = "short circuit because age is false"


print(message) if age and name else print(short_circuit_message)
