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
