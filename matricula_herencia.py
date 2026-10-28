"""
Caso práctico: sistema de matrícula UNSCH 2026-II
Versión con herencia múltiple (la que generó el reclamo).
"""


class Matricula:
    """Matrícula general: derecho base de S/ 60.00."""

    def calcular_costo(self):
        return 60.00


class Extemporanea(Matricula):
    """Recargo por matricularse fuera de fecha: + S/ 15.00."""

    def calcular_costo(self):
        return super().calcular_costo() + 15.00


class IndiceDesaprobatorio(Matricula):
    """Recargo por índice académico desaprobatorio: + S/ 15.00."""

    def calcular_costo(self):
        return super().calcular_costo() + 15.00


class BecaViolencia(Matricula):
    """Beca para afectados por la violencia sociopolítica: mitad del monto."""

    def calcular_costo(self):
        return super().calcular_costo() / 2


# Programador 1: beca, índice desaprobatorio, extemporánea
class Combinada1(BecaViolencia, IndiceDesaprobatorio, Extemporanea):
    pass


# Programador 2: índice desaprobatorio, extemporánea, beca
class Combinada2(IndiceDesaprobatorio, Extemporanea, BecaViolencia):
    pass


if __name__ == "__main__":
    print("MRO Combinada1:", [c.__name__ for c in Combinada1.__mro__])
    print("MRO Combinada2:", [c.__name__ for c in Combinada2.__mro__])
    print()
    print(f"Luis Huamaní Cárdenas (Combinada1): S/ {Combinada1().calcular_costo():.2f}")
    print(f"Rosa Ccahuana Prado   (Combinada2): S/ {Combinada2().calcular_costo():.2f}")
    print()

    # Combinar primero la matrícula general provoca un error de MRO
    try:
        class Mala(Matricula, BecaViolencia):
            pass
    except TypeError as e:
        print("TypeError:", e)
