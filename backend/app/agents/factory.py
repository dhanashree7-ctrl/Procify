import os
from anthropic import Anthropic
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AgentFactory:
    def __init__(self):
        self.anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_claude_response(self, prompt: str, system_prompt: str = ""):
        message = self.anthropic_client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            system=system_prompt,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text

    def get_openai_response(self, prompt: str, system_prompt: str = ""):
        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

factory = AgentFactory()
