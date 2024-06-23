import os
import requests
from typing import List, Dict, Any
from openai import OpenAI


class Factory:
    def __init__(self, instructions_general: str, instructions_1: str, instructions_2: str) -> None:
        self.API_KEY = os.getenv('API_KEY')
        self.client = OpenAI(api_key=self.API_KEY)
        self.instructions_general = instructions_general
        self.instructions_1 = instructions_1
        self.instructions_2 = instructions_2

    def create_agent(self):
        agent = Agent(api_key=self.API_KEY)
        return agent
    
    def observe_agent_conversation(self, num_messages: int):
        # Create agents
        self.agent_1 = self.create_agent()
        self.agent_2 = self.create_agent()
        # Add instructions
        self.agent_1.add_message(role="system", text=self.instructions_general)
        self.agent_2.add_message(role="system", text=self.instructions_general)
        print(f"TO BOTH AGENTS:\n{self.instructions_general}\n")
        # Start them off with who they are: agent-specific instructions
        self.agent_1.add_message(role="user", text=self.instructions_1)
        print(f"TO AGENT 1:\n{self.instructions_1}\n")
        self.agent_2.add_message(role="user", text=self.instructions_2)
        print(f"TO AGENT 2:\n{self.instructions_2}\n")
        # Start talking
        for _ in range(num_messages):
            self.talk()

    def talk(self):
        msg_str_1 = self.agent_1.respond()
        print(f"AGENT 1:\n{msg_str_1}\n")
        self.agent_1.add_message(role="assistant", text=msg_str_1)
        self.agent_2.add_message(role="user", text=msg_str_1)
        msg_str_2 = self.agent_2.respond()
        print(f"AGENT 2: {msg_str_2}\n")
        self.agent_2.add_message(role="assistant", text=msg_str_2)
        self.agent_1.add_message(role="user", text=msg_str_2)


class Agent(Factory):
    def __init__(self, api_key) -> None:
        self.API_KEY = api_key
        self.message_history = []

    def add_message(self, role: str, text: str) -> None:
        """Adds message (a dictionary object) for given text to the message history."""
        message = {
            "role": role,
            "content": [
                {
                    "type": "text",
                    "text": text
                }
            ]
        }
        self.message_history.append(message)

    def respond(self) -> str | None:
        """Have GPT respond to a list of messages."""
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.API_KEY}"}
        # Prepare the payload
        payload = {
            "model": "gpt-4o",
            "messages": self.message_history,
            "temperature": 0.1,
            "max_tokens": 4096
        }
        # Send the request to the API
        response = requests.post(
            "https://api.openai.com/v1/chat/completions", 
            headers=headers, 
            json=payload
        )
        if response.status_code == 200:
            response_data = response.json()
            if 'choices' in response_data and response_data['choices']:
                return response_data['choices'][0]['message']['content']
            else:
                return None
        else:
            return None