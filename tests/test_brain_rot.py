"""pytest test_brain_rot.py -v"""
import pytest
from bs_generator.brain_rot import brain_rot_mutator


class TestLevel1:
    def test_period_replaced(self):
        result = brain_rot_mutator("Hello world.", intensity=1)
        assert " fr." in result
        assert "Hello world" in result

    def test_question_mark_replaced(self):
        result = brain_rot_mutator("Are you okay?", intensity=1)
        assert " huh?" in result

    def test_exclamation_replaced(self):
        result = brain_rot_mutator("Let's go!", intensity=1)
        assert " no cap!" in result

    def test_comma_replaced(self):
        result = brain_rot_mutator("Yes, boss.", intensity=1)
        assert " lowkey," in result

    def test_no_slang_injected(self):
        result = brain_rot_mutator("simple words only", intensity=1)
        assert result == "simple words only"

    def test_not_all_caps(self):
        result = brain_rot_mutator("Hello World.", intensity=1)
        assert result != result.upper()


class TestLevel2:
    def test_punctuation_still_replaced(self):
        result = brain_rot_mutator("Hello world.", intensity=2)
        assert " fr." in result

    def test_output_is_longer_over_trials(self):
        original = "Prof Bloomberg is the best New York University Professor"
        longer_at_least_once = False
        for _ in range(30):
            if len(brain_rot_mutator(original, intensity=2)) > len(original):
                longer_at_least_once = True
                break
        assert longer_at_least_once

    def test_not_all_caps(self):
        result = brain_rot_mutator("Hello World", intensity=2)
        assert not result.isupper()


class TestLevel3:
    def test_output_all_caps(self):
        result = brain_rot_mutator("hello world", intensity=3)
        assert result.isupper()

    def test_original_words_uppercased(self):
        result = brain_rot_mutator("original text", intensity=3)
        assert "ORIGINAL" in result
        assert "TEXT" in result

    def test_period_replacement_uppercased(self):
        result = brain_rot_mutator("done.", intensity=3)
        assert " FR." in result


class TestEdgeCases:
    def test_empty_string(self):
        assert brain_rot_mutator("", intensity=1) == ""

    def test_whitespace_only(self):
        assert brain_rot_mutator("   ", intensity=1) == "   "

    def test_invalid_intensity(self):
        with pytest.raises(ValueError):
            brain_rot_mutator("test", intensity=5)

    def test_invalid_text_type_int(self):
        with pytest.raises(TypeError):
            brain_rot_mutator(42, intensity=1)  

    def test_invalid_text_type_none(self):
        with pytest.raises(TypeError):
            brain_rot_mutator(None, intensity=1) 

    def test_returns_str(self):
        assert isinstance(brain_rot_mutator("hi", intensity=1), str)