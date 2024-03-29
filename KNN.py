from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class KNN():
    def fit(self,X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
        
    def predict(self,X_test):
        predictions = []
        for row in X_test:
            labels = self.closest(row)
            predictions.append(labels)
        return predictions
    
    def closest(self,row):
        best_dist = euc(row,self.X_train[0])
        best_index = 0
        for i in range(1,len(self.X_train)):
            dist = euc(row,self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

from sklearn import datasets

iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.5)

clf = KNN()
clf.fit(X_train,y_train)

predictions = clf.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,predictions))