"""
Caso práctico: sistema de matrícula UNSCH 2026-II
Rediseño con composición: el orden de los cobros es explícito.
"""


class Regla:
    nombre = "regla"

    def aplicar(self, monto):
        raise NotImplementedError


class Extemporanea(Regla):
    nombre = "Recargo por matrícula extemporánea"

    def aplicar(self, monto):
        return monto + 15.00


class IndiceDesaprobatorio(Regla):
    nombre = "Recargo por índice desaprobatorio"

    def aplicar(self, monto):
        return monto + 15.00


class BecaViolencia(Regla):
    nombre = "Beca por violencia sociopolítica"

    def aplicar(self, monto):
        return monto / 2


class Matricula:
    DERECHO_BASE = 60.00

    def __init__(self, reglas=None):
        self.reglas = reglas or []  # el orden de aplicación es explícito

    def calcular_costo(self):
        monto = self.DERECHO_BASE
        for regla in self.reglas:
            monto = regla.aplicar(monto)
        return monto

    def detalle(self):
        monto = self.DERECHO_BASE
        lineas = [f"Derecho base: S/ {monto:.2f}"]
        for regla in self.reglas:
            monto = regla.aplicar(monto)
            lineas.append(f"{regla.nombre}: S/ {monto:.2f}")
        return "\n".join(lineas)


if __name__ == "__main__":
    # Beca DESPUÉS de los recargos: (60 + 15 + 15) / 2 = 45
    m1 = Matricula([Extemporanea(), IndiceDesaprobatorio(), BecaViolencia()])
    # Beca ANTES de los recargos: 60 / 2 + 15 + 15 = 60
    m2 = Matricula([BecaViolencia(), Extemporanea(), IndiceDesaprobatorio()])

    print("Beca al final (criterio recomendado):")
    print(m1.detalle())
    print()
    print("Beca al inicio:")
    print(m2.detalle())
