import json

def get_value_to_order (dict):
    return dict['attempts']


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list

def get_top_scores():
    score_list = get_score_list()
    #top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:5]
    top_score_list = sorted(score_list, key=get_value_to_order)
    return top_score_list[:3]

def hello():
    print("hello")