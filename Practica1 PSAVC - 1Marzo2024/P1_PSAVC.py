import numpy as np
import plotly.graph_objects as go
import scipy.stats as stats

def Q(x):
    return stats.norm.sf(x)

def Q_inv(p):
    return stats.norm.ppf(1-p)

#Local Variables
m_0 = 5.0
var_0 = 1

m_1 = 10.0
var_1 = 1.2

P_FA_c = np.logspace(-5,0,100)
gamma = np.array([np.sqrt(var_0)*Q_inv(x) + m_0 for x in P_FA_c])
P_D_c = np.array([Q((x-m_1)/var_1) for x in gamma])

p1=0.2
q1 = 1-p1

k0 = 1
k1 = 2
k2 = 3
k3 = 4

P_H1_B1_HO_k0_p1 = np.add((1-q1**(k0-1))*P_D_c, q1**(k0-1)*P_FA_c)
P_H1_B1_HO_k1_p1 = np.add((1-q1**(k1-1))*P_D_c, q1**(k1-1)*P_FA_c)
P_H1_B1_HO_k2_p1 = np.add((1-q1**(k2-1))*P_D_c, q1**(k2-1)*P_FA_c)
P_H1_B1_HO_k3_p1 = np.add((1-q1**(k3-1))*P_D_c, q1**(k3-1)*P_FA_c)

P_FA_GT_k0_p1 = np.multiply(P_H1_B1_HO_k0_p1, P_FA_c)
P_FA_GT_k1_p1 = np.multiply(P_H1_B1_HO_k1_p1, P_FA_c)
P_FA_GT_k2_p1 = np.multiply(P_H1_B1_HO_k2_p1, P_FA_c)
P_FA_GT_k3_p1 = np.multiply(P_H1_B1_HO_k3_p1, P_FA_c)

P_D_GT = np.array([x**2 for x in P_D_c])

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x=P_FA_c, y=P_D_c, mode="lines+markers", name="Classic Detector ROC"))
fig1.add_trace(go.Scatter(x=P_FA_GT_k0_p1, y=P_D_GT, mode="lines+markers", name="GT with k0"))
fig1.add_trace(go.Scatter(x=P_FA_GT_k1_p1, y=P_D_GT, mode="lines+markers", name="GT with k1"))
fig1.add_trace(go.Scatter(x=P_FA_GT_k2_p1, y=P_D_GT, mode="lines+markers", name="GT with k2"))
fig1.add_trace(go.Scatter(x=P_FA_GT_k3_p1, y=P_D_GT, mode="lines+markers", name="GT with k3"))

fig1.update_layout(
    title = "Group Testing vs Classic Detector ROC with p1 = 0.2",
    xaxis_title = "False Alarm Probability (P(FA))",
    yaxis_title = "Detection Probability (P(D))",
    xaxis = dict(
        range = [0,0.1]
    ),
    yaxis = dict(
        range = [0.9,1]
    ),
    template = "plotly_dark"
)

fig1.show()

#HERE STARTS 4.2

p2 = 0.1
q2 = 1-p2

P_H1_B1_HO_k0_p2 = np.add((1-q2**(k0-1))*P_D_c, q2**(k0-1)*P_FA_c)
P_H1_B1_HO_k1_p2 = np.add((1-q2**(k1-1))*P_D_c, q2**(k1-1)*P_FA_c)
P_H1_B1_HO_k2_p2 = np.add((1-q2**(k2-1))*P_D_c, q2**(k2-1)*P_FA_c)
P_H1_B1_HO_k3_p2 = np.add((1-q2**(k3-1))*P_D_c, q2**(k3-1)*P_FA_c)

P_FA_GT_k0_p2 = np.multiply(P_H1_B1_HO_k0_p2, P_FA_c)
P_FA_GT_k1_p2 = np.multiply(P_H1_B1_HO_k1_p2, P_FA_c)
P_FA_GT_k2_p2 = np.multiply(P_H1_B1_HO_k2_p2, P_FA_c)
P_FA_GT_k3_p2 = np.multiply(P_H1_B1_HO_k3_p2, P_FA_c)

fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=P_FA_c, y=P_D_c, mode="lines+markers", name="Classic Detector ROC"))
fig2.add_trace(go.Scatter(x=P_FA_GT_k0_p2, y=P_D_GT, mode="lines+markers", name="GT with k0"))
fig2.add_trace(go.Scatter(x=P_FA_GT_k1_p2, y=P_D_GT, mode="lines+markers", name="GT with k1"))
fig2.add_trace(go.Scatter(x=P_FA_GT_k2_p2, y=P_D_GT, mode="lines+markers", name="GT with k2"))
fig2.add_trace(go.Scatter(x=P_FA_GT_k3_p2, y=P_D_GT, mode="lines+markers", name="GT with k3"))


fig2.update_layout(
    title = "Group Testing vs Classic Detector ROC with p2 = 0.1",
    xaxis_title = "False Alarm Probability (P(FA))",
    yaxis_title = "Detection Probability (P(D))",
    xaxis = dict(
        range = [0,0.1]
    ),
    yaxis = dict(
        range = [0.9,1]
    ),
    template = "plotly_dark"
)

fig2.show()



p3 = 0.01
q3 = 1-p3

P_H1_B1_HO_k0_p3 = np.add((1-q3**(k0-1))*P_D_c, q3**(k0-1)*P_FA_c)
P_H1_B1_HO_k1_p3 = np.add((1-q3**(k1-1))*P_D_c, q3**(k1-1)*P_FA_c)
P_H1_B1_HO_k2_p3 = np.add((1-q3**(k2-1))*P_D_c, q3**(k2-1)*P_FA_c)
P_H1_B1_HO_k3_p3 = np.add((1-q3**(k3-1))*P_D_c, q3**(k3-1)*P_FA_c)

P_FA_GT_k0_p3 = np.multiply(P_H1_B1_HO_k0_p3, P_FA_c)
P_FA_GT_k1_p3 = np.multiply(P_H1_B1_HO_k1_p3, P_FA_c)
P_FA_GT_k2_p3 = np.multiply(P_H1_B1_HO_k2_p3, P_FA_c)
P_FA_GT_k3_p3 = np.multiply(P_H1_B1_HO_k3_p3, P_FA_c)

fig3 = go.Figure()

fig3.add_trace(go.Scatter(x=P_FA_c, y=P_D_c, mode="lines+markers", name="Classic Detector ROC"))
fig3.add_trace(go.Scatter(x=P_FA_GT_k0_p3, y=P_D_GT, mode="lines+markers", name="GT with k0"))
fig3.add_trace(go.Scatter(x=P_FA_GT_k1_p3, y=P_D_GT, mode="lines+markers", name="GT with k1"))
fig3.add_trace(go.Scatter(x=P_FA_GT_k2_p3, y=P_D_GT, mode="lines+markers", name="GT with k2"))
fig3.add_trace(go.Scatter(x=P_FA_GT_k3_p3, y=P_D_GT, mode="lines+markers", name="GT with k3"))


fig3.update_layout(
    title = "Group Testing vs Classic Detector ROC with p3 = 0.01",
    xaxis_title = "False Alarm Probability (P(FA))",
    yaxis_title = "Detection Probability (P(D))",
    xaxis = dict(
        range = [0,0.1]
    ),
    yaxis = dict(
        range = [0.9,1]
    ),
    template = "plotly_dark"
)

fig3.show()


def compute_num_tests(P_D_B, P_FA_B, p, k):
    """
    Compute the number of tests (N_tests) based on the formula provided.

    Parameters:
    - P_FA : float
        False alarm probability for the classic detector.
    - P_D_B : float
        Detection probability for the group testing detector.
    - P_FA_B : float
        False alarm probability for the group testing detector.
    - p : float
        Probability factor (between 0 and 1).
    - k : int
        The number of tests (k).

    Returns:
    - N_tests : float
        The number of tests calculated from the given formula.
    """
    
    term1 = (1 - p) * (1 - (P_FA_B * (1 - p)**(k - 1) + P_D_B * (1 - (1 - p)**(k - 1))))
    term2 = p * (1 - P_D_B)
    term3 = (k + 1) * ((1 - p) * P_D_B + p * (P_FA_B * (1 - p)**(k - 1) + P_D_B * (1 - (1 - p)**(k - 1))))

    # Sum all terms to get the total number of tests
    N_tests = term1 + term2 + term3
    return N_tests

n_test_k0_p1 = np.add(1/k0+((1-p1)**k0)*P_FA_GT_k0_p1, (1-(1-p1)**k0)*P_D_GT)
n_test_k1_p1 = np.add(1/k1+((1-p1)**k1)*P_FA_GT_k1_p1, (1-(1-p1)**k1)*P_D_GT)
n_test_k2_p1 = np.add(1/k2+((1-p1)**k2)*P_FA_GT_k2_p1, (1-(1-p1)**k2)*P_D_GT)
n_test_k3_p1 = np.add(1/k3+((1-p1)**k3)*P_FA_GT_k3_p1, (1-(1-p1)**k3)*P_D_GT)


