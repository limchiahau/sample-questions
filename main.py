import sys
import random
import numpy as np

NUM_QUESTIONS_TO_SAMPLE = 10

def get_num_questions():
    return int(sys.argv[1])

num_questions = get_num_questions()
sample_question = random.sample(list(np.arange(num_questions) + 1), NUM_QUESTIONS_TO_SAMPLE)
sample_question = sorted(sample_question)

print(sample_question)
