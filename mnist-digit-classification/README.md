# 🧠 Handwritten Digit Recognition using Machine Learning (MNIST)

This project builds and optimizes a machine learning model to recognize handwritten digits from the **MNIST dataset** using **Python** and **Scikit-learn**.  
It demonstrates the full machine learning pipeline — from **data preprocessing and model training** to **hyperparameter tuning, evaluation, and visualization**.

---

## 📌 Project Overview
The goal of this project is to develop a classifier that can accurately recognize handwritten digits (0–9).  
By applying **Stochastic Gradient Descent (SGDClassifier)** and **cross-validation**, the model achieves strong performance with:
- **Accuracy:** ~90%
- **ROC-AUC:** ~0.99 (Micro and Weighted)
- **Balanced precision and recall** across all classes

---

## ⚙️ Tech Stack
- **Language:** Python  
- **Libraries:** Scikit-learn, NumPy, Pandas, Matplotlib  
- **Dataset:** MNIST (70,000 grayscale images, 28×28 pixels each)

---

## 🧩 Workflow
1. **Data Preparation** – Load, visualize, and split the MNIST dataset.  
2. **Preprocessing** – Normalize pixel values using `StandardScaler`.  
3. **Model Building** – Train an `SGDClassifier` for multiclass digit recognition.  
4. **Evaluation** – Measure performance using accuracy, precision, recall, F1-score, and ROC-AUC.  
5. **Hyperparameter Tuning** – Optimize model parameters with `RandomizedSearchCV`.  
6. **Visualization** – Plot confusion matrices, ROC curves, and misclassified examples.  

---

## 🧠 Key Results
| Metric | Baseline Model | Tuned Model |
|---------|----------------|--------------|
| Accuracy | 88.7% | **90.1%** |
| Weighted ROC-AUC | 0.986 | **0.989** |
| Micro ROC-AUC | 0.987 | **0.990** |

The tuned model shows improved performance and balanced generalization across all digit classes.

---

## 📊 Visualizations
Below are example visual outputs from the notebook:

| Visualization | Description |
|----------------|-------------|
| 🧾 **Confusion Matrix** | Shows correctly vs. incorrectly predicted digits. |
| 🔍 **Precision–Recall Curve** | Demonstrates the trade-off between false positives and recall. |
| 📈 **ROC Curve** | Confirms high separability across digit classes. |
| 🖼️ **Prediction Samples** | Displays random predictions (green = correct, red = incorrect). |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/mayahalabi/mnist-digit-classification.git
cd mnist-digit-classification
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the notebook
Open `mnist_digit_classification.ipynb` in **Jupyter Notebook** or **Google Colab**,  
then run all cells in order to reproduce the results.
