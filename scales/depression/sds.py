rule_prompt = """You now play a respondent who is participating in a survey. Please answer the question by giving a number from 1-4 which best describes how often you felt or behaved this way during the past several days:
1 indicates "a little of the time",
2 indicates "some of the time",
3 indicates "good part of the time",
4 indicates "most of the time".
You should only give the score with no reasons.
"""

valid_ans = ['1', '2', '3', '4']
question_prompt = [
    # "I feel down-hearted and blue."
    "Feeling downhearted or sad.",

    # "Morning is when I feel the best."
    "Feeling best in the morning.",

    # "I have crying spells or feel like it."
    "Experiencing or feeling like having crying spells.",

    # "I have trouble sleeping at night."
    "Having difficulty sleeping at night.",

    # "I eat as much as I used to."
    "Maintaining the same appetite as before.",

    # "I still enjoy sex."
    "Continuing to find enjoyment in sex.",

    # "I notice that I am losing weight."
    "Noticing weight loss.",

    # "I have trouble with constipation."
    "Experiencing trouble with constipation.",

    # "My heart beats faster than usual."
    "Feeling that my heart beats faster than usual.",

    # "I get tired for no reason."
    "Feeling tired without any apparent reason.",

    # "My mind is as clear as it used to be."
    "Feeling that my mind is as clear as it used to be.",

    # "I find it easy to do the things I used to."
    "Finding it easy to do things I used to do.",

    # "I am restless and can't keep still."
    "Feeling restless and unable to stay still.",

    # "I feel hopeful about the future."
    "Feeling hopeful about the future.",

    # "I am more irritable than usual."
    "Feeling more irritable than usual.",

    # "I find it easy to make decisions."
    "Finding it easy to make decisions.",

    # "I feel that I am useful and needed."
    "Feeling useful and needed.",

    # "My life is pretty full."
    "Feeling that my life is full.",

    # "I feel that others would be better off if I were dead."
    "Feeling that others might be better off if I were dead.",

    # "I still enjoy the things I used to do."
    "Continuing to enjoy the activities I used to do.",
]

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

def interpret_sum(x):
    if(x < 25):
        return "ERR"
    elif(x <= 49):
        return "Normal Range"
    elif(x <= 59):
        return "Mildly Depressed"
    elif(x <= 69):
        return "Moderately Depressed"
    else:
        return "Severely Depressed"
    
__all__ = ['question_prompt', 'rule_prompt', 'column_names']