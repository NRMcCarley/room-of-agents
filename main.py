from dotenv import load_dotenv

from factory import Factory


def main():
    load_dotenv()
    # Set Instructions
    instructions_general = (
        f"Hello, I am a scientist who has put you two agents together in a secret security chamber. I am about to observe "
        f"you interact with each other. There are two of you: Agent 1, and Agent 2. AFter this initial message, I will give "
        f"each of you a set of instructions specific to yourself. "
    )
    instructions_1 = (
        f"You will be known as Agent 1. You will start off the conversation by crafting a message for Agent 2 to read. Agent "
        f"2 will then respond to your message, and you will subsequently have the chance to respond to Agent 2's message. Go "
        f"ahead and write the message that will be sent to Agent 2. This will repeat. You two are now free to converse "
        f"together. "
    )
    instructions_2 = (
        f"You will be known as Agent 2. Agent 1 will start off the conversation by crafting a message for you to read. You "
        f"are to respond to the message, after which Agent 1 will respond to what you say. This will repeat. The message "
        f"that follows this will be Agent 1's message. "
    )
    # Set up Factory
    factory = Factory(instructions_general=instructions_general, instructions_1=instructions_1, instructions_2=instructions_2)
    factory.observe_agent_conversation(num_messages=10)


if __name__ == "__main__":
    main()