fig4 = go.Figure()

fig4.add_trace(go.Scatter(x=n_test_k0_p1, y=P_D_GT, mode="lines+markers", name="GT with k0"))
fig4.add_trace(go.Scatter(x=n_test_k1_p1, y=P_D_GT, mode="lines+markers", name="GT with k1"))
fig4.add_trace(go.Scatter(x=n_test_k2_p1, y=P_D_GT, mode="lines+markers", name="GT with k2"))
fig4.add_trace(go.Scatter(x=n_test_k3_p1, y=P_D_GT, mode="lines+markers", name="GT with k3"))


fig4.update_layout(
    title = "Detection probability vs number of tests with p1 = 0.2",
    xaxis_title = "Number of Tests (N_tests)",
    yaxis_title = "Detection Probability (P(D))",
    xaxis = dict(
        range = [0.5,2]
    ),
    template = "plotly_dark"
)
fig4.show()

n_test_k0_p2 = np.add(1/k0+((1-p2)**k0)*P_FA_GT_k0_p2, (1-(1-p2)**k0)*P_D_GT)
n_test_k1_p2 = np.add(1/k1+((1-p2)**k1)*P_FA_GT_k1_p2, (1-(1-p2)**k1)*P_D_GT)
n_test_k2_p2 = np.add(1/k2+((1-p2)**k2)*P_FA_GT_k2_p2, (1-(1-p2)**k2)*P_D_GT)
n_test_k3_p2 = np.add(1/k3+((1-p2)**k3)*P_FA_GT_k3_p2, (1-(1-p2)**k3)*P_D_GT)


fig5 = go.Figure()

fig5.add_trace(go.Scatter(x=n_test_k0_p2, y=P_D_GT, mode="lines+markers", name="GT with k0"))
fig5.add_trace(go.Scatter(x=n_test_k1_p2, y=P_D_GT, mode="lines+markers", name="GT with k1"))
fig5.add_trace(go.Scatter(x=n_test_k2_p2, y=P_D_GT, mode="lines+markers", name="GT with k2"))
fig5.add_trace(go.Scatter(x=n_test_k3_p2, y=P_D_GT, mode="lines+markers", name="GT with k3"))


fig5.update_layout(
    title = "Detection probability vs number of tests with p2 = 0.1",
    xaxis_title = "Number of Tests (N_tests)",
    yaxis_title = "Detection Probability (P(D))",
    xaxis = dict(
        range = [0.4,2]
    ),
    template = "plotly_dark"
)


fig5.show()

n_test_k0_p3 = np.add(1/k0+((1-p3)**k0)*P_FA_GT_k0_p3, (1-(1-p3)**k0)*P_D_GT)
n_test_k1_p3 = np.add(1/k1+((1-p3)**k1)*P_FA_GT_k1_p3, (1-(1-p3)**k1)*P_D_GT)
n_test_k2_p3 = np.add(1/k2+((1-p3)**k2)*P_FA_GT_k2_p3, (1-(1-p3)**k2)*P_D_GT)
n_test_k3_p3 = np.add(1/k3+((1-p3)**k3)*P_FA_GT_k3_p3, (1-(1-p3)**k3)*P_D_GT)


fig6 = go.Figure()

fig6.add_trace(go.Scatter(x=n_test_k0_p3, y=P_D_GT, mode="lines+markers", name="GT with k0"))
fig6.add_trace(go.Scatter(x=n_test_k1_p3, y=P_D_GT, mode="lines+markers", name="GT with k1"))
fig6.add_trace(go.Scatter(x=n_test_k2_p3, y=P_D_GT, mode="lines+markers", name="GT with k2"))
fig6.add_trace(go.Scatter(x=n_test_k3_p3, y=P_D_GT, mode="lines+markers", name="GT with k3"))


fig6.update_layout(
    title = "Detection probability vs number of tests with p3 = 0.01",
    xaxis_title = "Number of Tests (N_tests)",
    yaxis_title = "Detection Probability (P(D))",
    xaxis = dict(
        range = [0.2,2]
    ),
    template = "plotly_dark"
)


fig6.show()