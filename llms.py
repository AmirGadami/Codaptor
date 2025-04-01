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

def optimized_claude(python):
    result = claude.messages.stream(
        model = CLAUDE_MODEL,
        max_tokens=200,
        system=system_message,
        messages=[{'role':'user','content':user_prompt_for(python)}]
    )
    reply = ""
    with result as stream:
        for text in stream.text_stream:
            reply += text
            print(text,end='', flush=True)
    write_output(reply)


def stream_gpt(python):
    stream = openai.chat.completions.create(model=OPENAI_MODEL, messages=messages_for(python), stream=True)
    reply = ""

    for chunk in stream:
        fragments = chunk.choices[0].delta.content or ""
        reply += fragments
        yield reply.replace('```cpp\n','').replace('```','')

def stream_claude(python):
    result = claude.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=2000,
        system=system_message,
        messages=[{"role": "user", "content": user_prompt_for(python)}],
    )
    reply = ""
    with result as stream:
        for text in stream.text_stream:
            reply += text
            yield reply.replace('```cpp\n','').replace('```','')



if __name__ =="__main__":
    from config import pi

    # exec(pi)
    optimized_claude(pi)
    stream_claude(pi)