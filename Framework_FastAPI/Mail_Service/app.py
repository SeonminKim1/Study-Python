import uvicorn
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

from send_email import send_email_background, send_email_async

app = FastAPI()

class Mail(BaseModel):
    subject:str
    message:str
    recipient:list = None

@app.post('/mail/api')
async def send_email_asynchronous(mail:Mail):
    await send_email_async(
        subject = mail.subject,
        email_list = mail.recipient,
        body = mail.message,
    )
    return 'Success'

@app.post('/mail/api/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks, mail:Mail):
    send_email_background(
        background_tasks = background_tasks, 
        subject = mail.subject,
        email_list = mail.recipient,
        body = mail.message,
    )
    return 'Success'

if __name__ == '__main__':
    uvicorn.run('app:app', reload=True)