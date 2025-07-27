import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = {
        "PERSON": [],
        "ORG": [],
        "GPE": [],
        "EDUCATION": [],
        "EXPERIENCE": [],
        "SKILLS": []
    }

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    lines = text.split('\n')
    skills, education, experience = [], [], []

    for line in lines:
        line = line.strip().lower()
        if any(degree in line for degree in ["b.tech", "m.tech", "bachelor", "master"]):
            education.append(line)
        if any(exp in line for exp in ["years", "experience", "worked at", "intern at"]):
            experience.append(line)
        if any(skill in line for skill in ["python", "ml", "data", "sql", "java", "cloud"]):
            skills.append(line)

    entities["EDUCATION"].extend(education)
    entities["EXPERIENCE"].extend(experience)
    entities["SKILLS"].extend(skills)

    return entities
