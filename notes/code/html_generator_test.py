# Example List 
#EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'], ['For Loop', 'For Loops allow you to iterate over lists'], ['Lists', 'Lists are sequences of data'] ]
EXAMPLE_LIST_OF_CONCEPTS = [1,2,3,4]

# Function to preapre the Example List 
def make_HTML_for_many_concepts(list_of_concepts):
#    i = 0
#    while i < len(EXAMPLE_LIST_OF_CONCEPTS):
#	print EXAMPLE_LIST_OF_CONCEPTS[i] 
#	i = i + 1
   for list in list_of_concepts:
	print list

make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
