"""pytest test_emoji.py -v"""
import pytest
from bs_generator.emoji import emoji_mutator

class TestEmoji:
    def test_hello(self):
        result = emoji_mutator("hello there")
        assert "👋" in result

    def test_ok(self):
        result = emoji_mutator("ok sure")
        assert "👌" in result
        
    def test_multiple_words(self):
        result = emoji_mutator("hello yes ok")
        assert "👋" in result
        assert "👍" in result
        assert "👌" in result
        
    def test_one_word(self):
        result = emoji_mutator("hello")
        assert "hello" in result
        assert "👋" in result

    def test_uppercase(self):
        result = emoji_mutator("HELLO")
        assert "👋" in result

    def test_mixed_case(self):
        result = emoji_mutator("HeLLo")
        assert "👋" in result

    def test_uppercase_ok(self):
        result = emoji_mutator("OK")
        assert "👌" in result

    def test_mixed_case_ok(self):
        result = emoji_mutator("Ok")
        assert "👌" in result

class TestColor:
    def test_default_multicolor(self):
        result = emoji_mutator("hello")
        assert any(emoji in result for emoji in ["🌈", "✨", "🎉", "🦄"])

    def test_red_color(self):
        result = emoji_mutator("hello", color="red")
        assert any(emoji in result for emoji in ["❤️", "🌹", "🍓", "🔥"])

    def test_blue_color(self):
        result = emoji_mutator("hello", color="blue")
        assert any(emoji in result for emoji in ["💙", "🫐", "🌊", "🌀"])

    def test_green_color(self):
        result = emoji_mutator("hello", color="green")
        assert any(emoji in result for emoji in ["💚", "🌿", "🍀", "🐢"])

    def test_yellow_color(self):
        result = emoji_mutator("hello", color="yellow")
        assert any(emoji in result for emoji in ["💛", "🌟", "🌼", "🍋"])


class TestInvalidInput:
    def test_invalid_text_type_int(self):
        with pytest.raises(TypeError):
            emoji_mutator(123)

    def test_invalid_text_type_none(self):
        with pytest.raises(TypeError):
            emoji_mutator(None)

    def test_invalid_color(self):
        with pytest.raises(ValueError):
            emoji_mutator("hello", color="purple")

class TestEdgeCases:
    def test_empty_string(self):
        assert emoji_mutator("") == ""

    def test_whitespace_only(self):
        assert emoji_mutator("   ") == "   "

    def test_no_match_keeps_original_words(self):
        result = emoji_mutator("random words")
        assert "random" in result
        assert "words" in result

    def test_no_partial_match(self):
        result = emoji_mutator("hellohello")
        assert "👋" not in result