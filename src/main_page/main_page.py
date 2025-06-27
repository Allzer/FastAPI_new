from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=["main_pages"]
)

templates = Jinja2Templates(directory='src/templates')

@router.get("/main")
def get_base_pages(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

# @router.get("/search/{operation_type}") #Если функция, которая образается к БД должна получить какой-то аргумент, то мы его указываем в декораторе
# def get_search_pages(request: Request, operations = Depends(get_specific_operations)):
#     return templates.TemplateResponse("search.html", {"request": request, "operations":operations['data']})