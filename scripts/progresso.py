#!/usr/bin/env python3
"""
Calculador de progresso do edital CACD 2030.
Conta checkboxes marcados vs total, por matéria e geral.
"""

import re
from pathlib import Path

ARQUIVO = Path(__file__).parent.parent / "planejamento" / "edital-conteudos.md"


def calcular_progresso():
    """Lê o arquivo e calcula progresso geral e por matéria."""

    if not ARQUIVO.exists():
        print(f"❌ Arquivo não encontrado: {ARQUIVO}")
        return

    conteudo = ARQUIVO.read_text(encoding="utf-8")

    # Encontrar todas as seções (## MATÉRIA)
    secoes = re.split(r"\n## (.+?)\n", conteudo)

    # secoes = ['', 'LÍNGUA PORTUGUESA', 'conteúdo...', 'LÍNGUA INGLESA', 'conteúdo...']
    progresso = {}

    for i in range(1, len(secoes), 2):
        if i + 1 < len(secoes):
            header = secoes[i].strip()
            corpo = secoes[i + 1]

            # Contar checkboxes
            total = len(re.findall(r"- \[[ x]\]", corpo))
            marcados = len(re.findall(r"- \[x\]", corpo))

            if total > 0:
                porcentagem = (marcados / total) * 100
            else:
                porcentagem = 0

            progresso[header] = {
                "total": total,
                "marcados": marcados,
                "porcentagem": porcentagem,
            }

    # Calcular total geral
    total_geral = sum(m["total"] for m in progresso.values())
    marcados_geral = sum(m["marcados"] for m in progresso.values())
    porcentagem_geral = (marcados_geral / total_geral * 100) if total_geral > 0 else 0

    # Exibir resultados
    print("\n" + "=" * 55)
    print("📊 PROGRESSO CACD 2030")
    print("=" * 55)
    print()
    print(f"✅ Estudados: {marcados_geral}")
    print(f"⬜ Pendentes: {total_geral - marcados_geral}")
    print(f"📦 Total: {total_geral}")
    print()
    print(f"📈 Progresso Geral: {porcentagem_geral:.1f}%")

    # Barra de progresso
    barras = int(porcentagem_geral / 5)
    print()
    print("[" + "█" * barras + "░" * (20 - barras) + f"] {porcentagem_geral:.1f}%")
    print()

    print("=" * 55)
    print("📚 PROGRESSO POR MATÉRIA")
    print("=" * 55)
    print()

    # Ordenar por nome
    for materia, dados in sorted(progresso.items()):
        if dados["total"] > 0:
            barras = int(dados["porcentagem"] / 5)
            # Nome truncado para alinhamento
            nome = materia[:30].ljust(30)
            print(
                f"{nome} [{'█' * barras + '░' * (20 - barras)}] {dados['porcentagem']:5.1f}% ({dados['marcados']}/{dados['total']})"
            )

    print()
    print("=" * 55)
    print()


if __name__ == "__main__":
    calcular_progresso()
