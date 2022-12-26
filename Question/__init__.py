import requests, json, os, pdfkit
from Question.constants import QUESTION_QUERY
from config import DEFAULT_LANGUAGE_EXTENSION, DEFAULT_LANGUAGE_SLUG

class Question:
    def __init__(self, question_link):
        self.question_link = question_link
        self.question_id = ""
        self.title = ""
        self.slug = ""
        self.starting_code = ""
        self.baseJSON = {
            "operationName": "questionData",
            "variables": {
                    "titleSlug": "PLACEHOLDER"
            },
            "query": QUESTION_QUERY
        }
        
        self.leetcode_api_endpoint = 'https://leetcode.com/graphql' 
        self.html_str = self.get_html_str() 
    
    def get_html_str(self):
        self.slug = self.question_link.split('https://leetcode.com/problems/', 1)[1]
        self.baseJSON['variables']['titleSlug'] = self.slug
        resp = requests.get(self.leetcode_api_endpoint, json=self.baseJSON)
        x = json.loads(resp.text)
        self.question_id = x['data']['question']['questionId']
        self.title = x['data']['question']['title']
        content = x['data']['question']['content']
        difficulty = x['data']['question']['difficulty']
        link = f'''<a href="{self.question_link  }">{self.question_link  }</a>'''        
        html_str = f'''<h1>{self.question_id}. {self.title} </h1>
                        <h1>Difficulty : {difficulty}</h1>'''
        html_str += f'''{link}'''
        html_str += str(content)
        
        # Get starting code
        for ele in x['data']['question']['codeSnippets']:
            if ele['langSlug'] == DEFAULT_LANGUAGE_SLUG:
                self.starting_code = ele['code']
        
        return html_str
    
    def create_html_file(self):
        if not os.path.exists(f'''{self.title}'''):
            os.mkdir(f'''{self.title}''') 

        # Create HTML file
        with open(f'''{self.title}/{self.question_id}_{self.slug}.html''', 'w') as file:
            file.write(self.html_str)
            
    def create_pdf_file(self):
        pdfkit.from_file(f'''{self.title}/{self.question_id}_{self.slug}.html''', f'''{self.title}/{self.question_id}_{self.slug}.pdf''')

    def create_starter_code_file(self):
        with open(f'''{self.title}/{self.question_id}_{self.slug}.{DEFAULT_LANGUAGE_EXTENSION}''', 'w') as file:
            file.write(self.starting_code)