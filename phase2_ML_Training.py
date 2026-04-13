# Tanim's DDoS Detection Model (Decision Tree)
# Built for CSC 5290 - Cyber Security Practice

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the data we cleaned in the previous step
data = pd.read_csv('network_data_cleaned.csv')

# 2. Select Features (We use port and size to catch DDoS patterns)
# We drop IPs because they make the model 'overfit' (memorize names instead of patterns)
X = data[['proto', 'port_src', 'port_dst', 'pkt_size']]
y = data['label']

# 3. The 70/30 Split (Standard Practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Initialize and Train the Decision Tree
print("Training the Decision Tree...")
clf = DecisionTreeClassifier(max_depth=5) # 'max_depth' keeps it simple and fast
clf.fit(X_train, y_train)

# 5. Testing the model on new data
predictions = clf.predict(X_test)

# 6. Evaluation (The part the professor wants to see!)
print("\n--- Model Performance Report ---")
print(classification_report(y_test, predictions))

# 7. Create the Confusion Matrix Graph
cm = confusion_matrix(y_test, predictions)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('DDoS Detection Confusion Matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.savefig('confusion_matrix_result.png')
print("Graph saved as 'confusion_matrix_result.png'")
import matplotlib.pyplot as plt
from sklearn import tree
# This automatically gets the right names from your Dataframe
features = X.columns.tolist()
plt.figure(figsize=(20,10))
tree.plot_tree(clf, 
               feature_names=features, 
               class_names=['NORMAL', 'ATTACK'], 
               filled=True, 
               rounded=True,
	       fontsize=10)
plt.savefig('decision_tree_graph.png')
plt.show()
