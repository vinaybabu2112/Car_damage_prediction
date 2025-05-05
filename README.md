
# 🚗 Car Damage Prediction App

## Overview
This **Car Damage Prediction App** uses a **ResNet-50** deep learning model to classify vehicle damage into six categories. The application is deployed using **Streamlit**, allowing users to upload images and receive real-time predictions.

## Features
- 📷 Upload vehicle images (JPG/PNG format)
- 🔍 Predict car damage using a fine-tuned **ResNet-50** model
- 📊 Display classification results in an intuitive UI
- 🚀 Deployed using **Streamlit** for easy accessibility

## Installation

### Clone the repository:
```sh
git clone https://github.com/your-username/car-damage-prediction.git
cd car-damage-prediction
```

### Install dependencies:
```sh
pip install -r requirements.txt
```

### Run the application:
```sh
streamlit run app.py
```

## Project Structure
```
📂 car-damage-prediction
├── 📂 model
   ├── saved_model.pth     # Trained ResNet-50 model
├── model_helper.py         # Model prediction logic
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

## How It Works
1. The user **uploads an image** of a vehicle.
2. The **pretrained model (ResNet-50)** processes the image.
3. The model predicts the **damage classification** (`Front Breakage, Rear Normal, etc.`).
4. The result is displayed with the **uploaded image** in the Streamlit app.

## Dependencies
- `torch`
- `torchvision`
- `streamlit`
- `PIL`
- `numpy`

## Deployment
The app can be deployed using **Streamlit Cloud**. 

### Deploy via Streamlit Cloud
1. Push your repository to GitHub.
2. Create an account on **Streamlit Community Cloud**.
3. Deploy by linking your repository.


## License
This project is **open-source** under the **MIT License**.

## Authors
- **Dhaval patel**
- Code Basics Team

## Contributors
👩‍💻 **Vinay Muttireddy** – Data Scientist & Developer  
Feel free to contribute! Open an issue or submit a pull request.

---

🚀 **Start predicting vehicle damage now!**
```
