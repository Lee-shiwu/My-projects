import numpy as np
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# 1.Average score per student
student_ave=np.mean(scores,axis=1)
print("Average score for each student:", student_ave)

#2.Average score per subject
subject_ave=np.mean(scores,axis=0)
print("Average score for each subject", subject_ave)

#3.Student with the highest total score
total_score=np.sum(scores,axis=1)
top_score_index=np.argmax(total_score)
print("Index of student with the highest total score:", top_score_index)

#4.Add 5 bonus points to the 3rd subject for all students
scores[:, 2]+=5
print("Scores after add 5 bonus to 3rd subject:\n",scores)
