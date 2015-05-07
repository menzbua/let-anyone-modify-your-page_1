# Function to output the final HTML Code
def generate_concept_HTML(title, description):
    html_text_1 = '''
<div class="content">
    <h3>
        ''' + title
    html_text_2 = '''
    </h3>
    <p>
        ''' + description
    html_text_3 = '''
    </p>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

# Function to prepare Title and Description
def make_HTML(concept):
    title = concept[0]
    description = concept[1]
    return generate_concept_HTML(title, description)

# Example List 
EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]

# Function to preapre the Example List 
def make_HTML_for_many_concepts(list_of_concepts):
    for list in list_of_concepts:
        print make_HTML(list)

# Execute the Program
make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
