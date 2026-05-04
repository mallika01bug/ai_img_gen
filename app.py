import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import datetime
import os


client=InferenceClient(token=os.getenv("HF_TOKEN"))
MODEL="stabilityai/stable-diffusion-xl-base-1.0"
st.set_page_config(page_title="AI Image Generator", page_icon="🖼️")
st.title("AI IMage Generator")
st.write("Describe your imagination to maake it real...")
prompt=st.text_input("describe your image...")


if st.button("Generate"):
    with st.spinner("AI is creating your image..."):
        image=client.text_to_image(prompt,model=MODEL)
        st.image(image,caption=prompt)
        image.save("image.png")
        st.success("image saved successfully")
