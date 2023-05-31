from Utils.file import File
import pandas as pd
from Algorithms.ID3 import DecisionTreeClassifier

def main():
    # Load training data from file
    data, feature_names, labels = File.load_train_data(r'Files/train.txt')

    # Create ID3 classifier
    tree_clf = DecisionTreeClassifier(data=data, feature_names=feature_names, labels=labels)

    # Create the tree
    tree_clf.id3()

    # Write the tree to 'output_tree' file in required format
    with open(r'Files/output_tree.txt', 'w') as f:
        File.write_tree_output(f, tree_clf.node)

    # Load test data from file
    test_data = pd.read_csv(r'Files/test.txt', sep="\t")

    # Evaluate and print the accuracy of the ID3
    accuracy = tree_clf.evaluate(test_data, test_data.columns[-1])
    print("Test accuracy {:.4f}".format(accuracy))


if __name__ == "__main__":
    main()
