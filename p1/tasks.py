from huey import crontab
from huey.contrib.djhuey import task, periodic_task


@task('p1')
def task_p1():
    print('task_p1')


@periodic_task('p1', crontab(minute="*"))
def periodic_task_p1():
    print('periodic_task_p1')
