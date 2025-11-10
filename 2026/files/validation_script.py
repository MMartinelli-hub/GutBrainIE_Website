import json

# DEFINE HERE THE PATH(S) TO YOUR PREDICTIONS
PREDICTIONS_PATH_6_1 = 'path/to/your/NER/predictions/in/json/format'
PREDICTIONS_PATH_6_2 = 'path/to/your/binary_tag_RE/predictions/in/json/format'
PREDICTIONS_PATH_6_3 = 'path/to/your/ternary_tag_RE/predictions/in/json/format'
PREDICTIONS_PATH_6_4 = 'path/to/your/ternary_mention_RE/predictions/in/json/format'

# DEFINE HERE FOR WHICH SUBTASK(S) YOU WANT TO TEST YOUR PREDICTIONS
TEST_6_1_NER = True
TEST_6_2_BINARY_TAG_RE = True
TEST_6_3_TERNARY_TAG_RE = True
TEST_6_4_TERNARY_MENTION_RE = True

print_all_details = False # If set to True, prints the details for each processed entity/relation
print_article_details = False # If set to True, prints the details for each processed article

LEGAL_ENTITY_LABELS = [
    "anatomical location",
    "animal",
    "bacteria",
    "biomedical technique",
    "chemical",
    "DDF",
    "dietary supplement",
    "drug",
    "food",
    "gene",
    "human",
    "microbiome",
    "statistical technique"
]

LEGAL_RELATION_LABELS = [
    "administered",
    "affect",
    "change abundance",
    "change effect",
    "change expression",
    "compared to",
    "impact",
    "influence",
    "interact",
    "is a",
    "is linked to",
    "located in",
    "part of",
    "produced by",
    "strike",
    "target",
    "used by"
]


