def extract_entity(sent_data):
    """SentenceData* -> dict"""
    slot = {}
    entities = sent_data.get("entities")
    text = sent_data.get("tokens")
    for entity in entities:
        slot[entity["entity"]] = entity["value"]
        end = entity["start"] + len(entity["value"].split())
        #if not("end" in entity):
        #    entity["end"] = entity["start"]
        for i in range(entity["start"], end):
            text[i] = "({})".format(entity["entity"]) if (i == entity["start"]) else '#del'
    while '#del' in text:
        text.remove('#del')

    return slot