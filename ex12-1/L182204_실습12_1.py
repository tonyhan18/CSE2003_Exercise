# title : 실습 12 1번(24p)
# Develop by : 20182204 한찬희
# Date : 2021-06-02

#  아래의 학생들의 성적표를 numpy의 array로 만들어, 각 과목별 평균과 학생 개인의 평균 점수를 구하고, 이를 과목별 그래프와, 학생 별 그래프로 나타내는 scrip를 작성할 것.
# numpy를 import하여, 각 학생(A~D)의 이름으로 4x4 array를 만들고, numpy의 function를 이용하여 연산할 것.(아래 표의 녹색 부분)
# matplotlib을 import하여, 과목평균과 학생평균에 대한 두 개의 그래프를 작성할 것. 그래프의 모양은 보기 좋게 자유롭게 옵션 작성.

import numpy as np
import matplotlib.pyplot as plt

student = np.array([[75, 89, 92, 78],
       [90, 76, 88, 83],
       [55, 99, 81, 88],
       [80, 67, 75, 91]])
stuSum = np.sum(student, axis = 1)/len(student[0]) # Student
subSum = np.sum(student, axis = 0)/len(student[0]) # Subject

print(stuSum)
print(subSum)

x = np.array(["A","B","C","D"])
y = np.array(["Kor","Math","Eng","Com"])

plt.title("Student Average")
plt.plot(x,stuSum,'g:o')
plt.show()
plt.title("Subject Average")
plt.plot(y,subSum,'b:o')
plt.show()