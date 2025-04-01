
from llms import stream_claude,stream_gpt
import gradio as gr
from config import pi




custom_css = """
body {
    background-color: #1e1e1e;
    color: #ffffff;
}

.gr-button {
    background-color: #228B22 !important;  /* Forest green */
    color: white !important;
    border: none !important;
}

textarea, input, select {
    background-color: #2e2e2e !important;
    color: white !important;
    border: 1px solid #444 !important;
}
"""


def optimize(python,model):
    if model == 'GPT':
        result = stream_gpt(python)
    elif model == "Claude":
        result = stream_claude(python)
    else:
        raise ValueError("Unknown Model")
    for chunk in result:
        yield chunk

with gr.Blocks(css = custom_css) as ui:

    gr.Markdown('## 🌿 Codaptor')
    with gr.Row():
        python = gr.Textbox(label = 'Python Code:', lines=10, value=pi)
        cpp = gr.Textbox('C++ Code', lines=10)


    with gr.Row():
        model = gr.Dropdown(['GPT','Claude'],label='Select Model',value='GPT')
        convert = gr.Button('Convert Code')


    convert.click(optimize,inputs=[python,model],outputs=[cpp])
    
ui.launch(inbrowser=True)