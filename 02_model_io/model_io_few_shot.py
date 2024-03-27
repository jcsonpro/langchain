from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {
        "input": "충청도의 계룡산 전라도의 내장산 강원도의 설악산은 모두 국립공원이다",
        "output": "충청도의 계룡산, 전라도의 내장산, 강원도의 설악산은 모두 국립공원이다"
    }
]

prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="입력: {input}\n출력: {output}",
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,      # 프롬프트에 사용할 예시를 목록 형식으로 전달
    example_prompt=prompt,  # 예제를 삽입할 서식을 설정하며, PromptTemplate을 전달해야 한다
    prefix="아래 문장부호가 빠진 입력에 문장부호를 추가하세요. 추가할 수 있는 문장부호는 ',', '.'입니다. 다른 문장부호는 추가하지 마세요",
    suffix="입력: {input_string}\n",
    input_variables=["input_string"],
)

llm = OpenAI(model="gpt-3.5-turbo-instruct") 
# 책에 있는데로 실행하면 에러 발생
# OpenAI()는 default 모델이 text-davinci-003 인듯, deprecated 되었기 때문에 gpt-3.5-turbo-instruct 모델을 지정하면 동작함 
# openai.error.InvalidRequestError: The model `text-davinci-003` has been deprecated, learn more here: https://platform.openai.com/docs/deprecations
# SHUTDOWN DATE	LEGACY MODEL	  LEGACY MODEL PRICE	RECOMMENDED REPLACEMENT
# 2024-01-04	text-davinci-003	$0.0200 / 1K tokens	gpt-3.5-turbo-instruct

formatted_prompt = few_shot_prompt.format(
    input_string="집을 보러 가면 그 집이 내가 원하는 조건에 맞는지 살기에 편한지 망가진 곳은 없는지 학인해야 한다 "
)

result = llm.predict(formatted_prompt)
print("formatted_prompt: ", formatted_prompt)
print(result)