from huey import crontab
from huey.contrib.djhuey import task, periodic_task


@task('p2')
def task_p2():
    print('task_p2')


@periodic_task('p2', crontab(minute="*"))
def periodic_task_p2():
    print('periodic_task_p2')
