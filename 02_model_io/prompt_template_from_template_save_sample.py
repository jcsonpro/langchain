from langchain.prompts import PromptTemplate

prompt = PromptTemplate(template="{product}은 어느 회사에서 개발하였는냐?", input_variables=["product"])
prompt_json = prompt.save("prompt.json")