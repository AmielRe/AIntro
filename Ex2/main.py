from Algorithms.NB import NaiveBayes
from Utils.file import File
import pandas as pd
from Algorithms.ID3 import ID3

def main():
    # Load training data from file
    data, feature_names, labels = File.load_train_data(r'Files/train.txt')

    # Create ID3 classifier and create the tree
    tree_clf = ID3(data=data, feature_names=feature_names, labels=labels)
    tree_clf.id3()

    # Create NaiveBayes
    naive_base = NaiveBayes(data=data, feature_names=feature_names, labels=labels)
    naive_base.nb()

    # Load test data from file
    test_data = pd.read_csv(r'Files/test.txt', sep="\t")

    # Write the tree to 'output_tree' file in required format
    with open(r'Files/output_tree.txt', 'w') as f:
        File.write_tree_output(f, tree_clf.node)

    # Write both algorithms result and accuracy
    with open(r'Files/output.txt', 'w') as f:
        File.write_output(f, tree_clf, naive_base, test_data, test_data.columns[-1])


if __name__ == "__main__":
    main()
