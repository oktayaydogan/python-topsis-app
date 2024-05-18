import numpy as np

class TOPSIS:
    def __init__(self, alternatives, criterias, matrix):
        self.alternatives = alternatives
        self.criterias = criterias
        self.matrix = self.convert_matrix(matrix)
        self.matrix = np.array(self.matrix)

        self.squares = {}
        self.sum = {}
        self.ratios = {}
        self.weighted_ratios = {}
        self.ideal_positive = []
        self.ideal_negative = []
        self.euclidean_distances = {}
        self.ranking = []

        print(self.alternatives)
        print(self.criterias)
        print(self.matrix)

    def convert_matrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if isinstance(matrix[i][j], str):
                    matrix[i][j] = 1
        return matrix

    def calculate_squares(self):
        self.squares = np.square(self.matrix)

    def calculate_ratios(self):
        self.sum = np.sqrt(np.sum(self.matrix ** 2, axis=0))
        self.ratios = self.matrix / self.sum

    def calculate_weighted_ratios(self):
        weights = np.array([criteria['weight'] / 100 for criteria in self.criterias])
        self.weighted_ratios = self.ratios * weights

        for criteria_id in range(len(self.criterias)):
            criteria_values = self.weighted_ratios[:, criteria_id]
            self.ideal_positive.append(max(criteria_values))
            self.ideal_negative.append(min(criteria_values))

    def calculate_euclidean_distances(self):
        for alternative_id in range(len(self.alternatives)):
            positive_distance = np.sqrt(np.sum((np.array(self.ideal_positive) - self.weighted_ratios[alternative_id]) ** 2))
            negative_distance = np.sqrt(np.sum((np.array(self.ideal_negative) - self.weighted_ratios[alternative_id]) ** 2))
            self.euclidean_distances[alternative_id] = {
                'name': self.alternatives[alternative_id],
                'values': {
                    'positive': positive_distance,
                    'negative': negative_distance
                }
            }

    def calculate_ranking(self):
        scores = []
        for alternative_id in range(len(self.alternatives)):
            positive_distance = self.euclidean_distances[alternative_id]['values']['positive']
            negative_distance = self.euclidean_distances[alternative_id]['values']['negative']
            score = negative_distance / (positive_distance + negative_distance)
            scores.append({
                'name': self.alternatives[alternative_id],
                'values': {
                    'score': score
                }
            })

        # Sıralamayı skora göre yaparken tersine çevir
        self.ranking = sorted(scores, key=lambda x: x['values']['score'], reverse=True)

    def run_topsis(self):
        self.calculate_squares()
        self.calculate_ratios()
        self.calculate_weighted_ratios()
        self.calculate_euclidean_distances()
        self.calculate_ranking()
        return self.ranking

    def get_all_calculations(self):
        return {
            'squares': self.squares,
            'sum': self.sum,
            'ratios': self.ratios,
            'weighted_ratios': self.weighted_ratios,
            'ideal_positive': self.ideal_positive,
            'ideal_negative': self.ideal_negative,
            'euclidean_distances': self.euclidean_distances,
            'ranking': self.ranking
        }
