from pathlib import Path
from typing import Any

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

from backend.schemas.ia import TreinoRequest, PredicaoRequest, PredicaoResponse
from backend.src.common.config import get_settings

settings = get_settings()


class ModeloIAService:
    def __init__(self) -> None:
        self.caminho = Path(settings.caminho_modelo_ia)
        self.modelo = None
        if self.caminho.exists():
            self.modelo = joblib.load(self.caminho)

    def _extrair_features(self, item: dict[str, Any]) -> list[float]:
        mapa_setor = {
            "Tecnologia": 1.0,
            "Servicos": 0.8,
            "Industria": 0.6,
        }
        mapa_status = {
            "PROSPECTADO": 0.1,
            "CONTATADO": 0.2,
            "RESPONDEU": 0.3,
            "QUALIFICADO": 0.5,
            "PROPOSTA": 0.7,
            "GANHO": 0.9,
            "PERDIDO": 0.05,
        }
        return [
            mapa_setor.get(item.get("setor"), 0.4),
            item.get("interacoes", 0),
            item.get("tempo_resposta_horas", 0),
            mapa_status.get(item.get("status_pipeline"), 0.1),
            item.get("abertura_email", 0),
        ]

    def treinar(self, payload: TreinoRequest) -> str:
        if not payload.dados:
            raise ValueError("Dados insuficientes")
        X = np.array([self._extrair_features(d.model_dump()) for d in payload.dados])
        y = np.array([d.ganho for d in payload.dados])
        modelo = LogisticRegression(max_iter=1000)
        modelo.fit(X, y)
        self.caminho.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(modelo, self.caminho)
        self.modelo = modelo
        return "Modelo treinado"

    def prever(self, payload: PredicaoRequest) -> PredicaoResponse:
        if not self.modelo:
            raise ValueError("Modelo nao treinado")
        features = np.array([self._extrair_features(payload.model_dump())])
        prob = float(self.modelo.predict_proba(features)[0][1])
        fatores = [
            f"Setor influencia {features[0][0]:.2f}",
            f"Interacoes: {payload.interacoes}",
            f"Etapa atual: {payload.status_pipeline}",
        ]
        motivo = "Maior probabilidade" if prob >= 0.5 else "Risco de perda"
        return PredicaoResponse(p_win=round(prob, 2), motivo_principal=motivo, fatores=fatores)
