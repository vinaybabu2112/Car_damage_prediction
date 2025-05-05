import streamlit as st
from model_helper import predict

st.set_page_config(page_title="Vehicle Damage Detection", page_icon="🚗")

st.title("Vehicle Damage Detection")

uploaded_file = st.file_uploader('Upload the file', type=['jpg', 'png'])

if uploaded_file is not None:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded File")
        st.write("Classifying...")
        # Call the predict function from model_helper.py
        prediction = predict(image_path)
        # Display the prediction result
        st.info(f"Predicted Class: {prediction}")
        # Optionally, you can delete the temporary file after processing
        # os.remove(image_path)  # Uncomment if you want to delete the temp file after processing
            
        
else:
    st.write("Please upload an image file.")
