def extract_entity(sent_data):
    """SentenceData* -> Dict"""
    slot = {}
    entities = sent_data.get("entities")
    text = sent_data.get("token")
    for entity in entities:
        slot[entity["entity"]] = entity["value"]
        if not("end" in entity):
            entity["end"] = entity["start"]
        for i in range(entity["start"], (entity["end"] + 1)):
            text[i] = "({})".format(entity["entity"]) if (i == entity["start"]) else 'del'
    if 'del' in text: text.remove('del')

    return slot