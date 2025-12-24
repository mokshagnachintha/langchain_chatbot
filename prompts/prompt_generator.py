from langchain_core.prompts import PromptTemplate
temp=PromptTemplate(
    input_variables=['paper','style','length'],
    template='give a {length} {style} of the research paper titled {paper}',validate_template=True
)

temp.save('prompts/prompt_template.json')
