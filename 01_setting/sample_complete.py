import json
import openai

response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt="비가 오는 날에는 회를",
    stop=".",
    max_tokens=100,
    n=2,
    temperature=0.5
)

print(json.dumps(response, indent=2, ensure_ascii=False))