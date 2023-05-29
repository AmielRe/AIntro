import math
from Components.Node import Node

class DecisionTreeClassifier:
    """Decision Tree Classifier using ID3 algorithm."""

    def __init__(self, data, feature_names, labels):
        self.data = data
        self.feature_names = feature_names
        self.labels = labels
        self.label_categories = list(set(labels))
        self.label_counts = [list(labels).count(x) for x in self.label_categories]
        self.node = None

    def _calculate_entropy(self, instance_ids):
        """Calculates the entropy for a given set of instances."""
        labels = [self.labels[i] for i in instance_ids]
        label_count = [labels.count(x) for x in self.label_categories]
        entropy = sum([-count / len(instance_ids) * math.log(count / len(instance_ids), 2) if count else 0 for count in label_count])
        return entropy

    def _calculate_information_gain(self, instance_ids, feature_id):
        """Calculates the information gain for a given feature."""
        entropy = self._calculate_entropy(instance_ids)
        feature_values = [self.data[x][feature_id] for x in instance_ids]
        unique_values = list(set(feature_values))
        feature_vals_count = [feature_values.count(x) for x in unique_values]
        feature_vals_id = [
            [instance_ids[i]
            for i, x in enumerate(feature_values)
            if x == y]
            for y in unique_values
        ]

        # Compute the information gain with the chosen feature
        info_gain = entropy - sum([val_counts / len(instance_ids) * self._calculate_entropy(val_ids)
                                     for val_counts, val_ids in zip(feature_vals_count, feature_vals_id)])

        return info_gain

    def _find_best_feature(self, instance_ids, feature_ids):
        """Finds the feature that maximizes the information gain."""
        features_gain = [self._calculate_information_gain(instance_ids, feature_id) for feature_id in feature_ids]
        max_id = feature_ids[features_gain.index(max(features_gain))]

        return self.feature_names[max_id], max_id

    def id3(self):
        """Initializes ID3 algorithm to build a Decision Tree Classifier."""
        instance_ids = [x for x in range(len(self.data))]
        feature_ids = [x for x in range(len(self.feature_names))]
        self.node = self._build_tree(instance_ids, feature_ids, self.node)

    def _build_tree(self, instance_ids, feature_ids, node):
        """Recursive function to build the decision tree."""
        if not node:
            node = Node()
        labels_in_features = [self.labels[x] for x in instance_ids]
        if len(set(labels_in_features)) == 1:
            node.value = self.labels[instance_ids[0]]
            return node
        if len(feature_ids) == 0:
            node.value = max(set(labels_in_features), key=labels_in_features.count)
            return node
        best_feature_name, best_feature_id = self._find_best_feature(instance_ids, feature_ids)
        node.value = best_feature_name
        node.childs = []
        feature_values = sorted(list(set([self.data[x][best_feature_id] for x in instance_ids])))
        for value in feature_values:
            child = Node()
            child.value = value  # Add a branch from the node to each feature value in our feature
            node.childs.append(child)  # Append new child node to current node
            child_x_ids = [x for x in instance_ids if self.data[x][best_feature_id] == value]
            if not child_x_ids:
                child.next = max(set(labels_in_features), key=labels_in_features.count)
            else:
                if feature_ids and best_feature_id in feature_ids:
                    to_remove = feature_ids.index(best_feature_id)
                    feature_ids.pop(to_remove)
                # Recursively call the algorithm
                child.next = self._build_tree(child_x_ids, feature_ids, child.next)
        return node
    
    def _predict(self, sample):
        """Predicts the label for a given instance."""
        node = self.node
        while node.childs:
            feature_id = self.feature_names.index(node.value)
            sample_value = sample[feature_id]
            child = next((child for child in node.childs if child.value == sample_value), None)
            if child:
                node = child.next
            else:
                # If there is no matching child node, return the most probable label
                label_counts = [self.labels.count(label) for label in self.label_categories]
                most_probable_label = self.label_categories[label_counts.index(max(label_counts))]
                return most_probable_label
        return node.value
            
    def evaluate(self, test_data_m, label):
        correct_predict = 0
        wrong_predict = 0
        for index, row in test_data_m.iterrows(): # For each row in the dataset
            result = self._predict(row.tolist()[:-1])
            if result == test_data_m[label].iloc[index]: # Predicted value and expected value is same or not
                correct_predict += 1
            else:
                wrong_predict += 1
        accuracy = correct_predict / (correct_predict + wrong_predict) # Calculate accuracy ( (TP + TN) / All Samples )
        return accuracy
