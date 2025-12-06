
TARIFA_KWH = 0.28172

def calcular_fornecimento(consumo_kwh: float, tarifa: float = TARIFA_KWH) -> float:
  
    return consumo_kwh * tarifa

def _fatores_por_consumo(consumo_kwh: float):
    if consumo_kwh <= 200:
        icms_factor = 0.136363
        cofins_factor = 0.0614722
        pis_factor = 0.013346
    else:
        icms_factor = 0.333333
        cofins_factor = 0.0730751
        pis_factor = 0.0158651
    return icms_factor, cofins_factor, pis_factor

def calcular_icms(consumo_kwh: float, tarifa: float = TARIFA_KWH) -> float:
    fornecimento = calcular_fornecimento(consumo_kwh, tarifa)
    icms_factor, _, _ = _fatores_por_consumo(consumo_kwh)
    return icms_factor * fornecimento

def calcular_cofins(consumo_kwh: float, tarifa: float = TARIFA_KWH) -> float:
    fornecimento = calcular_fornecimento(consumo_kwh, tarifa)
    _, cofins_factor, _ = _fatores_por_consumo(consumo_kwh)
    return cofins_factor * fornecimento

def calcular_pis_pasep(consumo_kwh: float, tarifa: float = TARIFA_KWH) -> float:
    fornecimento = calcular_fornecimento(consumo_kwh, tarifa)
    _, _, pis_factor = _fatores_por_consumo(consumo_kwh)
    return pis_factor * fornecimento

def calcular_icms_cofins(consumo_kwh: float, tarifa: float = TARIFA_KWH) -> float:
    fornecimento = calcular_fornecimento(consumo_kwh, tarifa)
    icms_factor, cofins_factor, _ = _fatores_por_consumo(consumo_kwh)
    return icms_factor * cofins_factor * fornecimento

def calcular_icms_pis_pasep(consumo_kwh: float, tarifa: float = TARIFA_KWH) -> float:

    fornecimento = calcular_fornecimento(consumo_kwh, tarifa)
    icms_factor, _, pis_factor = _fatores_por_consumo(consumo_kwh)
    return icms_factor * pis_factor * fornecimento

def calcular_fatura(consumo_kwh: float, tarifa: float = TARIFA_KWH) -> float:
    fornecimento = calcular_fornecimento(consumo_kwh, tarifa)
    icms = calcular_icms(consumo_kwh, tarifa)
    cofins = calcular_cofins(consumo_kwh, tarifa)
    pis = calcular_pis_pasep(consumo_kwh, tarifa)
    icms_cofins = calcular_icms_cofins(consumo_kwh, tarifa)
    icms_pis = calcular_icms_pis_pasep(consumo_kwh, tarifa)
    return fornecimento + icms + cofins + pis + icms_cofins + icms_pis

class EnergiaCalculator:
    def __init__(self, tarifa: float = TARIFA_KWH):
        self.tarifa = tarifa

    def fornecimento(self, consumo_kwh: float) -> float:
        return calcular_fornecimento(consumo_kwh, self.tarifa)

    def icms(self, consumo_kwh: float) -> float:
        return calcular_icms(consumo_kwh, self.tarifa)

    def cofins(self, consumo_kwh: float) -> float:
        return calcular_cofins(consumo_kwh, self.tarifa)

    def pis_pasep(self, consumo_kwh: float) -> float:
        return calcular_pis_pasep(consumo_kwh, self.tarifa)

    def icms_cofins(self, consumo_kwh: float) -> float:
        return calcular_icms_cofins(consumo_kwh, self.tarifa)

    def icms_pis_pasep(self, consumo_kwh: float) -> float:
        return calcular_icms_pis_pasep(consumo_kwh, self.tarifa)

    def fatura(self, consumo_kwh: float) -> float:
        return calcular_fatura(consumo_kwh, self.tarifa)

        