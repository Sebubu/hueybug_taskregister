# hueybug_taskregister
Shows a bug in huey with the global task register

## Run

```bash
git clone https://github.com/Sebubu/hueybug_taskregister.git
cd hueybug_taskregister
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py run_huey -qu p1
```

## Bug
Due to the global TaskRegistry, all tasks are registered at one place 
without the distinction which huey instance was used to decorate the method.

As soon as a consumer is started (in this specific case p1), 
all periodic tasks are scheduled, even the one of another huey instance.
```text
python manage.py run_huey -qu p1

Output:
INFO:huey.consumer:The following commands are available:
+ periodic_task_p2
+ task_p2
+ periodic_task_p1
+ task_p1
```
