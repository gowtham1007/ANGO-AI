import requests

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "ROSE FLOWER ",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.show()
import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    # Add a text input widget
    name = st.text_input("ango ai/app.py, "")

    # Add a button widget
    button_clicked = st.button("Click me!")

    # Display a message based on whether the button is clicked or not
    if button_clicked:
        st.write(f"Hello, {name}! You clicked the button.")
    else:
        st.write("Please click the button.")

if __name__ == "__main__":
    main()
