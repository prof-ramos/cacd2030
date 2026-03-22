#!/bin/bash
# Script para calcular progresso do edital CACD 2030

ARQUIVO="../planejamento/edital-conteudos.md"

if [ ! -f "$ARQUIVO" ]; then
    echo "Arquivo não encontrado: $ARQUIVO"
    exit 1
fi

# Contar checkboxes
TOTAL=$(grep -o "\- \[[ x]\]" "$ARQUIVO" | wc -l)
MARCADOS=$(grep -o "\- \[x\]" "$ARQUIVO" | wc -l)
NAO_MARCADOS=$((TOTAL - MARCADOS))

# Calcular porcentagem
if [ $TOTAL -gt 0 ]; then
    PORCENTAGEM=$(echo "scale=1; ($MARCADOS * 100) / $TOTAL" | bc)
else
    PORCENTAGEM=0
fi

# Mostrar resultado
echo "========================================="
echo "📊 PROGRESSO CACD 2030"
echo "========================================="
echo ""
echo "✅ Estudados: $MARCADOS"
echo "⬜ Pendentes: $NAO_MARCADOS"
echo "📦 Total: $TOTAL"
echo ""
echo "📈 Progresso: ${PORCENTAGEM}%"
echo ""

# Barra de progresso
BARRAS_COMPLETAS=$(echo "$PORCENTAGEM / 5" | bc)
BARRAS_VAZIAS=$((20 - BARRAS_COMPLETAS))

printf "["
for ((i=0; i<BARRAS_COMPLETAS; i++)); do printf "█"; done
for ((i=0; i<BARRAS_VAZIAS; i++)); do printf "░"; done
printf "] ${PORCENTAGEM}%%\n"

echo ""
echo "========================================="

# Progresso por matéria (apenas nível 1)
echo ""
echo "📚 PROGRESSO POR MATÉRIA:"
echo "-----------------------------------------"

for materia in "LÍNGUA PORTUGUESA" "LÍNGUA INGLESA" "HISTÓRIA DO BRASIL" "HISTÓRIA MUNDIAL" "POLÍTICA INTERNACIONAL" "GEOGRAFIA" "ECONOMIA" "DIREITO" "LÍNGUA ESPANHOLA" "LÍNGUA FRANCESA"; do
    # Contar checkboxes dentro de cada seção (simplificado)
    echo "  $materia"
done

echo ""
