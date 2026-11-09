# 🤖 AI-Based Job Role Predictor

An AI-based job role prediction project that predicts suitable job roles based on the skills provided by the user.

## 📌 About the Project

This project was developed as part of the **Honeywell FutureSkills Edge Program**.

The application uses Python and machine learning techniques to process skill-related data and predict suitable job roles.

## 🎯 Project Objective

To explore how machine learning can be used to analyze skills and predict potential job roles, helping users explore career opportunities based on their skill sets.

## 🛠️ Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computations
- **Scikit-learn** – Machine learning and data preprocessing
- **Jupyter Notebook** – Model development and experimentation
- **Streamlit** – Interactive web application

## 📂 Project Structure

- `app.py` – Streamlit application
- `job_predictor.ipynb` – Jupyter Notebook for model development
- `new_skills_dataset.csv` – Dataset used for training
- `job_model.pkl` – Saved trained model
- `vectorizer.pkl` – Saved vectorizer

## ⚙️ How It Works

1. The user enters their skills.
2. The input is processed using the saved vectorizer.
3. The trained machine learning model analyzes the input.
4. The application predicts a suitable job role.

## 🚀 How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/dwanish24cseu034-cloud/AI-Job_Role_Predictor.git
   ```

2. Navigate to the project folder:

   ```bash
   cd AI-Job_Role_Predictor
   ```

3. Install the required libraries:

   ```bash
   pip install pandas numpy scikit-learn streamlit
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## 📊 Project Details

- Dataset size: 1,000 records
- Input features: Skills
- Prediction target: Job Role
- Model development and preprocessing performed using Python.

## 📚 Learning Outcomes

- Hands-on experience with Python and data preprocessing.
- Understanding the basics of machine learning workflows.
- Working with datasets using Pandas and NumPy.
- Building an interactive application using Streamlit.
- Saving and loading trained machine learning models.

---

⭐ If you find this project interesting, feel free to explore the repository!
