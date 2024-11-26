import numpy as np
import plotly.graph_objects as go


# Parametros
k = 0.2463
theta = 60.227
N = 100

# Generar vector x de N realizaciones independientes de una distribucion gamma
x = np.random.gamma(shape=k, scale=theta, size=N)

# Calcular estimadores
m_x = np.mean(x)
V_x = np.var(x)

# Valores teoricos
m_x_teorico = k * theta
V_x_teorico = k * (theta**2)

print(f"Estimador m_x: {m_x}")
print(f"Valor teorico m_x: {m_x_teorico}")
print(f"Estimador V_x: {V_x}")
print(f"Valor teorico V_x: {V_x_teorico}")

# Graficar resultados
fig1 = go.Figure()

fig1.add_trace(go.Scatter(y=x, mode="lines+markers", name="Numeros Aleatorios Gamma"))

fig1.update_layout(
    title="A1: Gamma-Distributed Random Values",
    xaxis_title="N",
    yaxis_title="Gamma Distribution Values",
    template="plotly_dark",
)

fig1.show()

# ACTIVIDAD 2

# Calcular la cota de Cramer-Rao para m_x
N_values = np.arange(1, 101)
CRB_m = (theta**2 * k) / N_values

# Graficar resultados
fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=N_values, y=CRB_m, mode="lines+markers", name="CRB(m)"))

fig2.update_layout(
    title="A2: Cramer-Rao Bound For m Parameter",
    xaxis_title="N",
    yaxis_title="CRB(m)",
    yaxis_type="log",  # Escala logaritmica en el eje y
    template="plotly_dark",
)

fig2.show()


# ACTIVIDAD 3

# Parametros
R = 1000

# Inicializar listas para almacenar resultados
var_m = []
ecm_m = []

# Metodo de Montecarlo
for N in N_values:
    m_ML_vector = []
    for r in range(R):
        x = np.random.gamma(shape=k, scale=theta, size=N)
        m_ML_sim = np.mean(x)
        m_ML_vector.append(m_ML_sim)

    # Calcular varianza y ECM empiricos
    var = np.var(m_ML_vector)
    ecm = np.mean((np.array(m_ML_vector) - m_x_teorico) ** 2)

    var_m.append(var)
    ecm_m.append(ecm)

# Graficar resultados
fig3 = go.Figure()

fig3.add_trace(
    go.Scatter(x=N_values, y=var_m, mode="lines+markers", name="m Empirical Variance")
)

fig3.add_trace(
    go.Scatter(x=N_values, y=ecm_m, mode="lines+markers", name="m Empirical MSE")
)

fig3.add_trace(go.Scatter(x=N_values, y=CRB_m, mode="lines+markers", name="CRB(m)"))


fig3.update_layout(
    title="A3: Variance and Empirical MSE For m parameter",
    xaxis_title="N",
    yaxis_title="Value",
    yaxis_type="log",  # Escala logaritmica en el eje y
    template="plotly_dark",
)

fig3.show()

# ACTIVIDAD 4

# Calcular la cota de Cramer-Rao para V_x
CRB_V = (4 * k * theta**4) / N_values

# Graficar resultados
fig4 = go.Figure()

fig4.add_trace(go.Scatter(x=N_values, y=CRB_V, mode="lines+markers", name="CRB(V)"))

fig4.update_layout(
    title="A4: Cramer-Rao Bound For V Parameter",
    xaxis_title="N",
    yaxis_title="CRB(V)",
    yaxis_type="log",  # Escala logaritmica en el eje y
    template="plotly_dark",
)

fig4.show()

# ACTIVIDAD 5

# Inicializar listas para almacenar resultados
var_m = []
ecm_m = []
var_V = []
ecm_V = []

m_x_teorico = k * theta
V_x_teorico = k * (theta**2)

# Metodo de Montecarlo
for N in N_values:
    m_ML_vector = []
    V_ML_vector = []
    for r in range(R):
        x = np.random.gamma(shape=k, scale=theta, size=N)
        m_ML_sim = np.mean(x)
        V_ML_sim = np.var(x)
        m_ML_vector.append(m_ML_sim)
        V_ML_vector.append(V_ML_sim)

    # Calcular varianza y ECM empiricos para m
    var_m.append(np.var(m_ML_vector))
    ecm_m.append(np.mean((np.array(m_ML_vector) - m_x_teorico) ** 2))

    # Calcular varianza y ECM empiricos para V
    var_V.append(np.var(V_ML_vector))
    ecm_V.append(np.mean((np.array(V_ML_vector) - V_x_teorico) ** 2))

# Calcular la cota de Cramer-Rao para V_x
CRB_V = (4 * k * theta**4) / N_values

# Graficar resultados
fig5 = go.Figure()

fig5.add_trace(
    go.Scatter(x=N_values, y=var_V, mode="lines+markers", name="V Empirical Variance")
)

fig5.add_trace(
    go.Scatter(x=N_values, y=ecm_V, mode="lines+markers", name="V Empirical MSE")
)

fig5.add_trace(go.Scatter(x=N_values, y=CRB_V, mode="lines+markers", name="CRB(V)"))

fig5.update_layout(
    title="A5: Variance and Empirical MSE For V parameter",
    xaxis_title="N",
    yaxis_title="Value",
    yaxis_type="log",  # Escala logaritmica en el eje y
    template="plotly_dark",
)

fig5.show()

# ACTIVIDAD 6

# Parametros
k = 1
theta = 2
N_values = np.arange(1, 6)
R = 10000

# Inicializar listas para almacenar resultados
var_m = []
ecm_m = []
var_V = []
ecm_V = []
CRB_m = []
CRB_V = []

m_x_teorico = k * theta
V_x_teorico = k * (theta**2)

# Metodo de Montecarlo
for N in N_values:
    m_ML_vector = []
    V_ML_vector = []
    for r in range(R):
        x = np.random.gamma(shape=k, scale=theta, size=N)
        m_ML_sim = np.mean(x)
        V_ML_sim = np.var(x)
        m_ML_vector.append(m_ML_sim)
        V_ML_vector.append(V_ML_sim)

    # Calcular varianza y ECM empiricos para m
    var_m.append(np.var(m_ML_vector))
    ecm_m.append(np.mean((np.array(m_ML_vector) - m_x_teorico) ** 2))

    # Calcular varianza y ECM empiricos para V
    var_V.append(np.var(V_ML_vector))
    ecm_V.append(np.mean((np.array(V_ML_vector) - V_x_teorico) ** 2))

    # Calcular CRB para m y V
    CRB_m.append((theta**2 * k) / N)
    CRB_V.append((4 * k * theta**4) / N)

# Mostrar los resultados
print("Results:")
print("N\tCRB_m\tVar_m\tECM_m\tCRB_V\tVar_V\tECM_V")
for i in range(len(N_values)):
    print(
        f"{N_values[i]}\t{CRB_m[i]:.4f}\t{var_m[i]:.4f}\t{ecm_m[i]:.4f}\t{CRB_V[i]:.4f}\t{var_V[i]:.4f}\t{ecm_V[i]:.4f}"
    )
