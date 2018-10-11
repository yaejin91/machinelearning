import numpy as np

#P(A|B) = P(B|A) * P(A) / P(B)
p_disease = 1.0/100000.0
p_no_disease = 1.0 - p_disease

p_positive_given_disease = 0.99
p_false = 1 - p_positive_given_disease

p_positive = (p_positive_given_disease * p_disease) + (p_no_disease * p_false)

p_disease_given_positive = p_positive_given_disease*p_disease/p_positive

print(p_disease_given_positive)