#P(A)
p_know = 0.6
p_notknow = 1 - p_know

p_notright_given_know = 0.15
p_right_given_notknow = 0.2

#P(B|A)= P(right|know)
p_right_given_know = 1 - p_notright_given_know

#P(B) = P(correct)
p_correct = p_right_given_notknow*p_notknow + p_right_given_know*p_know

#P(A|B) = P(know|right)
p_know_given_right = p_right_given_know*p_know/p_correct

print(p_know_given_right)