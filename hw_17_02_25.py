#1merging two dictionaries
def merge_dicts(d1,d2):
    d1.update(d2)  # Directly update d1 with d2's values
    return d1
dict1={"a":1,"b":2}
dict2={"b":4,"c":3}
print(merge_dicts(dict1,dict2))

#2two lists and return a dictionary
def common_elements_count(list1,list2):
    common_dict={}  # Dictionary to store common elements and their counts
    for item in set(list1) & set(list2):  # Find common elements
        common_dict[item]=min(list1.count(item),list2.count(item))# Store minimum count
    return common_dict
list1=[1, 2, 2, 3, 4, 4, 4]
list2=[2, 2, 4, 4, 5, 6]
print(common_elements_count(list1,list2))

#3list of tuple converts into dictionary
def tuples_to_dict(tuples_list):
    return dict(tuples_list)  # Convert list of tuples into a dictionary
tuples=[("a",1),("b",2),("c",3)]
print(tuples_to_dict(tuples))  


