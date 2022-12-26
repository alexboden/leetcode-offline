import Question
import os
import config

def get_question_links():
    with open(config.LIST_OF_QUESTIONS) as f:
        links = f.read()

    return links.split('\n')

def create_section(section_text, OUTPUT_DIR):
    os.chdir(OUTPUT_DIR)
    new_path = os.getcwd() + f'''/{section_text[1:]}'''
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    os.chdir(f'''{section_text[1:]}''')    
    
def main():
    question_links = get_question_links()
    
    if not os.path.exists('output'):
        os.makedirs('output')
    os.chdir('output')
    
    OUTPUT_DIR = os.getcwd()
    
    for line in question_links:
        print(line)
        try:
            if line[0] == '~':
                create_section(line, OUTPUT_DIR)
            else:
                q = Question.Question(line)
                q.create_html_file()
                q.create_pdf_file()
                q.create_starter_code_file()
                
        except Exception as e:
            continue

if __name__=='__main__':
    main()