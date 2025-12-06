import pytest
from energia import (
    TARIFA_KWH,
    calcular_fornecimento,
    calcular_icms,
    calcular_cofins,
    calcular_pis_pasep,
    calcular_fatura,
)

CONSUMOS = [0, 50, 100, 150, 200, 250, 300, 500, 800, 1200]

@pytest.fixture(scope="module")
def tarifa():
    return TARIFA_KWH

def _expected_values_manual(consumo, tarifa):
    fornecimento = consumo * tarifa
    if consumo <= 200:
        icms_factor = 0.136363
        cofins_factor = 0.0614722
        pis_factor = 0.013346
    else:
        icms_factor = 0.333333
        cofins_factor = 0.0730751
        pis_factor = 0.0158651

    icms = icms_factor * fornecimento
    cofins = cofins_factor * fornecimento
    pis = pis_factor * fornecimento
    icms_cofins = icms_factor * cofins_factor * fornecimento
    icms_pis = icms_factor * pis_factor * fornecimento
    fatura = fornecimento + icms + cofins + pis + icms_cofins + icms_pis
    return {
        "fornecimento": fornecimento,
        "icms": icms,
        "cofins": cofins,
        "pis": pis,
        "fatura": fatura,
    }

@pytest.mark.parametrize("consumo", CONSUMOS)
def test_calcular_fornecimento(consumo, tarifa):
    esperado = _expected_values_manual(consumo, tarifa)["fornecimento"]
    obtido = calcular_fornecimento(consumo, tarifa)
    assert round(obtido, 6) == round(esperado, 6)

@pytest.mark.parametrize("consumo", CONSUMOS)
def test_calcular_icms(consumo, tarifa):
    esperado = _expected_values_manual(consumo, tarifa)["icms"]
    obtido = calcular_icms(consumo, tarifa)
    assert round(obtido, 6) == round(esperado, 6)

@pytest.mark.parametrize("consumo", CONSUMOS)
def test_calcular_cofins(consumo, tarifa):
    esperado = _expected_values_manual(consumo, tarifa)["cofins"]
    obtido = calcular_cofins(consumo, tarifa)
    assert round(obtido, 6) == round(esperado, 6)

@pytest.mark.parametrize("consumo", CONSUMOS)
def test_calcular_pis_pasep(consumo, tarifa):
    esperado = _expected_values_manual(consumo, tarifa)["pis"]
    obtido = calcular_pis_pasep(consumo, tarifa)
    assert round(obtido, 6) == round(esperado, 6)


@pytest.mark.parametrize("consumo", CONSUMOS)
def test_calcular_fatura(consumo, tarifa):
    esperado = _expected_values_manual(consumo, tarifa)["fatura"]
    obtido = calcular_fatura(consumo, tarifa)
    assert round(obtido, 6) == round(esperado, 6)