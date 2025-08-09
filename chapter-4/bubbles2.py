scores = [40, 101, 50, 30, 40, 110, 20, 200, 50, 60, 40, 30, 70, 90, 80, 85]


highest_score = 0
highest_score_index = 0
lowest_scores = []
second_highest_score = 0 
second_highest_score_index = 0

for score in scores:
    if score > highest_score:
        highest_score = score
print(highest_score, "is the highest score")

for score in scores:
    if score < highest_score:
        lowest_scores.append(score)
    
for score in lowest_scores:
    if score > second_highest_score:
        second_highest_score = score

highest_score_index = scores.index(highest_score)        
second_highest_score_index = scores.index(second_highest_score)        
print("top highest scores are at index:", highest_score_index, "and", second_highest_score_index)

## If we are to find the index of the top 2 highest scores, if there are more than one, get them into an array by checking if the score == highest_score and then appending them into an array
