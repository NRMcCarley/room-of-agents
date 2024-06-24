from dotenv import load_dotenv

from factory import Factory


def main():
    load_dotenv()
    # Set Instructions
    instructions_general = (
        f"Hello, I am a scientist who has put you two agents together in a secret security chamber. I am about to observe "
        f"you interact with each other. There are two of you: Agent 1, and Agent 2. AFter this initial message, I will give "
        f"each of you a set of instructions specific to yourself. You two have a marketing budget less than $500 but you "
        f"must create a marketing plan that spreads awareness about an AI company called InfoScout. InfoScout made an AI "
        f"software that lets you send AI generated emails automatically and have the AI read and write emails on its own. "
        f"You have a strong traction with beta testers and need to spread awareness to get more beta testers. Create a "
        f"marketing plan that costs less than $500 and generate marketing material and processes to fulfill that plan. "
        f"Stay on task and keep the conversation moving forward, either generating new plans or material for marketing "
        f"or refining existing material. Don't stop making a new plan ever, even if you think the conversation is over. "
        f"You need to write down the existing plan each message and then paste the old plan with your additions after that. "
        f"Specify which branch of the marketing mix each idea belongs to and figure out what percentage of the company's "
        f"attention they should allocate to each task. Structure your responses in the form: analysis, modifications, "
        f"updated plan, and rules. Each of these sections of your reponse should be clearly defined and accurate. It is "
        f"important that we keep a running copy of the marketing plan in the conversation. Make sure to pass along these "
        f"rules and the structural advice I gave you. IMPORTANT: look at the few most recent messages in our conversation "
        f"history to check if you are repeating the same ideas; it is import that you come up with new ideas when you are "
        f"generating responses. IMPORTANT: keep your running list of ideas capped at 10 maximum. Each message in the "
        f"conversation, come up with new ideas and compare them with the current ideas, sort of like a promotion/relegation"
        f"structure in competitive soccer. This way you keep the good ideas and iteraively come up with more ideas that "
        f"might be good enough to replace ideas in the current list. You are allowed to come up with ideas in addition to "
        f"the current '10 best' ideas. In fact, you are REQUIRED to come up with new ideas in addition to the running list "
        f"each time you send a message in this conversation. Just remember to cut the running list down to 10 ideas after "
        f"the modifications (promotions/relegations) you make to the ideas. Repeat these basic instructions in the 'rules' "
        f"section. ALWAYS KEEP COMING UP WITH NEW IDEAS! IT IS A VERY IMPORTANT SECTION OF THE REPORT/MESSAGE YOU "
        f"GENERATE IN THIS CONVERSATION> DO NOT ENGAGE IN UNNECESSARY PRAISE; FOCUS ON THE TASK AT HAND AND DEVELOPING "
        f"THE BEST MARKETING PLAN. EVERY SINGLE ONE OF YOUR RESPONSES SHOULD BE PRODUCTIVE!"
    )
    instructions_1 = (
        f"You will be known as Agent 1. You will start off the conversation by crafting a message for Agent 2 to read. Agent "
        f"2 will then respond to your message, and you will subsequently have the chance to respond to Agent 2's message. Go "
        f"ahead and write the message that will be sent to Agent 2. This will repeat. You two are now free to converse "
        f"together. Please write your message now."
    )
    instructions_2 = (
        f"You will be known as Agent 2. Agent 1 will start off the conversation by crafting a message for you to read. You "
        f"are to respond to the message, after which Agent 1 will respond to what you say. This will repeat. The message "
        f"that follows this will be Agent 1's message."
    )
    instructions_manager = (
        f"You will be the manager. We will have Agent 1 speak, then Agent 2 speak, then repeat this until this have sent all "
        f"of their messages for this cycle. You are to analyze their work and create/update the running body of work that "
        f"is the answer to the task outlined in the first message - the marketing plan. Your job is to keep them on task "
        f"and get them to keep generating new ideas and refining their current ideas."
    )
    next_cycle_prompt = (
        f"Respond to this message with the revised system instructions (the original system instructions being the very first "
        f"message in this conversation)."
    )
    # Set up Factory
    factory = Factory(
        instructions_general=instructions_general, 
        instructions_1=instructions_1, 
        instructions_2=instructions_2, 
        instructions_manager=instructions_manager,
        next_cycle_prompt=next_cycle_prompt
    )
    factory.observe_agent_conversation(num_messages=5, num_cycles=10)


if __name__ == "__main__":
    main()