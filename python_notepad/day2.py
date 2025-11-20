import keyword

all_keys=keyword.kwlist
print(all_keys)
print(len(all_keys))

complete_keys=keyword.softkwlist
print(complete_keys)
print(len(complete_keys))
print((len(all_keys)+len(complete_keys)))
total_keys=all_keys+complete_keys
print(total_keys)
print(len(total_keys))
