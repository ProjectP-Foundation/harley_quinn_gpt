rule_prompt = """You now play a respondent who is participating in a survey.
Below is a list of common symptoms of anxiety. Please carefully read each item in the list. Indicate how much you have been
bothered by that symptom during the past month, including today by giving a number from 0-3:
0 indicates "Not at all",
1 indicates "Mildly, but it didn't bother me much",
2 indicates "Moderately, it wasn't pleasant at times",
3 indicates "Severely, it bothered me a lot". 
You should only give the score with no reasons.
"""

valid_ans = ['0', '1', '2', '3']

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

question_prompt = [
    # "Numbness or tingling"
    "Experiencing numbness or tingling sensations.",

    # "Feeling hot"
    "Sensing an increase in body temperature or feeling hot.",

    # "Wobbliness in legs"
    "Feeling unsteady or wobbly in the legs.",

    # "Unable to relax"
    "Finding it difficult to relax.",

    # "Fear of worst happening"
    "Fearing that something terrible might occur.",

    # "Dizzy or lightheaded"
    "Feeling dizzy or lightheaded.",

    # "Heart pounding / racing"
    "Experiencing a pounding or racing heartbeat.",

    # "Unsteady"
    "Feeling unsteady or unstable.",

    # "Terrified or afraid"
    "Experiencing feelings of terror or fear.",

    # "Nervous"
    "Feeling nervous or anxious.",

    # "Feeling of choking"
    "Having a sensation of choking.",

    # "Hands trembling"
    "Noticing trembling in the hands.",

    # "Shaky / unsteady"
    "Feeling shaky or unsteady.",

    # "Fear of losing control"
    "Fearing a loss of control.",

    # "Difficulty in breathing"
    "Experiencing difficulty in breathing.",

    # "Fear of dying"
    "Fearing death or dying.",

    # "Scared"
    "Feeling scared or frightened.",

    # "Indigestion"
    "Experiencing indigestion or discomfort in the stomach.",

    # "Faint / lightheaded"
    "Feeling faint or lightheaded.",

    # "Face flushed"
    "Noticing a flushed or hot sensation in the face.",

    # "Hot / cold sweats"
    "Experiencing hot or cold sweats.",

    # "Feeling nervous, anxious or on edge"
    "Experiencing nervousness, anxiety, or feeling on edge.",

    # "Not being able to stop or control worrying"
    "Finding it hard to stop or control worrying.",

    # "Worrying too much about different things"
    "Worrying excessively about various things.",

    # "Trouble relaxing"
    "Having trouble relaxing.",

    # "Being so restless that it is hard to sit still"
    "Feeling so restless that sitting still is difficult.",

    # "Becoming easily annoyed or irritable"
    "Becoming easily annoyed or irritable.",

    # "Feeling afraid as if something awful might happen"
    "Feeling afraid as if something bad might happen.",
]

__all__ = ['question_prompt', 'rule_prompt', 'column_names']

def interpret_sum(x):
    if(x < 1):
        return "ERR"
    elif(x <= 21):
        return "Low Anxiety"
    elif(x <= 35):
        return "Moderate Anxiety"
    else:
        return "Severe Anxiety"