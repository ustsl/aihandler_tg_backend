def start_message(user: str, balance: str):
    msg = f"""
    Hello {user}

<b>Welcome to IMVO AI</b> 

Create prompts and use them through a chatbot or via an API link. 
Earn money from your prompts or complete your own tasks. 

<b>How to get started</b> 

Use the Interface button in the menu to create your first prompt, or select someone else’s prompt from those available in the public domain. 

The chatbot works within the prompt you choose.  More information on the links in the menu.

<b>Your current balance is ${balance}</b>.
    """
    return msg


def about_message():
    msg = f"""
<b>IMVO.</b> AI provider in Telegram with flexible configuration options for prompts and payment in cryptocurrency for actual use.

<b>Create prompts</b> in a convenient interface, select appropriate models and the size of the memory window of past messages to fine-tune the bot.

<b>Use AI inside telegram.</b>

<b>Share the IDs</b> of your prompts and earn money from other people using them.

<b>Use cryptocurrency</b> to pay for the service. No restrictions.
    """
    return msg
