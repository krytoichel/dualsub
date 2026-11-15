from fastapi import FastAPI

app = FastAPI(
    title="DualSub",
    description="Сервис для просмотра видео с двумя дорожками субтитров",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "DualSub",
    }