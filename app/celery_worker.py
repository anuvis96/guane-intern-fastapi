from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
from celery.result import AsyncResult
# Initialize celery
celery = Celery('tasks', broker='https://127.0.0.1:8000', backend='https://127.0.0.1:8000')
# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)
# Create Order - Run Asynchronously with celery
# Example process of long running task
@celery.task
def create_order_dog(name):
    
    # 5 seconds per 1 order
    complete_time_per_function= 20 
    sleep(complete_time_per_function)

# Display log    
    celery_log.info(f"Order Complete!")
    return {"message": f"Hi {name}, Your order has completed!"}