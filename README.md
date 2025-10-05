
# 🚗 Car Damage Prediction with Deep Learning

A computer vision project that classifies car damage severity using images. Built with transfer learning and deployed using a Streamlit interface for real-time predictions. Useful for automating insurance claims processing and damage assessment.

---

## 1. 🧠 Objective

- Use deep learning (e.g., CNN + ResNet50/ResNet18) to classify vehicle damage into categories like *Minor*, *Moderate*, *Severe*, or *No Damage*.
- Automate vehicle inspection workflows for insurers, repair shops, and used car marketplaces.

---

## 2. 🚧 Dataset & Inputs

- **Sources**: Custom-labeled dataset or publicly available Kaggle/car damage datasets (adjust based on your repo)
- **Total Images**: Approx. 1,000–3,000 images across damage categories
- **Classes**:
  - No Damage
  - Front Crushed
  - Rear Crushed
  - Front Breakage
  - Rear Breakage

---

## 3. 🧩 Project Structure



Car\_damage\_prediction/
├── data/                   # Raw and processed image folders and labels
├── notebooks/              # Training notebooks (e.g. transfer learning fine-tuning)
├── models/                 # Saved model weights (e.g. .pth or .h5)
├── app.py                  # Streamlit app for demo / prediction
├── predict.py              # Script for batch or CLI predictions
├── requirements.txt
├── README.md
└── LICENSE

````

---

## 4. 🧪 Model Development Workflow

1. Preprocess images: normalization, resizing
2. Train CNN with **Transfer Learning** (ResNet50 or similar)
3. Fine-tune model with hyperparameter tuning (e.g. learning rate, optimizers)
4. Evaluate performance on a validation/test set

---

## 5. 📈 Evaluation Metrics

- **Accuracy**: Overall classification accuracy across classes  
- **Confusion Matrix**: Detailed breakdown of prediction performance  
- **Precision / Recall / F1-Score** for each damage category  

> Example results: ~80–90% validation accuracy; good precision/recall across all classes.

---

## 6. 🚀 How to Run

### Install dependencies

```bash
git clone https://github.com/vinaybabu2112/Car_damage_prediction.git
cd Car_damage_prediction
pip install -r requirements.txt
````

### Launch prediction app

```bash
python app.py
```

Access on `http://localhost:8501` — upload an image and get instant classification results.

### Command-line prediction (batch mode)

```bash
python predict.py --input path/to/image.jpg
```

---

## 7. 🖼️ Example

| Upload Image             | Prediction & Confidence |
| ------------------------ | ----------------------- |
| car\_damage\_example.jpg | **Rear Crushed** (85%)  |

*(Add real screenshots in `/images` directory to support this.)*

---

## 8. 🔧 Technologies Used

* **Python**
* **PyTorch** (or TensorFlow/Keras if applicable)
* **Streamlit** for demo UI
* **pandas**, **numpy**, **opencv-python** for preprocessing
* **scikit-learn** for metrics and evaluation support

---

## 9. 🚀 Future Enhancements

* Deploy as an API using **FastAPI** / **Flask**
* Improve performance using **Optuna** or **GridSearchCV**
* Add **SHAP/LIME** explainability for model interpretations
* Augment training with additional damage-specific datasets

---

## 10. 📝 License

This project is licensed under the **MIT License**. Check the `LICENSE` file for details.

---

## 11. 💡 Acknowledgments

* Inspired by deep learning tutorials on car damage detection[codebasics.io]
* Transfer learning methods courtesy of Codebasics community and bootcamp projects ([codebasics.io])

---

## 12. ✍️ Author

**Vinay Babu Muttireddy**
🔗 [GitHub](https://github.com/vinaybabu2112)
📧 Vinaybabu2112@gmail.com



> 🌟 Feel free to fork or star this repository, and drop me a message for collaboration or feedback!
