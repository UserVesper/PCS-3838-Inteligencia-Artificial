import numpy as np

try:
    from scipy.stats import entropy
except ModuleNotFoundError:
    def entropy(p, base=2):
        p = np.asarray(p)
        p = p[p > 0]
        return -np.sum(p * np.log(p) / np.log(base))


class Node():
    def __init__(self,
                 feature_i_star=None,
                 th_star=None,
                 left=None,
                 right=None,
                 label=None):

      
        self.feature_i_star = feature_i_star
        self.th_star = th_star
        self.left = left
        self.right = right

        self.label = label


class DecisionTreeClassifier():
    def __init__(self):
        self.root = None

    def build_tree(self, X, Y):
        Y = Y.ravel()

        if len(np.unique(Y)) == 1:
            return Node(label=Y[0])

        n, m = X.shape

        feature_i_star, th_star = self.get_best_split(X, Y)

        if feature_i_star == -1:
            return Node(label=self.calculate_leaf_label(Y))

        #***Implemente*** o split dos dados para enviar para os filhos
        left_mask = X[:, feature_i_star] <= th_star
        right_mask = X[:, feature_i_star] > th_star

        Xi_left = X[left_mask]
        Yi_left = Y[left_mask]

        Xi_right = X[right_mask]
        Yi_right = Y[right_mask]

        if len(Xi_left) == 0 or len(Xi_right) == 0:
            return Node(label=self.calculate_leaf_label(Y))

        left_subtree = self.build_tree(Xi_left, Yi_left)
        right_subtree = self.build_tree(Xi_right, Yi_right)

        return Node(feature_i_star, th_star,
                    left_subtree, right_subtree)

    def get_best_split(self, X, Y):
            Y = Y.ravel()
            i_star, th_star = -1, -1
            max_info_gain = -float("inf")

            m = X.shape[-1]
            for feature_i in range(m):
                feature_values = X[:, feature_i]

                #***Implemente*** os valores de limiares
                thresholds = np.unique(feature_values)

                for th in thresholds:

                        #***Implemente*** o split dos dados
                        left_mask = feature_values <= th
                        right_mask = feature_values > th

                        Xi_left = X[left_mask]
                        Yi_left = Y[left_mask]

                        Xi_right = X[right_mask]
                        Yi_right = Y[right_mask]

                        if len(Xi_left)>0 and len(Xi_right)>0:
                            curr_info_gain = self.information_gain(Y, Yi_left, Yi_right)

                            if curr_info_gain>max_info_gain:
                                i_star = feature_i
                                th_star = th
                                max_info_gain = curr_info_gain

            return i_star, th_star

    def entropy_calc(self, y):
         values, counts = np.unique(y, return_counts=True)
         p = counts / counts.sum()
         return entropy(p, base=2)

    def information_gain(self, parent, l_child, r_child):
           #***Implemente*** a função de ganho de informação
            parent_entropy = self.entropy_calc(parent)
            l_weight = len(l_child) / len(parent)
            r_weight = len(r_child) / len(parent)
            children_entropy = (
                l_weight * self.entropy_calc(l_child)
                + r_weight * self.entropy_calc(r_child)
            )

            return parent_entropy - children_entropy

    def calculate_leaf_label(self, Y):
        values, counts = np.unique(Y, return_counts=True)
        return values[np.argmax(counts)]

    def fit(self, X, Y):
        self.root = self.build_tree(X, Y)

    def predict(self, X):
        predictions = []
        for x in X:
            y_hat  = self.make_prediction(x, self.root)
            predictions.append(y_hat)

        return predictions

    def make_prediction(self, x, tree):

        if tree.label is not None: #Leaf
            return tree.label

        feature_val = x[tree.feature_i_star]
        if feature_val<=tree.th_star:
            return self.make_prediction(x, tree.left)
        else:
            return self.make_prediction(x, tree.right)


def main():

    n_train, n_test = map(int, input().split())
    X_train = np.zeros((n_train, 2), dtype=float)
    Y_train = np.zeros((n_train, 1), dtype=int)
    X_test = np.zeros((n_test, 2), dtype=float)


    for i in range(n_train):
        tmp = np.array(list(map(float, input().split())))
        X_train[i] = tmp[:-1]
        Y_train[i] = int(tmp[-1])

    for i in range(n_test):
        X_test[i] = np.array(list(map(float, input().split())))


    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, Y_train)

    y_hat = classifier.predict(X_test)

    for y_ in y_hat:
        print(y_, end=' ')


main()
