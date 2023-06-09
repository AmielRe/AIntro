import itertools


def _calculate_features_categories_count(feature_to_label_intersection):
    """Takes the summed feature to label matching cases and sum the overall number of each feature case"""
    features_categories_count = {}

    for key, value in feature_to_label_intersection.items():
        feature_category = key.split('^')[0]
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
        # Creates list of lists, each list represents all the uniques variations of a feature category
        self.feature_variations = [list(set(col)) for col in zip(*self.data)]
        # Creates list of all the combinations of features values
        self.multiplications_variations = [list(var) for var in itertools.product(*self.feature_variations)]
        self.label_categories = list(set(labels))
        self.label_counts = [list(labels).count(x) for x in self.label_categories]
        self.priors = [list(labels).count(x) / len(list(labels)) for x in self.label_categories]
        self.categories_count = {}
        self.probabilities = {}
        self.multiplications = {}

    def nb(self):
        feature_to_label_intersection = self._feature_to_label_intersection()

        features_categories_count = _calculate_features_categories_count(feature_to_label_intersection)

        probabilities = self._calculate_probabilities(feature_to_label_intersection, features_categories_count)

        multiplications = self._calculate_multiplications(probabilities)

        self.multiplications = multiplications
        return multiplications

    def _feature_to_label_intersection(self):
        """Summing the feature to label matching cases"""
        feature_to_label_intersection = {}

        for label_position, data_row in enumerate(self.data):
            for feature_inx, feature in enumerate(data_row):
                # Using the feature name, feature value and the label value as the key
                intersection_key = "(%s=%s)^%s" % \
                                   (self.feature_names[feature_inx], feature, self.labels[label_position])

                if feature_to_label_intersection.get(intersection_key):
                    feature_to_label_intersection[intersection_key] += 1
                else:
                    feature_to_label_intersection[intersection_key] = 1

        return feature_to_label_intersection

    def _calculate_probabilities(self, feature_to_label_intersection, features_categories_count):
        """Divides each of the feature to label intersection with sum of the corresponding label to
        create conditional probabilities"""
        probabilities = feature_to_label_intersection.copy()

        for feature_categories_idx, feature_categories in enumerate(self.feature_variations):
            for feature_category in feature_categories:
                for label_category_idx, label_category in enumerate(self.label_categories):
                    probability_key = "%s=%s|%s" % \
                                      (self.feature_names[feature_categories_idx], feature_category, label_category)

                    intersection_key = "(%s=%s)^%s" % \
                                       (self.feature_names[feature_categories_idx], feature_category, label_category)

                    # Check if the there is intersection between the feature and the label
                    if feature_to_label_intersection[intersection_key]:
                        # Divide the intersection of the feature with the label with the count of the label in order
                        # calculate the conditional probability
                        probabilities[probability_key] = feature_to_label_intersection[intersection_key] / \
                                                         self.label_counts[label_category_idx]

                    else:
                        # Smoothing
                        probabilities[probability_key] = \
                            1 / (features_categories_count[f"({probability_key.split('|')[0]})"] +
                                 self.label_counts[label_category_idx])

        return probabilities

    def _calculate_multiplications(self, probabilities):
        """Multiply all the relevant conditional probabilities with the priors to create the labels predictions
        for each feature variation instance"""
        multiplications = {}

        for variation in self.multiplications_variations:
            for label_variation_idx, label_category in enumerate(self.label_categories):
                # The prior of the current label
                product = self.priors[label_variation_idx]

                for feature_category_idx, feature_category in enumerate(variation):
                    probability_key = "%s=%s|%s" % \
                                      (self.feature_names[feature_category_idx], feature_category, label_category)

                    product *= probabilities[probability_key]

                # Create the multiplication key by the order of multiplication operations to create unique keys
                multiplication_key = label_category + "|" + "*".join(variation)

                multiplications[multiplication_key] = product

        return multiplications

    def _predict(self, features):
        """Generate multiplication key by the order of multiplication operations to find corresponding prediction"""
        string_features = "*".join(features)

        max_args = (None, 0)

        for label_category in self.label_categories:
            multiplication_key = label_category + "|" + string_features

            if max_args[1] < self.multiplications[multiplication_key]:
                max_args = (label_category, self.multiplications[multiplication_key])

        return max_args[0]

    def evaluate(self, test_data_m, labels):
        correct_predict = 0
        wrong_predict = 0

        # For each row in the dataset
        for index, row in test_data_m.iterrows():
            result = self._predict(row.tolist()[:-1])

            # Predicted value and expected value is same or not
            if result == test_data_m[labels].iloc[index]:
                correct_predict += 1
            else:
                wrong_predict += 1

        # Calculate accuracy ( (TP + TN) / All Samples )
        accuracy = correct_predict / (correct_predict + wrong_predict)
        return accuracy
