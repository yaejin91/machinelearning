import numpy as np

#P(spam | enhancement)

a = 'spam'
b = 'enhancement'

p_spam = 0.2
p_notspam = 1 - p_spam
p_enhancement_given_spam = 0.05
p_enhancement_not_spam = 0.001

p_enhancement = p_enhancement_given_spam * p_spam + p_enhancement_not_spam * p_notspam

p_spam_enhancement = p_enhancement_given_spam * p_spam / p_enhancement

print(p_spam_enhancement)