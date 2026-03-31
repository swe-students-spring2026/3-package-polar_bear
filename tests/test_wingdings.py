import pytest

from bs_generator.wingdings import wingdingsify


class TestWingdingsify:
    """tests for bs_generator.wingdingsify"""

    def test_empty(self):
        """test empty input"""
        result = wingdingsify("", True)
        assert result is ""

    def test_empty_with_flag(self):
        """test empty input with only_alphanumeric"""
        result = wingdingsify("", True)
        assert result is ""

    def test_wingdings(self):
        """test multiline input"""
        input = """
        None of the characters were mapped to Unicode at the time. However, Unicode approved the addition of many symbols in the Wingdings and Webdings fonts in Unicode 7.0.
        """.strip()
        output = """
        ☠□■♏ □♐ ⧫♒♏ ♍♒♋❒♋♍⧫♏❒⬧ ⬥♏❒♏ 🔾♋🞐🞐♏♎ ⧫□ 🕆■♓♍□♎♏ ♋⧫ ⧫♒♏ ⧫♓🔾♏📬 ☟□⬥♏❖♏❒📪 🕆■♓♍□♎♏ ♋🞐🞐❒□❖♏♎ ⧫♒♏ ♋♎♎♓⧫♓□■ □♐ 🔾♋■⮹ ⬧⮹🔾♌□●⬧ ♓■ ⧫♒♏ 🕈♓■♑♎♓■♑⬧ ♋■♎ 🕈♏♌♎♓■♑⬧ ♐□■⧫⬧ ♓■ 🕆■♓♍□♎♏ 🖮📬📁📬
        """.strip()

        result = wingdingsify(input, only_alphanumneric=False)
        assert result == output

    def test_multiline_with_flag(self):
        input = """
        Wingdings is a series of dingbat fonts that render letters as a variety of symbols.
        They were originally developed in 1990 by Microsoft.
        
        a! b@ c# d$ *e (f )g 0) 9( *8 4$
        """.strip()

        output = """
        🕈♓■♑♎♓■♑⬧ ♓⬧ ♋ ⬧♏❒♓♏⬧ □♐ ♎♓■♑♌♋⧫ ♐□■⧫⬧ ⧫♒♋⧫ ❒♏■♎♏❒ ●♏⧫⧫♏❒⬧ ♋⬧ ♋ ❖♋❒♓♏⧫⮹ □♐ ⬧⮹🔾♌□●⬧.
        ❄♒♏⮹ ⬥♏❒♏ □❒♓♑♓■♋●●⮹ ♎♏❖♏●□🞐♏♎ ♓■ 📂🖲🖲📁 ♌⮹ 💣♓♍❒□⬧□♐⧫.
        
        ♋! ♌@ ♍# ♎$ *♏ (♐ )♑ 📁) 🖲( *🖰 🗐$
        """.strip()

        result = wingdingsify(input, only_alphanumneric=True)
        assert result == output
