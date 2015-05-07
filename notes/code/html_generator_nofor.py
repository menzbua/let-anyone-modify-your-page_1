def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="content">
    <h3>
        ''' + concept_title
    html_text_2 = '''
    </h3>
    <p>
        ''' + concept_description
    html_text_3 = '''
    </p>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_title_location = concept.find('TITLE:')
    end_title_location = concept.find('DESCRIPTION:')
    title = concept[start_title_location+7 : end_title_location-1]
    return title

def get_description(concept):
    start_desc_location = concept.find('DESCRIPTION:')
    description = concept[start_desc_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    i = 0
    while i < concept_number:
        i = i + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

TEST_TEXT = """TITLE: Why Computers are Stupid
DESCRIPTION: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
DESCRIPTION: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true.
TITLE: For Loops
DESCRIPTION: With for Loops you can go through lists and evaluate every element in the List.
The for Loops iterates as long as you have Elements in the input list. 
A List in the List is one Element as in the len Function."""


def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html


print generate_all_html(TEST_TEXT)