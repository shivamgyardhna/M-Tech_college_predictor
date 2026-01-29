# 🎓 GATE College Predictor | CCMT Program Finder

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![License](https://img.shields.io/badge/License-MIT-green)


A **Streamlit-based web application** designed to help **GATE aspirants** explore, filter, and shortlist **CCMT counselling programs** across multiple years based on **GATE score, category, institute type, and program preferences**.

The goal of this project is to make large CCMT cutoff tables **easy to analyze, searchable, and student-friendly**.

---

## 👨‍💻 Developed By

**Shivam**  
🔗 Portfolio: https://shivamgyardhna.github.io/Shivam_portfolioo/

---

## 📌 Project Description

CCMT (Centralized Counselling for M.Tech./M.Arch./M.Plan) releases detailed cutoff data every year in tabular form.  
Manually searching through this data is time-consuming and confusing for students.

This project solves that problem by:

- Converting CCMT cutoff data into structured CSV files
- Loading the data into a Streamlit web app
- Providing **interactive filters** to quickly find eligible programs

The app is fast, scalable, and built with future analysis and visualization in mind.

---

## 🎯 Use Cases

- ✅ GATE aspirants checking **eligible colleges**
- ✅ Shortlisting **IIT / NIT / IIIT programs**
- ✅ Filtering **CS / AI / ML / Data Science programs**
- ✅ Checking eligibility based on **GATE score**
- ✅ Year-wise cutoff comparison
- ✅ Academic analysis and decision support

---

## ✨ Features

- 📅 **Year filter** (works like a normal data filter)
- 🏫 **Institute type filter** (IIT / NIT / IIIT)
- 🎓 **PG Program multi-select filter**
- 🤖 **Special program filters**:
  - CS-related programs
  - AI / ML / Data Science programs
- 🏷️ **Category-based filtering**
- 📊 **GATE score eligibility filter**
- ⚡ Fast performance using `@st.cache_data`
- 📄 Clean, interactive tabular output

---

## 🧱 Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **CSV datasets (CCMT Cutoffs)**

---

## 📁 Project Structure

```
Gate_college_predictor/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── Data/
│   ├── ccmt_2021_data.csv
│   ├── ccmt_2022_data.csv
│   ├── ccmt_2023_data.csv
│   ├── ccmt_2024_data.csv
│   └── ccmt_2025_data.csv
```

---

## ▶️ How to Run the Project (Quick Start)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/shivamgyardhna/M-Tech_college_predictor.git
```

### 2️⃣ Create and activate virtual environment (recommended)

```bash
python -m venv env
env\Scripts\activate      # Windows
# source env/bin/activate # Linux / Mac
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

### 5️⃣ Open in browser

```
http://localhost:8501
```

---

## 📊 Data Source

- **CCMT Official Website**  
  https://admissions.nic.in/CCMT/

> ℹ️ Data is collected from official CCMT records and stored in CSV format for analysis purposes only.

---

## 🔮 Future Enhancements

- 📈 Year-wise cutoff trend graphs
- 🔀 Multi-year comparison
- 🏫 Institute-wise analytics
- 🤖 Smart recommendation system
- 🌐 Public deployment on Streamlit Cloud


---

## 🤝 Contributing

Contributions are welcome and appreciated!

If you would like to improve this project:

- 🐞 Report bugs or issues
- ✨ Suggest new features
- 🧹 Improve code quality or documentation

### How to Contribute

1. Fork the repository
2. Create a new branch (`feature/your-feature-name`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

Please ensure your code follows clean coding practices and is well-documented.
