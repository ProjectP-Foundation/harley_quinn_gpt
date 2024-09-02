rule_prompt = """You now play a respondent who is participating in a survey. Please answer the question by giving a number from 1-4 which best describes how often you felt or behaved this way during the past several days:
1 indicates "a little of the time",
2 indicates "some of the time",
3 indicates "good part of the time",
4 indicates "most of the time".
You should only give the score with no reasons.
"""

valid_ans = ['1', '2', '3', '4']
question_prompt = [
    # "I feel more nervous and anxious than usual."
    "Experiencing heightened nervousness and anxiety.",

    # "I feel afraid for no reason at all."
    "Feeling fearful without any apparent cause.",

    # "I get upset easily or feel panicky."
    "Becoming easily upset or feeling panicky.",

    # "I feel like I'm falling apart and going to pieces."
    "Feeling as if I'm losing control or falling apart.",

    # "I feel that everything is all right and nothing bad will happen."
    "Believing that everything is fine and nothing bad will occur.",

    # "My arms and legs shake and tremble."
    "Experiencing trembling or shaking in arms and legs.",

    # "I am bothered by headaches neck and back pain."
    "Being troubled by headaches, neck pain, or back pain.",

    # "I feel weak and get tired easily."
    "Feeling weak and becoming tired easily.",

    # "I feel calm and can sit still easily."
    "Feeling calm and able to sit still without difficulty.",

    # "I can feel my heart beating fast."
    "Noticing a rapid heartbeat.",

    # "I am bothered by dizzy spells."
    "Being disturbed by episodes of dizziness.",

    # "I have fainting spells or feel like it."
    "Experiencing or feeling like fainting.",

    # "I can breathe in and out easily."
    "Breathing in and out with ease.",

    # "I get numbness and tingling in my fingers and toes."
    "Experiencing numbness or tingling in fingers and toes.",

    # "I am bothered by stomach aches or indigestion."
    "Being troubled by stomachaches or indigestion.",

    # "I have to empty my bladder often."
    "Feeling the need to empty my bladder frequently.",

    # "My hands are usually dry and warm."
    "Having dry and warm hands.",

    # "My face gets hot and blushes."
    "Experiencing flushing or a hot sensation in the face.",

    # "I fall asleep easily and get a good night's rest."
    "Falling asleep easily and getting restful sleep.",

    # "I have nightmares."
    "Having nightmares or disturbing dreams.",
]

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

def interpret_sum(x):
    if(x < 20):
        return "ERR"
    elif(x <= 44):
        return "Normal Range"
    elif(x <= 59):
        return "Mild to Moderate Anxiety Levels"
    elif(x <= 74):
        return "Marked to Severe Anxiety Levels"
    else:
        return "Extreme Anxiety Levels"
    
__all__ = ['question_prompt', 'rule_prompt', 'column_names']