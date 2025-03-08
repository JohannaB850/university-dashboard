import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
file_path = "university_student_dashboard_data.csv"
df = pd.read_csv(file_path)

# Título del dashboard
st.title("Dashboard de Admisión y Satisfacción Estudiantil")

# 1️⃣ Métricas clave
st.header("Métricas Clave")
st.metric("Total de Aplicaciones", df["Applications"].sum())
st.metric("Total de Admisiones", df["Admitted"].sum())
st.metric("Total de Inscripciones", df["Enrolled"].sum())

# 2️⃣ Tasa de retención a lo largo del tiempo
st.header("Tasa de Retención a lo Largo del Tiempo")
fig, ax = plt.subplots()
df.groupby("Year")["Retention Rate (%)"].mean().plot(marker='o', ax=ax)
ax.set_ylabel("Tasa de Retención (%)")
ax.set_xlabel("Año")
ax.set_title("Tasa de Retención a lo Largo del Tiempo")
st.pyplot(fig)
st.write("- La tasa de retención ha mostrado un aumento constante, lo que indica mejoras en el apoyo académico y la satisfacción estudiantil.")

# 3️⃣ Satisfacción estudiantil a lo largo del tiempo
st.header("Tendencias de Satisfacción Estudiantil")
fig, ax = plt.subplots()
df.groupby("Year")["Student Satisfaction (%)"].mean().plot(marker='o', ax=ax)
ax.set_ylabel("Satisfacción Estudiantil (%)")
ax.set_xlabel("Año")
ax.set_title("Satisfacción Estudiantil a lo Largo del Tiempo")
st.pyplot(fig)
st.write("- La satisfacción estudiantil ha ido en aumento, lo que sugiere que la institución ha implementado estrategias exitosas para mejorar la experiencia de los estudiantes.")

# 4️⃣ Distribución de inscripciones por departamento
st.header("Distribución de Inscripciones por Departamento")
department_data = df[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum()
fig, ax = plt.subplots()
department_data.plot(kind="bar", ax=ax)
ax.set_ylabel("Total de Inscripciones")
ax.set_xlabel("Departamento")
ax.set_title("Distribución de Inscripciones por Departamento")
st.pyplot(fig)
st.write("- Ingeniería y Negocios tienen las inscripciones más altas, mientras que Artes y Ciencias mantienen números estables.")

# 5️⃣ Comparación entre Spring vs. Fall
st.header("Comparación de Inscripciones: Primavera vs. Otoño")
term_data = df.groupby("Term")["Enrolled"].sum()
fig, ax = plt.subplots()
term_data.plot(kind="bar", ax=ax)
ax.set_ylabel("Total de Inscripciones")
ax.set_xlabel("Periodo Académico")
ax.set_title("Comparación de Inscripciones: Primavera vs. Otoño")
st.pyplot(fig)
st.write("- La cantidad de inscripciones es relativamente equilibrada entre Primavera y Otoño, con una ligera tendencia al alza en Otoño.")

# 6️⃣ Tendencias de inscripción por departamento a lo largo del tiempo
st.header("Tendencias de Inscripción por Departamento")
fig, ax = plt.subplots()
df.groupby("Year")[["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]].sum().plot(ax=ax)
ax.set_ylabel("Total de Inscripciones")
ax.set_xlabel("Año")
ax.set_title("Tendencias de Inscripción por Departamento")
st.pyplot(fig)
st.write("- Ingeniería y Negocios han mostrado crecimiento constante, mientras que Artes y Ciencias se han mantenido más estables.")

# 7️⃣ Hallazgos clave y recomendaciones
st.header("Hallazgos Clave y Recomendaciones")
st.write("- **Aumento en la tasa de retención:** Se observa una mejora continua en la retención de estudiantes, lo que sugiere que los programas de apoyo académico están funcionando correctamente.")
st.write("- **Satisfacción estudiantil en aumento:** La tendencia positiva en los niveles de satisfacción indica que los esfuerzos de la institución están dando resultados en la experiencia estudiantil.")
st.write("- **Tendencias por departamento:** Ingeniería y Negocios son las áreas con mayor número de estudiantes inscritos, mientras que Artes y Ciencias mantienen un crecimiento estable.")
st.write("- **Equilibrio entre Primavera y Otoño:** La cantidad de inscripciones es consistente en ambos periodos académicos, con una ligera ventaja en Otoño.")
st.write("- **Recomendación:** Se recomienda fortalecer las estrategias de retención en los programas con menor inscripción y continuar mejorando la experiencia estudiantil para mantener la satisfacción alta.")


