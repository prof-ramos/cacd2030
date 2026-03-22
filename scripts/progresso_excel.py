#!/usr/bin/env python3
"""
Lê o checklist Excel do CACD 2030 e mostra progresso.
O Excel é a fonte de verdade - edite diretamente nele.

Como usar:
1. Abra recursos/CACD2026_checklist.xlsx
2. Marque 'x' na coluna D (Estudado) para tópicos estudados
3. Salve o arquivo
4. Rode este script ou pergunte ao James "qual meu progresso no CACD?"
"""

import openpyxl
from pathlib import Path

EXCEL_PATH = Path(__file__).parent.parent / "recursos" / "CACD2026_checklist.xlsx"

# Disciplinas: (linha_inicial_itens, linha_final_itens, total_esperado)
# Baseado na estrutura real do Excel
DISCIPLINAS = {
    "LÍNGUA PORTUGUESA": (3, 21, 19),
    "LÍNGUA INGLESA": (23, 26, 4),
    "HISTÓRIA DO BRASIL": (28, 89, 62),
    "HISTÓRIA MUNDIAL": (91, 157, 67),
    "POLÍTICA INTERNACIONAL": (159, 200, 42),
    "GEOGRAFIA": (202, 231, 30),
    "ECONOMIA": (233, 341, 109),
    "DIREITO": (343, 413, 71),
    "LÍNGUA ESPANHOLA": (415, 416, 2),
    "LÍNGUA FRANCESA": (418, 419, 2),
}


def contar_estudados(ws, inicio, fim):
    """Conta células marcadas como estudadas na coluna D."""
    count = 0
    for row in range(inicio, fim + 1):
        valor = ws.cell(row=row, column=4).value  # Coluna D = "Estudado"
        if valor:
            valor_str = str(valor).strip().lower()
            if valor_str in ["x", "1", "true", "sim", "✓", "yes", "s"]:
                count += 1
    return count


def mostrar_progresso():
    """Lê o Excel e mostra progresso por matéria."""

    if not EXCEL_PATH.exists():
        print(f"❌ Arquivo não encontrado: {EXCEL_PATH}")
        return

    wb = openpyxl.load_workbook(EXCEL_PATH)
    ws = wb["Checklist CACD 2026"]

    print("\n" + "=" * 65)
    print("📊 PROGRESSO CACD 2030 (via Excel)")
    print("=" * 65)
    print()

    total_geral = 0
    estudados_geral = 0
    resultados = []

    for nome, (inicio, fim, total) in DISCIPLINAS.items():
        estudados = contar_estudados(ws, inicio, fim)
        pct = (estudados / total * 100) if total > 0 else 0
        barras = int(pct / 5)

        resultados.append({
            "nome": nome,
            "estudados": estudados,
            "total": total,
            "pct": pct,
            "barras": barras
        })

        total_geral += total
        estudados_geral += estudados

    # Mostrar resultados ordenados por % (decrescente)
    for r in sorted(resultados, key=lambda x: x["pct"], reverse=True):
        nome = r["nome"][:30].ljust(30)
        barra = '█' * r["barras"] + '░' * (20 - r["barras"])
        print(f"{nome} [{barra}] {r['pct']:5.1f}% ({r['estudados']}/{r['total']})")

    print()
    pct_geral = (estudados_geral / total_geral * 100) if total_geral > 0 else 0
    barras = int(pct_geral / 5)
    barra = '█' * barras + '░' * (20 - barras)

    print("=" * 65)
    print(f"📈 TOTAL GERAL:    [{barra}] {pct_geral:.1f}%")
    print(f"   {estudados_geral} de {total_geral} tópicos estudados")
    print("=" * 65)
    print()

    wb.close()


if __name__ == "__main__":
    mostrar_progresso()
