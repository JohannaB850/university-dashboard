import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Instalar dependencias necesarias
os.system('pip install streamlit pyngrok matplotlib pandas')
from pyngrok import ngrok

# Cargar datos
file_path = "university_student_dashboard_data.csv"
df = pd.read_csv(file_path)

# Iniciar Streamlit App
def run():
    st.title("University Admissions & Student Satisfaction Dashboard")

    # Metrics
    st.header("Key Metrics")
    st.metric("Total Applications", df["Applications"].sum())
    st.metric("Total Admissions", df["Admitted"].sum())
    st.metric("Total Enrollments", df["Enrolled"].sum())

    # Retention Rate Over Time
    st.header("Retention Rate Trends")
    fig, ax = plt.subplots()
    df.groupby("Year")["Retention Rate (%)"].mean().plot(marker='o', ax=ax)
    ax.set_ylabel("Retention Rate (%)")
    ax.set_xlabel("Year")
    ax.set_title("Retention Rate Over the Years")
    st.pyplot(fig)

    # Student Satisfaction Over Time
    st.header("Student Satisfaction Trends")
    fig, ax = plt.subplots()
    df.groupby("Year")["Student Satisfaction (%)"].mean().plot(marker='o', ax=ax)
    ax.set_ylabel("Satisfaction (%)")
    ax.set_xlabel("Year")
    ax.set_title("Student Satisfaction Over the Years")
    st.pyplot(fig)

    # Enrollment Breakdown by Department
    st.header("Enrollment Breakdown by Department")
    department_data = df[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum()
    fig, ax = plt.subplots()
    department_data.plot(kind="bar", ax=ax)
    ax.set_ylabel("Total Enrollments")
    ax.set_xlabel("Department")
    ax.set_title("Total Enrollments by Department")
    st.pyplot(fig)

    # Comparison of Spring vs. Fall Trends
    st.header("Spring vs. Fall Enrollment Trends")
    term_data = df.groupby("Term")["Enrolled"].sum()
    fig, ax = plt.subplots()
    term_data.plot(kind="bar", ax=ax)
    ax.set_ylabel("Total Enrollments")
    ax.set_xlabel("Term")
    ax.set_title("Spring vs. Fall Enrollment Trends")
    st.pyplot(fig)

    # Comparison of Departments over the Years
    st.header("Department Trends Over the Years")
    fig, ax = plt.subplots()
    df.groupby("Year")[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum().plot(ax=ax)
    ax.set_ylabel("Total Enrollments")
    ax.set_xlabel("Year")
    ax.set_title("Enrollment Trends by Department Over Time")
    st.pyplot(fig)

# Abrir un túnel con ngrok para ejecutar el dashboard
def start_ngrok():
    public_url = ngrok.connect(8501)
    print(f"Access the Streamlit dashboard here: {public_url}")

# Ejecutar Streamlit y abrir el túnel
if __name__ == "__main__":
    start_ngrok()
    os.system('streamlit run app.py')
