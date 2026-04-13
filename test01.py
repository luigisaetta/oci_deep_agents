"""
Test01: Test the connection to OCI OpenAI and generate a response from the model.
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OCI_API_KEY = os.getenv("OCI_API_KEY")
OCI_BASE_URL = os.getenv("OCI_BASE_URL")
MODEL_ID = os.getenv("OCI_MODEL_NAME")
PROJECT_ID = os.getenv("OCI_PROJECT_ID")

default_headers = {"OpenAI-Project": PROJECT_ID}

llm = ChatOpenAI(
            model=MODEL_ID,
            openai_api_base=OCI_BASE_URL,
            openai_api_key=OCI_API_KEY,
            temperature=0.0,
            # important: force responses API (not completions)
            use_responses_api=True,
            output_version="responses/v1",
            # add project id to the request
            default_headers=default_headers,
        )

question = "Tell me something about Rome, Italy"
response = llm.invoke(question)

print("Question: ", question)
print("")
print("Response:")
print(response.content[0]["text"])
print("")

