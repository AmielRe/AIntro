import pandas as pd
from Algorithms.ID3 import ID3
from Components.Node import Node
from Algorithms.NB import NaiveBayes

class File:
    @staticmethod
    def load_train_data(filename: str):
        """Load training data, remove the classification and return the data, feature_names and labels."""
        data_df = pd.read_csv(filename, sep="\t")
        data = data_df.iloc[:, :-1].to_numpy()
        labels = data_df.iloc[:, -1].to_numpy()
        feature_names = data_df.columns[:-1].tolist()
        return data, feature_names, labels
    
    @staticmethod
    def write_tree_output(file_to_write_to, node: Node, indent: str = "") -> None:
        """Recursive function that prints the ID3 tree in the desired format."""
        if node is None:
            return

        if node.childs is not None:
            for child in node.childs:
                # Check if we got a result here (for the different format)
                next_indent = indent + "|" if indent != "" else indent
                if child.nextFeature.childs is None:
                    file_to_write_to.write(f"{next_indent}{node.value}={child.value}:{child.nextFeature.value}\n")
                else:
                    file_to_write_to.write(f"{next_indent}{node.value}={child.value}\n")
                File.write_tree_output(file_to_write_to, child.nextFeature, indent + "\t")
   
    @staticmethod
    def write_output(file_to_write_to, id3: ID3, naive_bayes: NaiveBayes, test_data, label):
        id3_correct_predict = 0
        nb_correct_predict = 0
        id3_wrong_predict = 0
        nb_wrong_predict = 0
        for index, row in test_data.iterrows(): # For each row in the dataset
            id3_result = id3._predict(row.tolist()[:-1])
            nb_result = naive_bayes._predict(row.tolist()[:-1])
            file_to_write_to.write(f"{id3_result}\t{nb_result}\n")

            if id3_result == test_data[label].iloc[index]: # Predicted value and expected value is same or not
                id3_correct_predict += 1
            else:
                id3_wrong_predict += 1

            if nb_result == test_data[label].iloc[index]: # Predicted value and expected value is same or not
                nb_correct_predict += 1
            else:
                nb_wrong_predict += 1

        # Calculate accuracy ( (TP + TN) / All Samples )
        id3_accuracy = id3_correct_predict / (id3_correct_predict + id3_wrong_predict)
        nb_accuracy = nb_correct_predict / (nb_correct_predict + nb_wrong_predict)
        file_to_write_to.write("{:.3f}\t{:.3f}".format(id3_accuracy, nb_accuracy))
