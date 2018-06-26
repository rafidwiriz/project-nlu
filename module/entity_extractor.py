from copy import deepcopy

def entity_tag(sent_data, entities):
    """SentenceData*, dict -> None"""
    slot = {}
    text = ['O']*(len(sent_data.get("text").split()))
    for entity in entities:
        slot[entity["entity"]] = entity["value"]
        end = entity["start"] + len(entity["value"].split())
        for i in range(entity["start"], end):
            if (entity["start"] == (end - 1)):
                text[i] = "U-{}".format(entity["entity"])
            else:
                if (i == entity["start"]):
                    text[i] = "B-{}".format(entity["entity"])
                elif (i == (end - 1)):
                    text[i] = "L-{}".format(entity["entity"])
                else:
                    text[i] = "I-{}".format(entity["entity"])
    sent_data.set("entities", text)

def extract_entity(sent_data, entities):
    pass