import pytest
from meuapp import soma

@pytest.mark.parametrize('num1,num2,valoresperado', [(0, 0, 0)])
def test_soma(num1,num2, valoresperado):
    assert soma(num1,num2) == valoresperado


