from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    streaming=True,
    callbacks=[
        StreamingStdOutCallbackHandler()
    ]
)

resp = chat([
    HumanMessage(content="맛있는 스테이크 굽는 법을 알려주세요")
])