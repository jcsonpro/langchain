import langchain.schema as sc
from langchain.chat_models import ChatOpenAI   # ChatOpenAI클래스 가져오기  OpenAI의 Chat 모델을 호출할 때 사용
# from langchain.schema import HumanMessage      # 사용자의 메시지인 HumanMessage 가져오기
# from langchain.schema import AIMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

result = chat(
    [
        sc.HumanMessage(content="안녕하세요!"),
        sc.AIMessage(content="{ChatModel의 답변인 계란찜 만드는 법}"),
        sc.HumanMessage(content="영어로 번역해줘"),
    ]
)
print(result.content)