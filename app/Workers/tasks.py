from time import sleep
from app.celery_worker import celery
from celery.result import AsyncResult

# Crear Orden - Corriendo de manera asincrona con celery


@celery.task
def create_order_dog(name):
    # 5 seconds per 1 order
    complete_time_per_function = 6
    sleep(complete_time_per_function)
    return {"message": f"Hi {name}, Your order has completed!"}
