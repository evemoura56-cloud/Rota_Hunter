from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database.session import Base, engine
from backend.src.common.config import get_settings
from backend.src.auth.routes import router as auth_router
from backend.src.hunter.routes import router as hunter_router
from backend.src.crm.routes import router as crm_router
from backend.src.engagement.routes import router as engagement_router
from backend.src.ia.routes import router as ia_router
from backend.src.forms.routes import router as forms_router
from backend.src.whatsapp.routes import router as whatsapp_router

settings = get_settings()
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_nome, version="1.0.0", description="Plataforma local de inteligencia comercial")
origins = [settings.frontend_url] if settings.frontend_url else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(hunter_router)
app.include_router(crm_router)
app.include_router(engagement_router)
app.include_router(ia_router)
app.include_router(forms_router)
app.include_router(whatsapp_router)


@app.get("/")
def raiz():
    return {"mensagem": "Rota Hunter 1.0 online"}