def test_submission_6_1_NER(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            predictions = json.load(file)
    except OSError:
        raise OSError(f'Error in opening the specified json file: {path}')
    
    total_entities_count = 0
    for pmid in predictions.keys():
        try:
            entities = predictions[pmid]['entities']
        except KeyError:
            raise KeyError(f'{pmid} - Not able to find field \"entities\" within article')
        
        doc_entities_count = 0
        for entity in entities:
            try:
                start_idx = int(entity["start_idx"])
                end_idx = int(entity["end_idx"])
                location = str(entity["location"])
                text_span = str(entity["text_span"])
                label = str(entity["label"]) 
            except KeyError:
                raise KeyError(f'{pmid} - Not able to find one or more of the expected fields for entity: {entity}')
            
            if label not in LEGAL_ENTITY_LABELS:
                raise NameError(f'{pmid} - Illegal label {label} for entity: {entity}')

            total_entities_count += 1
            doc_entities_count += 1
            if print_all_details:
                print(f'\n===== {pmid}: entity{doc_entities_count} =====')
                print(f'start: {start_idx}, end: {end_idx}, loc: {location}, text: {text_span}, label: {label}')

        if print_article_details:            
            print(f'===== Total entities for article {pmid}: {doc_entities_count} =====\n\n')
    
    print(f'\n===== Total entities for the collection: {total_entities_count} =====\n\n')


def test_submission_6_2_binary_tag_RE(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            predictions = json.load(file)
    except OSError:
        raise OSError(f'Error in opening the specified json file: {path}')
    
    total_relations_count = 0
    for pmid in predictions.keys():
        try:
            relations = predictions[pmid]['binary_tag_based_relations']
        except KeyError:
            raise KeyError(f'{pmid} - Not able to find field \"binary_tag_based_relations\" within article')
        
        doc_relations_count = 0
        for relation in relations:
            try:
                subject_label = str(relation["subject_label"])
                object_label = str(relation["object_label"]) 
            except KeyError:
                raise KeyError(f'{pmid} - Not able to find one or more of the expected fields for relation: {relation}')
            
            if subject_label not in LEGAL_ENTITY_LABELS:
                raise NameError(f'{pmid} - Illegal subject entity label {subject_label} for relation: {relation}')
            
            if object_label not in LEGAL_ENTITY_LABELS:
                raise NameError(f'{pmid} - Illegal object entity label {object_label} for relation: {relation}')

            total_relations_count += 1
            doc_relations_count += 1
            if print_all_details:
                print(f'\n===== {pmid}: relation{doc_relations_count} =====')
                print(f'subj_label: {subject_label}, obj_label: {object_label}')
            
        if print_article_details:
            print(f'===== Total relations for article {pmid}: {doc_relations_count} =====\n\n')
    
    print(f'\n===== Total relations for the collection: {total_relations_count} =====\n\n')
    

def test_submission_6_3_ternary_tag_RE(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            predictions = json.load(file)
    except OSError:
        raise OSError(f'Error in opening the specified json file: {path}')
    
    total_relations_count = 0
    for pmid in predictions.keys():
        try:
            relations = predictions[pmid]['ternary_tag_based_relations']
        except KeyError:
            raise KeyError(f'{pmid} - Not able to find field \"ternary_tag_based_relations\" within article')
        
        doc_relations_count = 0
        for relation in relations:
            try:
                subject_label = str(relation["subject_label"])
                predicate = str(relation["predicate"])
                object_label = str(relation["object_label"]) 
            except KeyError:
                raise KeyError(f'{pmid} - Not able to find one or more of the expected fields for relation: {relation}')
            
            if subject_label not in LEGAL_ENTITY_LABELS:
                raise NameError(f'{pmid} - Illegal subject entity label {subject_label} for relation: {relation}')
            
            if object_label not in LEGAL_ENTITY_LABELS:
                raise NameError(f'{pmid} - Illegal object entity label {object_label} for relation: {relation}')
            
            if predicate not in LEGAL_RELATION_LABELS:
                raise NameError(f'{pmid} - Illegal predicate {predicate} for relation: {relation}')

            total_relations_count += 1
            doc_relations_count += 1
            if print_all_details:
                print(f'\n===== {pmid}: relation{doc_relations_count} =====')
                print(f'subj_label: {subject_label}, predicate: {predicate}, obj_label: {object_label}')
            
        if print_article_details:
            print(f'===== Total relations for article {pmid}: {doc_relations_count} =====\n\n')
    
    print(f'\n===== Total relations for the collection: {total_relations_count} =====\n\n')


def test_submission_6_4_ternary_mention_RE(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            predictions = json.load(file)
    except OSError:
        raise OSError(f'Error in opening the specified json file: {path}')
    
    total_relations_count = 0
    for pmid in predictions.keys():
        try:
            relations = predictions[pmid]['ternary_mention_based_relations']
        except KeyError:
            raise KeyError(f'{pmid} - Not able to find field \"ternary_mention_based_relations\" within article')
        
        doc_relations_count = 0
        for relation in relations:
            try:
                subject_text_span = str(relation["subject_text_span"])
                subject_label = str(relation["subject_label"])
                predicate = str(relation["predicate"])
                object_text_span = str(relation["object_text_span"])
                object_label = str(relation["object_label"]) 
            except KeyError:
                raise KeyError(f'{pmid} - Not able to find one or more of the expected fields for relation: {relation}')
            
            if subject_label not in LEGAL_ENTITY_LABELS:
                raise NameError(f'{pmid} - Illegal subject entity label {subject_label} for relation: {relation}')
            
            if object_label not in LEGAL_ENTITY_LABELS:
                raise NameError(f'{pmid} - Illegal object entity label {object_label} for relation: {relation}')
            
            if predicate not in LEGAL_RELATION_LABELS:
                raise NameError(f'{pmid} - Illegal predicate {predicate} for relation: {relation}')

            total_relations_count += 1
            doc_relations_count += 1
            if print_all_details:
                print(f'\n===== {pmid}: relation{doc_relations_count} =====')
                print(f'subj_text: {subject_text_span}, subj_label: {subject_label}, predicate: {predicate}, obj_text: {object_text_span}, obj_label: {object_label}')
            
        if print_article_details:
            print(f'===== Total relations for article {pmid}: {doc_relations_count} =====\n\n')
    
    print(f'\n===== Total relations for the collection: {total_relations_count} =====\n\n')


if __name__ == '__main__':
    if TEST_6_1_NER:
        test_submission_6_1_NER(PREDICTIONS_PATH_6_1)
    
    if TEST_6_2_BINARY_TAG_RE:
        test_submission_6_2_binary_tag_RE(PREDICTIONS_PATH_6_2)

    if TEST_6_3_TERNARY_TAG_RE:
        test_submission_6_3_ternary_tag_RE(PREDICTIONS_PATH_6_3)
    
    if TEST_6_4_TERNARY_MENTION_RE:
        test_submission_6_4_ternary_mention_RE(PREDICTIONS_PATH_6_4)