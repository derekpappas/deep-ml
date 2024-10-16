import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
  l = len(features)
  X = [0] * l
  for i in range(len(features)):
    feature = features[i]
    for j in range(len(feature)):
      X[i] += feature[j] * weights[j]
  XB = [x + bias for x in X]
  
  probabilities = [1 / (1 + math.exp(-x)) for x in XB]
  probabilities = [round(probability, 4) for probability in probabilities]
  mse = sum([(label - probability) ** 2 for label, probability in zip(labels, probabilities)]) / len(labels)
  return probabilities, mse

# features = [[1, 2], [2, 3], [3, 4]]
#
# labels = [0, 1, 1]
#
# weights = [0.1, 0.2]
#
# bias = 0.3
#
# probabilities, mse = single_neuron_model(features, labels, weights, bias)
#
# print(f"probabilities: {probabilities}")
#
# print(f"mse: {mse}")

print( 'Got     : ' + str(single_neuron_model([[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]], [0, 1, 0], [0.7, -0.4], -0.1)))

print(f'Expected: ([0.4626, 0.4134, 0.6682], 0.3349)')

#print(single_neuron_model([[1, 2], [2, 3], [3, 1]], [1, 0, 1], [0.5, -0.2], 0))
