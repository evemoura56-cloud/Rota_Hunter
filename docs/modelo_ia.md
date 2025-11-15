# Modelo IA Comercial

- **Algoritmo**: LogisticRegression (scikit-learn)
- **Features**: setor, interacoes, tempo de resposta, etapa do funil, abertura de email.
- **Output**: `p_win` (0-1), motivo principal, lista de fatores.
- **Treino**: enviar payload `TreinoRequest` com registros historicos (campos em PT-BR).
- **Arquivo**: salvo em `database/modelo_ia.pkl` para uso local e versionavel.
- **Scripts**:
  - `python train_ia.py` - treina utilizando dataset de exemplo.
  - `python seed_db.py` - garante dados coerentes para gerar features.
