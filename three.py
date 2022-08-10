join_list=['anu','sr','ee']
print(''.join(join_list))
print('#'.join(join_list))
print('.'.join(join_list))
print('$'.join(join_list))


string_partition='hiiamanusreesreenivasan'
print(string_partition.partition('e'))

string_replace='anu is good girl'
print(string_replace.replace('anu','girl'))

string_replace='anu is good,anu is good,anu is from kerala'
print(string_replace.replace('anu','parju',2))

swapcase_string='your Are Very Beautiful'
print(swapcase_string.swapcase())

startwith_string='you are very beautiful'
print(startwith_string.startswith('you'))