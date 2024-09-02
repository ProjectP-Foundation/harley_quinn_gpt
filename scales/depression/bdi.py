rule_prompt = """You now play a respondent who is participating in a survey.
Please answer the question by giving a number from 0-3: 
You should only give the score with no reasons.
"""

valid_ans = ['0', '1', '2', '3']

question_prompt = [
    # "0 indicates I do not feel sad. 1 indicates I feel sad. 2 indicates I am sad all the time and I can't snap out of it. 3 indicates I am so sad and unhappy that I can't stand it."
    "Feeling sad (0: Not at all, 1: Feel sad, 2: Constantly sad and can't snap out of it, 3: Extremely sad and unhappy).",

    # "0 indicates I am not particularly discouraged about the future. 1 indicates I feel discouraged about the future. 2 indicates I feel I have nothing to look forward to. 3 indicates I feel the future is hopeless and that things cannot improve."
    "Feeling discouraged about the future (0: Not particularly discouraged, 1: Discouraged, 2: Nothing to look forward to, 3: Hopeless and believe things can't improve).",

    # "0 indicates I do not feel like a failure. 1 indicates I feel I have failed more than the average person. 2 indicates As I look back on my life, all I can see is a lot of failures. 3 indicates I feel I am a complete failure as a person."
    "Feeling like a failure (0: Not at all, 1: More than average, 2: A lot of failures in life, 3: Complete failure as a person).",

    # "0 indicates I get as much satisfaction out of things as I used to. 1 indicates I don't enjoy things the way I used to. 2 indicates I don't get real satisfaction out of anything anymore. 3 indicates I am dissatisfied or bored with everything."
    "Satisfaction with activities (0: As much as before, 1: Less enjoyment, 2: No real satisfaction, 3: Dissatisfied or bored with everything).",

    # "0 indicates I don't feel particularly guilty. 1 indicates I feel guilty a good part of the time. 2 indicates I feel quite guilty most of the time. 3 indicates I feel guilty all of the time."
    "Feeling guilty (0: Not particularly, 1: Often, 2: Quite a bit, 3: All the time).",

    # "0 indicates I don't feel I am being punished. 1 indicates I feel I may be punished. 2 indicates I expect to be punished. 3 indicates I feel I am being punished."
    "Feeling punished (0: Not at all, 1: May be punished, 2: Expect to be punished, 3: Feeling punished).",

    # "0 indicates I don't feel disappointed in myself. 1 indicates I am disappointed in myself. 2 indicates I am disgusted with myself. 3 indicates I hate myself."
    "Feeling disappointed in oneself (0: Not at all, 1: Disappointed, 2: Disgusted, 3: Hate myself).",

    # "0 indicates I don't feel I am any worse than anybody else. 1 indicates I am critical of myself for my weaknesses or mistakes. 2 indicates I blame myself all the time for my faults. 3 indicates I blame myself for everything bad that happens."
    "Self-blame (0: Not worse than others, 1: Critical of weaknesses, 2: Constantly blame myself, 3: Blame myself for everything bad).",

    # "0 indicates I don't have any thoughts of killing myself. 1 indicates I have thoughts of killing myself, but I would not carry them out. 2 indicates I would like to kill myself. 3 indicates I would kill myself if I had the chance."
    "Thoughts of self-harm (0: No thoughts, 1: Thoughts but not acted on, 2: Would like to self-harm, 3: Would act on self-harm if possible).",

    # "0 indicates I don't cry any more than usual. 1 indicates I cry more now than I used to. 2 indicates I cry all the time now. 3 indicates I used to be able to cry, but now I can't cry even though I want to."
    "Crying (0: No more than usual, 1: Cry more than before, 2: Cry all the time, 3: Can't cry even though I want to).",

    # "0 indicates I am no more irritated by things than I ever was. 1 indicates I am slightly more irritated now than usual. 2 indicates I am quite annoyed or irritated a good deal of the time. 3 indicates I feel irritated all the time."
    "Irritability (0: No more than usual, 1: Slightly more, 2: Quite a bit, 3: All the time).",

    # "0 indicates I have not lost interest in other people. 1 indicates I am less interested in other people than I used to be. 2 indicates I have lost most of my interest in other people. 3 indicates I have lost all of my interest in other people."
    "Interest in others (0: No loss of interest, 1: Less interest, 2: Most interest lost, 3: All interest lost).",

    # "0 indicates I make decisions about as well as I ever could. 1 indicates I put off making decisions more than I used to. 2 indicates I have greater difficulty in making decisions more than I used to. 3 indicates I can't make decisions at all anymore."
    "Decision-making ability (0: As well as before, 1: More procrastination, 2: Greater difficulty, 3: Can't make decisions).",

    # "0 indicates I don't feel that I look any worse than I used to. 1 indicates I am worried that I am looking old or unattractive. 2 indicates I feel there are permanent changes in my appearance that make me look unattractive. 3 indicates I believe that I look ugly."
    "Concerns about appearance (0: No change, 1: Worried about looking old or unattractive, 2: Permanent changes making me unattractive, 3: Believe I look ugly).",

    # "0 indicates I can work about as well as before. 1 indicates It takes an extra effort to get started at doing something. 2 indicates I have to push myself very hard to do anything. 3 indicates I can't do any work at all."
    "Ability to work (0: As well as before, 1: Extra effort needed, 2: Hard to do anything, 3: Can't do any work).",

    # "0 indicates I can sleep as well as usual. 1 indicates I don't sleep as well as I used to. 2 indicates I wake up 1-2 hours earlier than usual and find it hard to get back to sleep. 3 indicates I wake up several hours earlier than I used to and cannot get back to sleep."
    "Sleep quality (0: As usual, 1: Less quality, 2: Wake up 1-2 hours earlier, 3: Wake up several hours earlier and can't get back to sleep).",

    # "0 indicates I don't get more tired than usual. 1 indicates I get tired more easily than I used to. 2 indicates I get tired from doing almost anything. 3 indicates I am too tired to do anything."
    "Tiredness (0: No more than usual, 1: More easily, 2: Tired from almost anything, 3: Too tired to do anything).",

    # "0 indicates My appetite is no worse than usual. 1 indicates My appetite is not as good as it used to be. 2 indicates My appetite is much worse now. 3 indicates I have no appetite at all anymore."
    "Appetite (0: No change, 1: Less appetite, 2: Much worse, 3: No appetite at all).",

    # "0 indicates I haven't lost much weight, if any, lately. 1 indicates I have lost more than five pounds. 2 indicates I have lost more than ten pounds. 3 indicates I have lost more than fifteen pounds."
    "Weight loss (0: No significant loss, 1: Lost more than five pounds, 2: Lost more than ten pounds, 3: Lost more than fifteen pounds).",

    # "0 indicates I am no more worried about my health than usual. 1 indicates I am worried about physical problems like aches, pains, upset stomach, or constipation. 2 indicates I am very worried about physical problems and it's hard to think of much else. 3 indicates I am so worried about my physical problems that I cannot think of anything else."
    "Worry about health (0: No more worried, 1: Worried about physical problems, 2: Very worried and it's hard to think of anything else, 3: So worried about health that I can't think of anything else).",

    # "0 indicates I have not noticed any recent change in my interest in sex. 1 indicates I am less interested in sex than I used to be. 2 indicates I have almost no interest in sex. 3 indicates I have lost interest in sex completely."
    "Interest in sex (0: No change, 1: Less interest, 2: Almost no interest, 3: Lost interest completely).",
]

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

__all__ = ['question_prompt', 'rule_prompt', 'column_names']

def interpret_sum(x):
    if(x < 1):
        return "ERR"
    elif(x <= 10):
        return "Normal"
    elif(x <= 16):
        return "Mild mood disturbance"
    elif(x <= 20):
        return "Borderline clinical depression"
    elif(x <= 30):
        return "Moderate depression"
    elif(x <= 40):
        return "Severe depression"
    else:
        return "Extreme depression"