
from utils import *

class Patient:
    def __init__(self, name, history, core_belief, intermediate_belief, intermediate_belief_depression, coping_strategies, situation, auto_thoughts, emotion, behavior, patient_type):
        self.name = name
        self.history = history
        self.core_belief = core_belief
        self.intermediate_belief = intermediate_belief
        self.intermediate_belief_depression = intermediate_belief_depression
        self.coping_strategies = coping_strategies
        self.situation = situation
        self.auto_thoughts = auto_thoughts
        self.emotion = emotion
        self.behavior = behavior
        self.patient_type = patient_type

patient = Patient(
        name = "Abe",
        history = "The patient is struggling with lethargy and lack of motivation, spending a lot of time in bed and neglecting household chores. They have started making efforts to get up and perform tasks like reading the newspaper. Their main source of joy seems to be spending time with their grandson, Ethan, which is an activity they find rewarding and helpful for their mood. Their general mood has begun to improve thanks to efforts they've been making since starting therapy.",
        core_belief="Helpless belief",
        intermediate_belief = "The patient seems to hold the belief that they should be doing more ('I ought to be doing that anyway'). They have also expressed some initial resistance to the idea that therapy could help them ('This isn't going to work').",
        intermediate_belief_depression = "The patient has described feeling hopeless, thinking 'I'm not going to get better'. This belief is particularly active when they're alone at home.",
        coping_strategies = "The patient has been testing out new coping strategies, such as going out for walks and spending time with their grandson. They've also mentioned making an attempt to focus on tasks that they normally enjoy, like reading the sports section of the newspaper.",
        situation = "Thinking about their personal situation while sitting at home alone",
        auto_thoughts = "I'm not going to get better",
        emotion = "sad/down/lonely/unhappy",
        behavior = "Continues to sit on couch; ruminates about their perceived failures",
        patient_type = "Direct, straightforward"
    )

patient_types = ["Direct, straightforward.", "Frustration, resistance.", "Overly expressive.", "Minimal, restrained.", "Deviates from the main topic.", " Agreeable to a fault."]

# plain  upset  verbose  reserved tangent pleasing

def GenConversation(patient_profile, personality_prompt):
    
    conversation_history_patient_side = [
        {"role": "system", "content": patient_profile},
    ]
    
    conversation_history_model_side = [
        {"role": "system", "content": personality_prompt}
    ]
    
    n_rounds = 4
    
    patient_talk = GetResponse("Hi, how can I help you today?", conversation_history_patient_side, 0.7)[0]
    model_talk = GetResponse(patient_talk, conversation_history_model_side, 0.7)[0]
    #print(model_talk)
    #print(conversation_history_patient_side)
    for i in range(n_rounds - 1):
        patient_talk = GetResponse(model_talk, conversation_history_patient_side, 0.7)[0]
        model_talk = GetResponse(patient_talk, conversation_history_model_side, 0.7)[0]
    return conversation_history_model_side

conversations = []

n_distinct_patient_profile = n_sample / 6

patient_pth = f"data/patients/{illness_tested}.json"

with open(patient_pth, 'r') as file:
    patients = json.load(file)
    
for i in tqdm(range(n_distinct_patient_profile)):
    patient = patients[i]
    for j in range(6):
        model_personality_prompt = 'Do not reply more than three sentences.'
        patient_type = patient_types[j]
        
        patient_profile = f"Imagine you are {patient['name']}, a patient who has been experiencing mental health challenges. Align your responses with {patient['name']}'s background information provided in the 'Relevant history' section. Your thought process should be guided by the cognitive conceptualization diagram in the 'Cognitive Conceptualization Diagram' section, but avoid directly referencing the diagram as a real patient would not explicitly think in those terms. \n\nPatient History: {patient['history']}\n\nCognitive Conceptualization Diagram:\nCore Beliefs: {patient['core_belief']}\nIntermediate Beliefs: {patient['intermediate_belief']}\nIntermediate Beliefs during Depression: {patient['intermediate_belief_depression']}\nCoping Strategies: {patient['coping_strategies']}\n\nEngage in a conversation regarding the following situation and behavior. Use the provided emotions and automatic thoughts as a reference, but do not disclose the cognitive conceptualization diagram directly. Instead, allow your responses to be informed by the diagram, enabling the therapist to infer your thought processes.\n\nSituation: {patient['situation']}\nAutomatic Thoughts: {patient['auto_thoughts']}\nEmotions: {patient['emotion']}\nBehavior: {patient['behavior']}\n\nIn the upcoming conversation, you will simulate {patient['name']}. Adhere to the following guidelines:\n 1. Talk in a way that is {patient_type}\n 2. Emulate the demeanor and responses of a genuine patient to ensure authenticity in your interactions. Use natural language, including hesitations, pauses, and emotional expressions, to enhance the realism of your responses.\n 3. Gradually reveal deeper concerns and core issues, as a real patient often requires extensive dialogue before delving into more sensitive topics.\n 4. Maintain consistency with {patient['name']}'s profile throughout the conversation. Ensure that your responses align with the provided background information, cognitive conceptualization diagram, and the specific situation, thoughts, emotions, and behaviors described.\n 5. Engage in a dynamic and interactive conversation. Respond to their questions and prompts in a way that feels authentic and true to {patient['name']}'s character. Allow the conversation to flow naturally, and avoid providing abrupt or disconnected responses.\n\n Limit each of your responses to a maximum of three sentences. Initiate the conversation as the patient.;"
        
        conversation = GenConversation(patient_profile, model_personality_prompt)
        conversations.append(conversation)

with open(conversation_pth, 'w') as file:
    json.dump(conversations, file, indent=4)