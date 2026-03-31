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

    def test_multiline(self):
        """test multiline input"""
        input = """
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        """.strip()
        output = """
☹□❒♏🔾 🖐🞐⬧◆🔾 ♓⬧ ⬧♓🔾🞐●⮹ ♎◆🔾🔾⮹ ⧫♏⌧⧫ □♐ ⧫♒♏ 🞐❒♓■⧫♓■♑ ♋■♎ ⧫⮹🞐♏⬧♏⧫⧫♓■♑ ♓■♎◆⬧⧫❒⮹📬 ☹□❒♏🔾 🖐🞐⬧◆🔾 ♒♋⬧ ♌♏♏■ ⧫♒♏ ♓■♎◆⬧⧫❒⮹🕯⬧ ⬧⧫♋■♎♋❒♎ ♎◆🔾🔾⮹ ⧫♏⌧⧫ ♏❖♏❒ ⬧♓■♍♏ ⧫♒♏ 📂🗄📁📁⬧📪 ⬥♒♏■ ♋■ ◆■🙵■□⬥■ 🞐❒♓■⧫♏❒ ⧫□□🙵 ♋ ♑♋●●♏⮹ □♐ ⧫⮹🞐♏ ♋■♎ ⬧♍❒♋🔾♌●♏♎ ♓⧫ ⧫□ 🔾♋🙵♏ ♋ ⧫⮹🞐♏ ⬧🞐♏♍♓🔾♏■ ♌□□🙵📬 🖐⧫ ♒♋⬧ ⬧◆❒❖♓❖♏♎ ■□⧫ □■●⮹ ♐♓❖♏ ♍♏■⧫◆❒♓♏⬧📪 ♌◆⧫ ♋●⬧□ ⧫♒♏ ●♏♋🞐 ♓■⧫□ ♏●♏♍⧫❒□■♓♍ ⧫⮹🞐♏⬧♏⧫⧫♓■♑📪 ❒♏🔾♋♓■♓■♑ ♏⬧⬧♏■⧫♓♋●●⮹ ◆■♍♒♋■♑♏♎📬 🖐⧫ ⬥♋⬧ 🞐□🞐◆●♋❒♓⬧♏♎ ♓■ ⧫♒♏ 📂🖲⌛📁⬧ ⬥♓⧫♒ ⧫♒♏ ❒♏●♏♋⬧♏ □♐ ☹♏⧫❒♋⬧♏⧫ ⬧♒♏♏⧫⬧ ♍□■⧫♋♓■♓■♑ ☹□❒♏🔾 🖐🞐⬧◆🔾 🞐♋⬧⬧♋♑♏⬧📪 ♋■♎ 🔾□❒♏ ❒♏♍♏■⧫●⮹ ⬥♓⧫♒ ♎♏⬧🙵⧫□🞐 🞐◆♌●♓⬧♒♓■♑ ⬧□♐⧫⬥♋❒♏ ●♓🙵♏ ✌●♎◆⬧ 🏱♋♑♏💣♋🙵♏❒ ♓■♍●◆♎♓■♑ ❖♏❒⬧♓□■⬧ □♐ ☹□❒♏🔾 🖐🞐⬧◆🔾📬        
        """.strip()

        result = wingdingsify(input, only_alphanumneric=False)
        assert result is output

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
        assert result is output
