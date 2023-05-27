from Utils.file import File
import pandas as pd
from Algorithms.ID3 import DecisionTreeClassifier

def main():
    # Run ID3
    data, feature_names, labels = File.load_train_data(r'Ex2/Files/train.txt')
    tree_clf = DecisionTreeClassifier(data=data, feature_names=feature_names, labels=labels)
    tree_clf.id3()
    with open(r'Ex2/Files/output_tree.txt', 'w') as f:
        File.write_tree_output(f, tree_clf.node)
    test_data = pd.read_csv(r'Ex2/Files/test.txt', sep="\t")
    accuracy = tree_clf.evaluate(test_data, test_data.columns[-1])
    print("Test accuracy {:.4f}".format(accuracy))
        
if __name__ == "__main__":
    main()
