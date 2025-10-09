from main import saludo

def test_saludo():
    assert saludo("Mundo") == "Hola, Mundo!"
    assert saludo("Mundo") == "Hola, Mund!"