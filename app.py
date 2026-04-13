import streamlit as st

st.title("Tabla de multiplicar")

n = st.number_input(
    "Vamos a multiplicar, dame un número entero mayor que 0:",
    min_value=1,
    step=1
)

if st.button("Generar tabla"):
    suma = 0
    for i in range(1, 11):
        resultado = int(n) * i
        st.write(f"{int(n)} * {i} = {resultado}")
        suma += resultado

    st.write(f"Suma acumulada de las tablas: {suma}")
