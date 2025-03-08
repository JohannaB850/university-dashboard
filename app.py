import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
file_path = "university_student_dashboard_data.csv"
df = pd.read_csv(file_path)

# Título del dashboard
st.title("University Admissions & Student Satisfaction Dashboard")

# 1️⃣ Métricas clave
st.header("Key Metrics")
st.metric("Total Applications", df["Applications"].sum())
st.metric("Total Admissions", df["Admitted"].sum())
st.metric("Total Enrollments", df["Enrolled"].sum())

# Análisis detallado por métrica
st.subheader("Analysis")
st.write("- **Total applications, admissions, and enrollments per term:** The number of applications has been stable, but the conversion rate from applications to enrollments varies per term, indicating potential areas for improving admissions efficiency.")
st.write("- **Retention rate trends over time:** A steady increase in retention rates suggests that student support systems and academic programs are improving, leading to better student retention.")
st.write("- **Student satisfaction scores over the years:** Student satisfaction has shown positive trends, implying improvements in academic and extracurricular experiences. Areas with lower satisfaction should be analyzed for potential interventions.")
st.write("- **Enrollment breakdown by department (Engineering, Business, Arts, Science):** Engineering and Business programs show the highest enrollments, while Arts and Science maintain stable numbers. Strategies to boost interest in less-enrolled programs could be explored.")
st.write("- **Comparison between Spring vs. Fall term trends:** Enrollment remains fairly balanced between Spring and Fall, but minor fluctuations indicate possible seasonal impacts on admissions trends.")
st.write("- **Compare trends between departments, retention rates, and satisfaction levels:** Departments with higher enrollments tend to have higher satisfaction and retention rates, suggesting that well-established programs attract and retain students better. Lower-enrollment programs may require strategic enhancements to improve retention.")

# 2️⃣ Tasa de retención a lo largo del tiempo
st.header("Retention Rate Trends")
fig, ax = plt.subplots()
df.groupby("Year")["Retention Rate (%)"].mean().plot(marker='o', ax=ax)
ax.set_ylabel("Retention Rate (%)")
ax.set_xlabel("Year")
ax.set_title("Retention Rate Over the Years")
st.pyplot(fig)

# 3️⃣ Satisfacción estudiantil a lo largo del tiempo
st.header("Student Satisfaction Trends")
fig, ax = plt.subplots()
df.groupby("Year")["Student Satisfaction (%)"].mean().plot(marker='o', ax=ax)
ax.set_ylabel("Satisfaction (%)")
ax.set_xlabel("Year")
ax.set_title("Student Satisfaction Over the Years")
st.pyplot(fig)

# 4️⃣ Distribución de inscripciones por departamento
st.header("Enrollment Breakdown by Department")
department_data = df[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum()
fig, ax = plt.subplots()
department_data.plot(kind="bar", ax=ax)
ax.set_ylabel("Total Enrollments")
ax.set_xlabel("Department")
ax.set_title("Total Enrollments by Department")
st.pyplot(fig)

# 5️⃣ Comparación entre Spring vs. Fall
st.header("Spring vs. Fall Enrollment Trends")
term_data = df.groupby("Term")["Enrolled"].sum()
fig, ax = plt.subplots()
term_data.plot(kind="bar", ax=ax)
ax.set_ylabel("Total Enrollments")
ax.set_xlabel("Term")
ax.set_title("Spring vs. Fall Enrollment Trends")
st.pyplot(fig)

# 6️⃣ Tendencias de inscripción por departamento a lo largo del tiempo
st.header("Department Trends Over the Years")
fig, ax = plt.subplots()
df.groupby("Year")[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum().plot(ax=ax)
ax.set_ylabel("Total Enrollments")
ax.set_xlabel("Year")
ax.set_title("Enrollment Trends by Department Over Time")
st.pyplot(fig)

# 7️⃣ Hallazgos clave y recomendaciones
st.header("Key Findings and Actionable Insights")
st.write("- **Increasing Retention Rates:** The retention rate has shown a steady increase over the years, indicating improvements in student support and academic programs.")
st.write("- **Student Satisfaction:** Student satisfaction has also been trending upwards, suggesting that the institution is addressing student needs effectively.")
st.write("- **Departmental Trends:** Engineering and Business programs have the highest enrollments, while Arts and Science enrollments remain stable.")
st.write("- **Spring vs. Fall Enrollment:** Enrollment numbers are consistent between terms, with a slight increase in Fall terms.")
st.write("- **Recommendation:** Focus on improving retention strategies for lower-enrollment departments and continue enhancing student experience to sustain satisfaction rates.")

