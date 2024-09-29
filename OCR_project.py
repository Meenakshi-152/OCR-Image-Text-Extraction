#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install gradio')
get_ipython().system('pip install trasformers')


# In[2]:


import gradio as gr
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from PIL import Image
import torch
import re


# In[3]:


# Load the model and processor
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct", torch_dtype="auto", device_map={"": "cpu"}
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")


# In[4]:


def ocr_image_text_extraction(image):
    try:
        # OCR processing for text extraction
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image},
                    {"type": "text", "text": "Extract the text from this image."},
                ],
            }
        ]

        # Prepare input for the model
        text_input = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = processor(images=image, text=[text_input], padding=True, return_tensors="pt")
        inputs = inputs.to("cpu")

        # Generate text using the model
        generated_ids = model.generate(**inputs, max_new_tokens=128)
        extracted_text = processor.batch_decode(generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

        return extracted_text
    except Exception as e:
        return f"Error: {e}"


# In[5]:


def keyword_search(extracted_text, search_query):
    try:
        # Check if the search query is in the extracted text
        if re.search(search_query, extracted_text, re.IGNORECASE):
            highlighted_text = re.sub(search_query, f"**{search_query}**", extracted_text, flags=re.IGNORECASE)
            return highlighted_text
        else:
            return "No matching text found."
    except Exception as e:
        return f"Error: {e}"


# In[6]:


demo = gr.Interface(
    fn=ocr_image_text_extraction,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Extracted Text"),
    title="OCR Image Text Extraction",
    description="Extract text from an image using OCR",
)


# In[7]:


demo2 = gr.Interface(
    fn=keyword_search,
    inputs=["text", "text"],
    outputs=gr.Textbox(label="Matching Text"),
    title="Keyword Search",
    description="Search for keywords within the extracted text",
)


# In[8]:


demo.launch(share=True)
demo2.launch(share=True)


# In[ ]:




