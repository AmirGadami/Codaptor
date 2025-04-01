
from llms import stream_claude,stream_gpt
import gradio as gr
from config import pi


custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

body {
    
    color: #1f2937; /* slate-800 */
    font-family: 'Poppins', 'Segoe UI', sans-serif;
    font-size: 30px;
    line-height: 1.7;
    padding: 20px;
}

.gr-button {

    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 22px !important;
    font-size: 17px !important;
    font-weight: 600 !important;
    box-shadow: 0 6px 12px rgba(96, 165, 250, 0.3);
    transition: all 0.25s ease-in-out;
}

.gr-button:hover {
 
    box-shadow: 0 10px 16px rgba(59, 130, 246, 0.3);
    transform: translateY(-2px);
}

textarea, input, select, .gr-textbox, .gr-dropdown, .gr-radio {
    
    
    border: 1px solid #dbeafe !important; /* soft blue-gray */
    border-radius: 10px !important;
    font-size: 16px;
    padding: 14px !important;
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.03);
}

.gr-textbox label, .gr-dropdown label, .gr-radio label {
    font-size: 18px !important;
    font-weight: 600 !important;
    
}

h1, h2, h3, .gr-markdown {
    
    font-weight: 700;
    font-size: 24px;
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

with gr.Blocks(theme=gr.themes.Base(), css=custom_css) as ui:
    gr.Markdown('## 🌟 Codaptor - High Performance Code Converter')

    with gr.Row():
        python = gr.Code(label='🐍 Python Code', lines=10, value=pi,language='python')
        cpp = gr.Code(label='⚙️ C++ Code', language='cpp',lines=10,)

    with gr.Row():
        model = gr.Dropdown(['GPT', 'Claude'], label='💡 Select Model', value='GPT')

    with gr.Row():
        convert = gr.Button('🚀 Convert Code')

    convert.click(optimize, inputs=[python, model], outputs=[cpp])

ui.launch(inbrowser=True)