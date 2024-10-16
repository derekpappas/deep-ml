import math

def softmax(scores: list[float]) -> list[float]:
  exp_scores = [math.exp(score) for score in scores]
  sum_exp_scores = sum(exp_scores)
  softmax_scores = [exp_score / sum_exp_scores for exp_score in exp_scores]
  softmax_scores = [round(softmax_score, 4) for softmax_score in softmax_scores]
  return softmax_scores

print(softmax([1, 2, 3]))

print(softmax([1, 1, 1]))

print(softmax([-1, 0, 5]))
