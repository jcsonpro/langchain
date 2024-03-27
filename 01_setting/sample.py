
# 언어모델을 호출할 때 입력되는 텍스트를 '프롬프트' 라고 함
# 랭체인을 사용하지 않고 언어 모델을 호출하는 로직


import json
import openai  #← OpenAI에서 제공하는 Python 패키지 가져오기

response = openai.ChatCompletion.create(  #←OpenAI API를 호출하여 언어 모델을 호출합니다.
    model="gpt-3.5-turbo",  #← 호출할 언어 모델의 이름
    messages=[
        {
            "role": "user",
            "content": "감자탕의 감자는 뭐야?"  #←입력할 문장(프롬프트)
        },
    ],
    max_tokens = 100,
    temperature = 1,
    n = 2,
)

print(json.dumps(response, indent=2, ensure_ascii=False))
