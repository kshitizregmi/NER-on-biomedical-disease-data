test_f1scores = None
valid_f1scores = None

with open('scores/valid_f1scores.json', 'r', encoding = "utf-8") as f:
    valid_f1scores = eval(f.read())

with open('scores/test_f1scores.json', 'r', encoding = "utf-8") as f:
    test_f1scores = eval(f.read())
    
import matplotlib.pyplot as plt
x=range(0,20)
plt.plot(valid_f1scores,label="Validation F1_score")
plt.plot(test_f1scores,label="Test F1_score")
plt.xlabel('Iterations')
plt.ylabel('F1 score')
plt.legend()
plt.title('F1 score vs Iterations for validation and test data')
plt.show()
