from langchain.prompts import PromptTemplate

prompt = PromptTemplate(template="{product}는 어느 회사에서 개발했나요?",
                        input_variables=["product"])
prompt_json = prompt.save("prompt.json")