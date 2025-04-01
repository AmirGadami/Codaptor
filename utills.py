
from config import system_message


def user_prompt_for(python):
    user_prompt = "Rewrite this Python code in C++ with the fastest possible implementation that produces identical output in the least time. "
    user_prompt += "Respond only with C++ code; do not explain your work other than a few comments. "
    user_prompt += "Pay attention to number types to ensure no int overflows. Remember to #include all necessary C++ packages such as iomanip.\n\n"
    user_prompt += python
    return user_prompt


def messages_for(python):
    return [
        {'role':'system','content':system_message},
        {'role':'user', 'content':user_prompt_for(python)}
    ]


def write_output(cpp):
    code = cpp.replace("```cpp","").replace("```","")
    with open('optimized.cpp','w') as f:
        f.write(code)