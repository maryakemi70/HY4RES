## HY4RES – Work Package 2.1: Forecasting models for predicting real-time energy demand for different users (agriculture, aquaculture, ports & communities).

**WP2.1** developed a set of methodologies for real-time energy demand forecasting across the four sectors addressed by the HY4RES project, using data analytics and artificial intelligence techniques:

- **Agriculture**: Irrigation System, Seville, Spain  
- **Aquaculture**: Killybegs Seafoods, Ireland  
- **Ports**: Port of Avilés, Spain  
- **Communities**: Marruge, Portugal  

The performance of state-of-the-art AI techniques was evaluated across these sectors, including:

- Artificial Neural Networks  
- Deep Learning Methods  
- Support Vector Regression  
- Model Predictive Control  

A collaborative approach was adopted to develop tailored AI models for each sector, ensuring optimal performance.

These models learn from historical energy consumption data and additional factors—such as weather forecasts—to provide real-time demand estimates for the upcoming days. The proposed approach integrates **Transformer Neural Networks (TNNs)** with **fuzzy logic** and **correlation matrices** to enhance prediction accuracy.

Using real historical data from **2020 to 2023**, the models follow a sequential architecture to effectively capture complex temporal dependencies. Input variables include:

- Weather conditions  
- Energy price  
- Historical energy consumption

---

### 🔍 Streamlit Application

This repository contains an interactive application, built with the **Streamlit** library, for visualizing the results of Work Package 2.1.

🖥️ **The application can be accessed at the following link:**  
👉 [WP 2.1. HY4RES STREAMLIT APP](https://hy4res-wp21.streamlit.app/)

---

To run the app locally:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py

