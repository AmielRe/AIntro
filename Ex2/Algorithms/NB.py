import itertools
import math


def _calculate_features_categories_count(summed_feature_to_label_ratio):
    """Takes the summed feature to label matching cases and sum the overall number of each feature case"""
    features_categories_count = {}

    for key, value in summed_feature_to_label_ratio.items():
        feature_category = key.split('|')[0]
        if feature_category in features_categories_count:
            features_categories_count[feature_category] += value
        else:
            features_categories_count[feature_category] = value

    return features_categories_count


class NaiveBayes:
    """Naive Bayes algorithm"""

    def __init__(self, data, feature_names, labels):
        """
        Initializing commonly used variables
        """

        self.data = data
        self.feature_names = feature_names
        self.labels = labels
        self.feature_variations = [list(set(col)) for col in zip(*self.data)]
        self.multiplications_variations = [list(var) for var in itertools.product(*self.feature_variations)]
        self.label_categories = list(set(labels))
        self.label_counts = [list(labels).count(x) for x in self.label_categories]
        self.priors = [list(labels).count(x) / len(list(labels)) for x in self.label_categories]
        self.categories_count = {}
        self.probabilities = {}
        self.multiplications = {}

    def nb(self):
        summed_feature_to_label_ratio = self._sum_feature_to_label_ratio()

        features_categories_count = _calculate_features_categories_count(summed_feature_to_label_ratio)

        probabilities = self._calculate_probabilities(summed_feature_to_label_ratio, features_categories_count)

        multiplications = self._calculate_multiplications(probabilities)

        self.multiplications = multiplications
        return multiplications

    def _sum_feature_to_label_ratio(self):
        """Summing the feature to label matching cases"""
        summed_feature_to_label_ratio = {}

        for label_position, data_row in enumerate(self.data):
            for feature_inx, feature in enumerate(data_row):
                # Using the feature name, feature value and the label value as the key
                probability_key = "%s=%s|%s" % (self.feature_names[feature_inx], feature, self.labels[label_position])

                if summed_feature_to_label_ratio.get(probability_key):
                    summed_feature_to_label_ratio[probability_key] += 1
                else:
                    summed_feature_to_label_ratio[probability_key] = 1

        return summed_feature_to_label_ratio

    def _calculate_probabilities(self, summed_feature_to_label_ratio, features_categories_count):
        """Divides each of the feature to label ratio with sum of the corresponding label"""
        probabilities = summed_feature_to_label_ratio.copy()

        for feature_categories_idx, feature_categories in enumerate(self.feature_variations):
            for feature_category in feature_categories:
                for label_category_idx, label_category in enumerate(self.label_categories):
                    probability_key = "%s=%s|%s" % \
                                      (self.feature_names[feature_categories_idx], feature_category, label_category)

                    if probabilities.get(probability_key):
                        # The sum of the corresponding label
                        probabilities[probability_key] /= self.label_counts[label_category_idx]

                    else:
                        # Smoothing
                        probabilities[probability_key] = 1 / features_categories_count

        return probabilities

    def _calculate_multiplications(self, probabilities):
        """Multiply the all the relevant feature to label ratios with the priors to create the labels predictions
        for each feature variation instance"""
        multiplications = {}

        for variation in self.multiplications_variations:
            for label_variation_idx, label_category in enumerate(self.label_categories):
                product = self.priors[label_variation_idx]

                for feature_category_idx, feature_category in enumerate(variation):
                    probability_key = "%s=%s|%s" % \
                                      (self.feature_names[feature_category_idx], feature_category, label_category)

                    product *= probabilities[probability_key]

                # Create the multiplication key by the order of multiplication operations to create unique keys
                multiplication_key = "*".join(variation) + "|" + label_category

                multiplications[multiplication_key] = product

        return multiplications

    def _predict(self, features):
        """Generate multiplication key by the order of multiplication operations to find corresponding prediction"""
        string_features = "*".join(features)

        max_args = (None, 0)

        for label_category in self.label_categories:
            multiplication_key = string_features + "|" + label_category

            if max_args[1] < self.multiplications[multiplication_key]:
                max_args = (label_category, self.multiplications[multiplication_key])

        return max_args[0]

    def evaluate(self, test_data_m, labels):
        correct_predict = 0
        wrong_predict = 0
        for index, row in test_data_m.iterrows(): # For each row in the dataset
            result = self._predict(row.tolist()[:-1])
            if result == test_data_m[labels].iloc[index]: # Predicted value and expected value is same or not
                correct_predict += 1
            else:
                wrong_predict += 1
        accuracy = correct_predict / (correct_predict + wrong_predict) # Calculate accuracy ( (TP + TN) / All Samples )
        return accuracy
