from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    events = ["Dhurandhar 2", "Concert", "Comedy Show"]
    return templates.TemplateResponse(
        name="index.html",
        request=request,
        context = {"events": events}
    )

# @app.get("/book", response_class=HTMLResponse)
# def book_page(request: Request, event: str):
#     return templates.TemplateResponse(
#         "booking.html",
#         {
#             "request": request,
#             "event": event
#         }
#     )

# @app.post("/book", response_class=HTMLResponse)
# def book_ticket(
#     request: Request,
#     name: str = Form(...),
#     tickets: int = Form(...),
#     event: str = Form(...)
# ):
#     return templates.TemplateResponse(
#         "success.html",
#         {
#             "request": request,
#             "name": name,
#             "tickets": tickets,
#             "event": event
#         }
#     )