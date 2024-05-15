import re

ip_address = "216.08.094.196"
result = re.sub(r'\b0+(\d)', r'\1', ip_address)

print(result)

