# 本脚本适用于昇思大模型平台单卡环境部署，对应指导手册中deepseek-r1-distill-qwen-1.5b-gradio.py
from mindnlp.transformers import AutoModelForCausalLM, AutoTokenizer
from mindnlp.transformers import TextIteratorStreamer
from mindnlp.peft import PeftModel
from threading import Thread

# 开启同步，在出现报错，定位问题时开启
# mindspore.set_context(pynative_synchronize=True)

# Loading the tokenizer and model from Modelers's model hub.
tokenizer = AutoTokenizer.from_pretrained("MindSpore-Lab/DeepSeek-R1-Distill-Qwen-1.5B-FP16", mirror="modelers")
# 设置pad_token为eos_token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained("MindSpore-Lab/DeepSeek-R1-Distill-Qwen-1.5B-FP16", mirror="modelers")
# adapter_model path
# model = PeftModel.from_pretrained(model, "./output/DeepSeek-R1-Distill-Qwen-1.5B/adapter_model_for_demo/")

system_prompt = "你是一个智能聊天机器人，以最简单的方式回答用户问题"


def build_input_from_chat_history(chat_history, msg: str):
    messages = [{'role': 'system', 'content': system_prompt}]
    for info in chat_history:
        role, content = info['role'], info['content']
        messages.append({'role': role, 'content': content})
    messages.append({'role': 'user', 'content': msg})
    return messages


def inference(message, history):
    messages = build_input_from_chat_history(history, message)
    input_ids = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="ms",
            tokenize=True
        )
    
    streamer = TextIteratorStreamer(tokenizer, timeout=300, skip_prompt=True, skip_special_tokens=True)
    generate_kwargs = dict(
        input_ids=input_ids,
        streamer=streamer,
        max_new_tokens=1024,
        use_cache=True,
    )
    
    t = Thread(target=model.generate, kwargs=generate_kwargs)
    t.start()  # Starting the generation in a separate thread.
    partial_message = ""
    for new_token in streamer:
        partial_message += new_token
        print(new_token, end="", flush=True)
    
    messages.append({'role': 'assistant', 'content': partial_message})
    return messages[1:]

import os
import platform
os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'
welcome_prompt = '欢迎使用 DeepSeek-R1-Distill-Qwen-1.5B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序'
print(welcome_prompt)
history = []
while True:
    query = input("\n用户：")
    if query.strip() == "stop":
        break
    if query.strip() == "clear":
        os.system(clear_command)
        print(welcome_prompt)
        continue
    print("\nDeepSeek-R1-Distill-Qwen-1.5B：", end="")
    history = inference(query, history)
    print("")
