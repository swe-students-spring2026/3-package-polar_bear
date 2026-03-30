import pytest
import bs_generator.emotion as emotion_module
from bs_generator.emotion import emotion_mutator


def test_default_map_replaces_period():
    result = emotion_mutator("Hello.")
    assert " fr." in result


def test_default_replaces_question_and_exclamation(monkeypatch):
    monkeypatch.setattr(emotion_module.random, "random", lambda: 1.0)
    monkeypatch.setattr(emotion_module.random, "choice", lambda seq: ":)")
    result = emotion_mutator("A? B!", emotion="funny")
    assert " huh?" in result
    assert " no cap!!" in result


def test_invalid_emotion():
    with pytest.raises(ValueError):
        emotion_mutator("hello", emotion="angry")


def test_invalid_emotion_type():
    with pytest.raises(TypeError):
        emotion_mutator("hello", emotion=1)


def test_invalid_text_type():
    with pytest.raises(TypeError):
        emotion_mutator(123)


def test_happy_emotion_exclamation_style():
    result = emotion_mutator("Wow!", emotion="happy")
    assert "!!!" in result


def test_sleepy_emotion_exclamation_style():
    result = emotion_mutator("Wow!", emotion="sleepy")
    assert "..." in result


def test_emotion_can_add_keyboard_face(monkeypatch):
    monkeypatch.setattr(emotion_module.random, "random", lambda: 0.0)
    monkeypatch.setattr(emotion_module.random, "choice", lambda seq: ":)")
    result = emotion_mutator("hello world", emotion="classic")
    assert ":)" in result


def test_emotion_forces_one_face_when_none_added(monkeypatch):
    monkeypatch.setattr(emotion_module.random, "random", lambda: 1.0)
    monkeypatch.setattr(emotion_module.random, "choice", lambda seq: "(¬‿¬)")
    result = emotion_mutator("hello world", emotion="smug")
    assert "(¬‿¬)" in result
