from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the structure of the Bayesian Network
model = BayesianNetwork([
    ('Cold', 'Cough'),
    ('Flu', 'Cough'),
    ('Cold', 'Fever'),
    ('Flu', 'Fever')
])

# Define the Conditional Probability Tables (CPTs)
cpd_cold = TabularCPD(variable='Cold', variable_card=2, values=[[0.7], [0.3]])
cpd_flu = TabularCPD(variable='Flu', variable_card=2, values=[[0.8], [0.2]])

cpd_cough = TabularCPD(
    variable='Cough', variable_card=2,
    values=[[0.9, 0.6, 0.7, 0.1], [0.1, 0.4, 0.3, 0.9]],
    evidence=['Cold', 'Flu'],
    evidence_card=[2, 2]
)

cpd_fever = TabularCPD(
    variable='Fever', variable_card=2,
    values=[[0.8, 0.5, 0.7, 0.2], [0.2, 0.5, 0.3, 0.8]],
    evidence=['Cold', 'Flu'],
    evidence_card=[2, 2]
)

# Add the CPTs to the model
model.add_cpds(cpd_cold, cpd_flu, cpd_cough, cpd_fever)

# Validate the model
assert model.check_model()

# Perform inference
inference = VariableElimination(model)

# Query: What is the probability of having a Cold given that the person has a Cough?
query_result = inference.query(variables=['Cold'], evidence={'Cough': 1})
print(query_result)

# Query: What is the probability of having a Flu given that the person has a Fever?
query_result = inference.query(variables=['Flu'], evidence={'Fever': 1})
print(query_result)
