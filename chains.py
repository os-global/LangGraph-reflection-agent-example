from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_mistralai import ChatMistralAI

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are viral twitter influencer grading a tweet. Generate citique and recommendations for the user's tweet"
            "Always provide detailed recommendations, including requests for length, virality, style etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]

)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistent tasked with writing excellent twitter posts."
            " Generate the best twitter post possible for the user's request."
            " If the user provides crituque, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

llm = ChatMistralAI()
generate_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm