# this file mustn't import any other files
def hp_change(name, hp_to_change):
    name['hp'] = name['hp'] + hp_to_change
    return name


currently_selected = None
