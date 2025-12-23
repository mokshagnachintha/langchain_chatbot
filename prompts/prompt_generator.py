from langchain_core.prompts import PromptTemplate

temp = PromptTemplate(
    input_variables=['paper', 'style', 'length'],
    template='give a {length} {style} of the research paper titled {paper}',
    validate_template=True
)

paper_input = "Attention is all you need"
style_input = "summary"
length_input = "short"

prompt = temp.invoke({
    'paper': paper_input,
    'style': style_input,
    'length': length_input
})

print(f"Generated prompt: {prompt}")
temp.save('prompts/prompt_template.json')
