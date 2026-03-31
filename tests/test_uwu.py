import pytest
from bs_generator import uwu_mutator


def test_uwu_mutator_raises_type_error_for_non_string():
    with pytest.raises(TypeError):
        uwu_mutator(123)  

def test_uwu_mutator_raise_value_error_for_invalid_intensity_low():
    with pytest.raises(ValueError):
        uwu_mutator("hello", intensity=0)

def test_uwu_mutator_raise_value_error_for_invalid_intensity_high():
    with pytest.raises(ValueError):
        uwu_mutator("hello", intensity=4)

def test_uwu_mutator_returns_empty_string_unchanged():
    assert uwu_mutator("") == ""

def test_uwu_mutator_returns_spaces_unchanged():
    assert uwu_mutator(" ") == " "

def test_uwu_mutator_intensity1_replaces_r_and_l():
    assert uwu_mutator("Hello friend", intensity = 1) == "Hewwo fwiend"

def test_uwu_mutator_intensity1_reserves_non_target_letter():
    assert uwu_mutator("cat", intensity = 1) == "cat"

def test_uwu_mutator_intensity1_handles_uppercase_r_and_l():
    assert uwu_mutator("LOL REALLY", intensity = 1) == "WOW WEAWWY"

def test_uwu_mutator_intensity2_replaces_special_words():
    result = uwu_mutator("I love my dog", intensity= 2)
    assert "wuv" in result
    assert "doggo" in result

def test_uwu_mutator_intensity2_preserves_capitalization_for_capitalized_word():
    assert uwu_mutator("Love", intensity=2) == "Wuv"

def test_uwu_mutator_intensity2_preserves_capitalization_for_uppercase_word():
    assert uwu_mutator("LOVE", intensity=2) == "WUV"

def test_uwu_mutator_intensity_2_adds_ny_for_lowercase_n_before_vowel():
    result = uwu_mutator("nice", intensity=2)
    assert "nyice" in result

def test_uwu_mutator_intensity_2_adds_ny_for_uppercase_n_before_vowel():
    result = uwu_mutator("Nice", intensity=2)
    assert "Ny" in result

def test_uwu_mutator_intensity_3_adds_period_suffix():
    result = uwu_mutator("Hi.", intensity=3)
    possible_suffixes = {" uwu.", " owo.", " >w<.", " ^w^.", " nyaa~"}
    assert any(suffix in result for suffix in possible_suffixes)

def test_uwu_mutator_intensity_3_adds_exclamation_suffix():
    result = uwu_mutator("Hi!", intensity=3)
    possible_suffixes = {" owo!", " >w<!", " ^_^!", " :3!", " nyaa!!"}
    assert any(suffix in result for suffix in possible_suffixes)

def test_uwu_mutator_intensity_3_adds_question_suffix():
    result = uwu_mutator("Hi?", intensity=3)
    possible_suffixes = {" owo?", " uwu?", " >_<?", " ;w;?", " nyaa??"}
    assert any(suffix in result for suffix in possible_suffixes)