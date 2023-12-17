from utils.recommendation_library import get_combinations
import json

with open('data.json') as f:
    outfit_data = json.load(f)
    # json_results = json.dumps(prediction_results, indent=2)

# # Print or save the JSON results as needed
# print(json_results)

recommendations = json.dumps(get_combinations(outfit_data),indent=2)

if __name__ == '__main__':
    print(recommendations)

