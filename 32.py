d=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"}, 
{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}] 
print("Original list: ",d) 
unique_value=set(value for dic in d for value in dic.values()) 
print("Unique value: ",unique_value)