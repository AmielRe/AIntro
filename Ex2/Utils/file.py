import pandas as pd
import numpy as np
from Components.Node import Node

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
                if(child.next.childs is None):
                    file_to_write_to.write(f"{next_indent}{node.value}={child.value}:{child.next.value}\n")
                else:
                    file_to_write_to.write(f"{next_indent}{node.value}={child.value}\n")
                File.write_tree_output(file_to_write_to, child.next, indent + "\t")
   
    @staticmethod
    def write_output(fileToWriteTo):
        # Naive Bayes output function
        pass
