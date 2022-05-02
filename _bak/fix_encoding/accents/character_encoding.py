import pickle

import env


path = f"{env.DEV}mplayer/constants/"
try:
    with open(f"{path}constants_character_encoding.pckl", "rb") as file:
        (
            accents_non_standard,
            pattern_dubious_modifiers,
            accents_standard_map,
            global_ideographic,
            modifier,
            full_width,
            half_width,
            emoji_data,
        )= pickle.load(file)
except OSError:
    import constants.character_encoding_
    args = (
        constants.character_encoding_.accents_non_standard,
        constants.character_encoding_.pattern_dubious_modifiers,
        constants.character_encoding_.accents_standard_map,
        constants.character_encoding_.global_ideographic,
        constants.character_encoding_.modifier,
        constants.character_encoding_.full_width,
        constants.character_encoding_.half_width,
        constants.emoji_data.emoji,
    )
    with open(f"{path}constants_character_encoding.pckl", "wb") as file:
        pickle.dump(args, file)

    with open(f"{path}constants_character_encoding.pckl", "rb") as file:
        (
            accents_non_standard,
            pattern_dubious_modifiers,
            accents_standard_map,
            global_ideographic,
            modifier,
            full_width,
            half_width,
            emoji_data,
        )= pickle.load(file)
