from fastapi import APIRouter
from atleta.contoller import router as atleta
from categoria.controller import router as categoria
from centro_treinamento.controller import router as centro_treinamento

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])
api_router.include_router(categoria, prefix='/categorias', tags=['categorias'])
api_router.include_router(centro_treinamento, prefix='/centro_treinamento', tags=['centros_treinamento'])