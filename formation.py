# схема переводов параметра description не все значения в словарях были покачто реализованы

formats = {
    'en': ('endurance', lambda x: float(x)),
    'atk': ('atk', lambda x: int(x)),
    'drop': ('drop_dice_probability', lambda x: float(x)),
    'osh': ('one_shoot', lambda x: float(x)),
    'rev': ('reverse_action', lambda x: float(x)),
    'xp': ('heal', lambda x: int(x)),
    'mul': ('mul', lambda x: float(x)),
    'val': ('value', lambda x: int(x)),
    'dcd': ('death_crit_damage', lambda x: float(x)),
    'prob': ('probability', lambda x: float(x)),
}

deforms = {
    'value': 'val',
    'probability': 'prob',
    'endurance': 'en',
    'atk': 'atk',
    'mul': 'mul',
    'one_shoot': 'osh',
    'reverse_action': 'rev',
    'heal': 'xp',
    'drop_dice_probability': 'drop',
    'decrease_enemy_damage': 'dcd'
}


def format_description(description: str):
    description = description.split(';')
    res_dict = {}
    for el in range(len(description)):
        if '|' not in description[el]:
            res_dict['description'] = description[el]
        else:
            elem = description[el].split('|')
            if elem[1] in formats.keys():
                res_dict[formats[elem[1]][0]] = formats[elem[1]][1](elem[0])
    return res_dict


def deform_description(description: dict):
    res_str = []
    for k, v in description.items():
        if k == 'description':
            res_str.append(v)
        else:
            res_str.append(f'{deforms[k]}|{v}')
    return ';'.join(res_str)