from utils.recommendation_library import get_combinations
import json

with open('data.json') as f:
    outfit_data = json.load(f)

recommendations = get_combinations(outfit_data)

if __name__ == '__main__':
    print(recommendations)

