score_1 = [98, 99, 87, 78, 56]
score_2 = score_1
print("原本的score_1", score_1)
print("原本的score_2", score_2)
score_2[4] = 59.9
print("修改的score_1", score_1)
print("修改的score_2", score_2)
print("-" * 20)
print("id of score_1", id(score_1))
print("id of score_2", id(score_2))