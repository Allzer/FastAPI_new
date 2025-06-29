from fastapi import APIRouter, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=["main_pages"]
)

@router.get("/")
async def get_base_pages(request: Request):
    return await 'Главаня страница'

# templates.TemplateResponse(
#         "main.html", 
#         {
#             "request": request,
#             "title": "Главная | Мир Книг"  # Добавлен заголовок
#         }
#     )

# @router.get("/search/{operation_type}") #Если функция, которая образается к БД должна получить какой-то аргумент, то мы его указываем в декораторе
# def get_search_pages(request: Request, operations = Depends(get_specific_operations)):
#     return templates.TemplateResponse("search.html", {"request": request, "operations":operations['data']})