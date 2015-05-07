# Function to output the final HTML Code
def generate_concept_HTML(title, description, text):
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
    <p>
	''' + text 
    html_text_4 = '''
    </p>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3 + html_text_4
    return full_html_text

# Function to prepare Title and Description
def make_HTML(concept):
    title = concept[0]
    description = concept[1]
    text = concept[2]
    return generate_concept_HTML(title, description, text)

# Example List 
EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language', 'Programming in Python is funny.'],
                             ['For Loop', 'For Loops allow you to iterate over lists', 'They are very helpful and reduce Code.'],
                             ['Lists', 'Lists are sequences of data', 'Lists are not so hard to understand.'] ]

# Function to preapre the Example List 
def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for list in list_of_concepts:
        concept_HTML = make_HTML(list)
        HTML = HTML + concept_HTML
    return HTML

# Execute the Program
print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)

