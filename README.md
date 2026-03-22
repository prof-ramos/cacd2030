# CACD 2030

Planejamento de estudos para aprovação no Concurso de Admissão à Carreira de Diplomata.

## Meta

**Aprovação até 2030**

## Estrutura

```
cacd2030/
├── README.md
├── planejamento/
│   ├── edital-conteudos.md    # Checklist completo do edital 2026
│   ├── cronograma.md          # Cronograma de estudos
│   ├── materias.md            # Matérias por fase e prioridade
│   └── metas.md               # Metas e métricas
├── notas/
│   └── ...                    # Notas de estudo por matéria
└── recursos/
    └── ...                    # Materiais, PDFs, referências
```

## Fases do Concurso

1. **Primeira Fase** - Provas Objetivas
2. **Segunda Fase** - Provas Escritas
3. **Terceira Fase** - Exame Médico
4. **Quarta Fase** - Avaliação Psicológica
5. **Quinta Fase** - Prova Oral
6. **Sexta Fase** - Curso de Formação

## Matérias (1ª e 2ª Fases)

- Língua Portuguesa
- Língua Inglesa
- Língua Espanhola (2ª fase)
- Língua Francesa (2ª fase)
- História do Brasil
- História Mundial
- Política Internacional
- Geografia
- Economia
- Direito

## Status

🚧 Em planejamento

## Como Usar

### Marcar Progresso

**Opção 1: Excel (recomendado)**
1. Abra `recursos/CACD2026_checklist.xlsx`
2. Marque `x` na coluna **D (Estudado)** para tópicos estudados
3. Salve o arquivo

**Opção 2: Markdown**
1. Edite `planejamento/edital-conteudos.md`
2. Troque `- [ ]` → `- [x]` nos tópicos estudados

### Ver Progresso

Peça ao James: **"qual meu progresso no CACD?"**

Ou rode manualmente:
```bash
cd cacd2030/scripts
python3 progresso_excel.py  # Lê do Excel
python3 progresso.py        # Lê do Markdown
```

## Links Úteis

- [Edital CACD 2026](https://www.cespe.unb.br/concursos/cacd_2026/)
- [Conteúdos Programáticos](./planejamento/edital-conteudos.md)
- [Metas](./planejamento/metas.md)
