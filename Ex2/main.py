from Ex2.Algorithms.NB import NaiveBayes
from Utils.file import File
import pandas as pd
from Algorithms.ID3 import DecisionTreeClassifier

def main():
    # Run ID3
    data, feature_names, labels = File.load_train_data(r'Files/train.txt')
    tree_clf = DecisionTreeClassifier(data=data, feature_names=feature_names, labels=labels)
    tree_clf.id3()
    with open(r'Files/output_tree.txt', 'w') as f:
        File.write_tree_output(f, tree_clf.node)
    test_data = pd.read_csv(r'Files/test.txt', sep="\t")
    accuracy = tree_clf.evaluate(test_data, test_data.columns[-1])
    print("Test accuracy {:.4f}".format(accuracy))

    naive_base = NaiveBayes(data=data, feature_names=feature_names, labels=labels)

    naive_base.nb()

    print(naive_base.evaluate(test_data, test_data.columns[-1]))


if __name__ == "__main__":
    main()
