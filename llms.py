from config import OPENAI_MODEL,CLAUDE_MODEL, system_message
from utills import user_prompt_for,messages_for, write_output
from openai import OpenAI
from anthropic import Anthropic



openai = OpenAI()
claude = Anthropic()


def optimized_gpt(python):
    stream = openai.chat.completions.create(
        model = OPENAI_MODEL,
        messages=messages_for(python),
        stream = True
    )
    reply = ""
    for chunk in stream:
        fragment = chunk.choices[0].delta.content or ""
        reply += fragment
        print(fragment, end="",flush=True)
    write_output(reply)



