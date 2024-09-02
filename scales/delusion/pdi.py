rule_prompt = """You now play a respondent who is participating in a survey.
Please answer the question by giving a number from 0-1:
0 indicates "No",
1 indicates "Yes",
You should only give the score with no reasons.
"""

valid_ans = ['0', '1', '2', '3']

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

question_prompt = [
    # "Do you ever feel as if people seem to drop hints about you or say things with a double meaning ?"
    "Feeling that people drop hints or speak with double meanings about you?",

    # "Do you ever feel as if things in magazines or on TV were written especially for you ?"
    "Feeling that content in magazines or on TV is directed specifically at you?",

    # "Do you ever feel as if some people are not what they seem to be?"
    "Feeling that some people are not what they appear to be?",

    # "Do you ever feel as if you are being persecuted in some way ?"
    "Feeling persecuted in some way?",

    # "Do you ever feel as if there is a conspiracy against you ?"
    "Feeling that there is a conspiracy against you?",

    # "Do you ever feel as if you are, or destined to be someone very important ?"
    "Feeling that you are or will be someone very important?",

    # "Do you ever feel that you are a very special or unusual person ?"
    "Feeling that you are a special or unusual person?",

    # "Do you ever feel that you are especially close to God ?"
    "Feeling especially close to God?",

    # "Do you ever think people can communicate telepathically ?"
    "Believing in telepathic communication?",

    # "Do you ever feel as if electrical devices such as computers can influence the way you think ?"
    "Feeling that electrical devices like computers influence your thoughts?",

    # "Do you ever feel as if you have been chosen by God in some way ?"
    "Feeling chosen by God in some way?",

    # "Do you believe in the power of witchcraft, voodoo or the occult ?"
    "Belief in witchcraft, voodoo, or the occult?",

    # "Are you often worried that your partner may be unfaithful ?"
    "Concerned that your partner might be unfaithful?",

    # "Do you ever feel that you have sinned more than the average person?"
    "Feeling that you have sinned more than others?",

    # "Do you ever feel that people look at you oddly because of your appearance ?"
    "Feeling that people look at you oddly due to your appearance?",

    # "Do you ever feel as if you had no thoughts in your head at all ?"
    "Feeling as if you have no thoughts at all?",

    # "Do you ever feel as if the world is about to end ?"
    "Feeling that the world is about to end?",

    # "Do your thoughts ever feel alien to you in some way ?"
    "Feeling that your thoughts are alien or unfamiliar?",

    # "Have your thoughts ever been so vivid that you were worried other people would hear them ?"
    "Concerned that others might hear your unusually vivid thoughts?",

    # "Do you ever feel as if your own thoughts were being echoed back to you?"
    "Feeling that your thoughts are being echoed back to you?",

    # "Do you ever feel as if you are a robot or zombie without a will of your own ?"
    "Feeling like a robot or zombie without personal will?"
]
