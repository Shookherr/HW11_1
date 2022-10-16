import json


def load_candidates_from_json(path):
    """
    Возвращает список всех кандидатов
    """
    with open(path, 'r', encoding='utf-8') as file:     # открытие файла
        data = json.load(file)                          # загрузка данных

    return data


def get_candidate(candidate_id, data):
    """
    Возвращает одного кандидата по его id
    """
    for dat in data:
        if int(dat.get('id')) == candidate_id:
            return True, dat
    return False, f'Нет кандидатов с id={candidate_id}'


def get_candidates_by_name(candidate_name, data):
    """
    Возвращает кандидатов по имени
    """
    candidates = []

    for dat in data:
        if candidate_name.upper() == dat.get('name').upper():
            candidates.append(dat)
            continue
    if len(candidates) == 0:
        return f'Нет кандидатов с именем \"{candidate_name}\"'
    return candidates


def get_candidates_by_skill(skill_name, data):
    """
    Возвращает кандидатов по навыку
    """
# Инициализация массива словарей с кандидатами
    candidates = []

    for dat in data:
        if skill_name.upper() in dat.get('skills').upper():
            candidates.append(dat)
            continue
    if len(candidates) == 0:
        return f'Нет кандидатов с навыком \"{skill_name}\"'
    return candidates
