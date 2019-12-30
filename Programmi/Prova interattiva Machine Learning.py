from sklearn import tree
caratteristiche=[[1,55,1],[1,57,1],[1,57,1],[2,36,2]]
frutto=[1,1,2,2]

classificatore=tree.DecisionTreeClassifier()
classificatore=classificatore.fit(caratteristiche,frutto)
print (classificatore.predict([[1,46,1]]))
