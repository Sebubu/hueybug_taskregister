# hueybug_taskregister
Shows a bug in huey with the global task register

## Prepare to run

```bash
git clone https://github.com/Sebubu/hueybug_taskregister.git
cd hueybug_taskregister
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Bug
Due to the global TaskRegistry, all tasks are registered at one place 
without the distinction which huey instance was used to decorate the method.

```python
# simple_example.py
from huey import RedisHuey, crontab


huey1 = RedisHuey('app1', host='localhost')
huey2 = RedisHuey('app2', host='localhost')


@huey1.periodic_task(crontab(minute="*"))
def periodic_task_1():
    print(periodic_task_1)


@huey2.periodic_task(crontab(minute="*"))
def periodic_task_2():
    print(periodic_task_2)
```

```bash
# Run the consumer
huey_consumer.py simple_example.huey1

# Output:
[2017-06-27 14:20:16,654] INFO:huey.consumer:MainThread:Huey consumer started with 1 thread, PID 9046
[2017-06-27 14:20:16,654] INFO:huey.consumer:MainThread:Scheduler runs every 1 seconds.
[2017-06-27 14:20:16,654] INFO:huey.consumer:MainThread:Periodic tasks are enabled.
[2017-06-27 14:20:16,654] INFO:huey.consumer:MainThread:UTC is enabled.
[2017-06-27 14:20:16,654] INFO:huey.consumer:MainThread:The following commands are available:
+ periodic_task_2
+ periodic_task_1
```
Thus both periodic tasks are executed although only one is associated with the huey1 instance.

