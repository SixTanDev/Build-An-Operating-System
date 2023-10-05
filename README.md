# Awesome Async Adventures - build-an-Operating-System 🚀

Welcome to the Awesome Async Adventures repository! 🎉 

Are you ready to dive into the world of multitasking, coroutines, and async magic? This repository is your gateway to understanding how multitasking can be achieved using a single thread and the power of coroutines. 🧙‍♂️

# Running in Docker 🐳
To run this project in a Docker container, you can use the provided Makefile. Here are some useful commands:

| Detail command                       |      Command      |
|------------------------------------- |:-----------------:|
| Build the Docker image               |  sudo make build  |
| Run the Docker container             |    make run       |
| Start an existing container          | make start        |
| Stop an existing container           | make stop         |
| Restart the container                | make restart      |
| Interact with the running container  | make interact     |
| Delete the container and image       | make delete       |
| Delete only the container            | make delete_cnt   |


# Using Poetry for Development 📝
You can also set up a development environment using Poetry. Here are the steps to install Poetry and create your environment:

Install Poetry (if not already installed):

1. curl -sSL https://install.python-poetry.org | python -
2. poetry install
3. poetry shell

## NOTE:
If you're using the Poetry environment and encounter **IMPORT ERRORS** when running the examples, whether in debug or normal mode using the python ```examples/example0.py``` command, you may need to configure the ```PYTHONPATH``` environment variable to point to the location where you have cloned the repository.

For instance, if you have cloned the repository in the ```Download``` folder, you can set the ```PYTHONPATH``` as follows in a Linux environment:

```export PYTHONPATH=/Users/my_user/Downloads/Build-An-Operating-System```


## What's Inside? 📦

Inside this repository, you'll find an exhilarating journey through the heart of multitasking and asynchronous programming. We've got a bunch of cool classes and examples to help you grasp these concepts:

### Scheduler 🔄

The `Scheduler` class is your guide to orchestrating tasks like a maestro! It lets you create, schedule, and execute tasks based on coroutines. Imagine managing multiple tasks with a single thread! 😮

```
# Create an instance of the Scheduler
sched = Scheduler()

# Create tasks using coroutines
sched.create_task(task=coroutine_1())
sched.create_task(task=coroutine_2())

# Let the event loop begin!
sched.run_event_loop()
```

### System Calls 📞
Ever wanted to control the CPU's attention like a magician's sleight of hand? Introducing the System Calls – the secret spells that allow tasks to communicate and share CPU time. We've got GetTid, NewTask, KillTask, and even a WaitTask to keep things thrilling! 🎩✨

```
# Launch a new task with GetTid and NewTask
child = yield NewTask(coroutine())

# Simulate task interactions and terminate tasks with KillTask
for i in range(5):
    yield
yield KillTask(child)
```

### Task Class 🏃‍♂️
Meet the Task class – your dynamic duo partner for coroutines! It wraps your coroutines, letting you manage and control their execution. 🦸‍♀️

```
# Create a task with a coroutine
task_1 = Task(coroutine=coroutine())
task_1.run()
```

How Does it Relate to the GIL? 🐍
This adventure is closely tied to the Global Interpreter Lock (GIL) in CPython. By mastering coroutines, system calls, and scheduling, you'll unlock the secrets of maximizing CPU utilization and crafting responsive applications.

Get ready to unleash your Python multitasking prowess and conquer the async world! 🎮🌐

Let the Adventure Begin! 🌟
Are you ready to embark on an epic journey through the realms of coroutines, multitasking, and the async universe? Clone this repository, run the examples, and prepare to be amazed! 🚀🔥

Feel free to explore the code, try out different scenarios, and level up your async skills. If you have questions or insights, don't hesitate to share them – we're all on this adventure together! 💬🤝

Happy coding and multitasking!


**I hope this README inspires and motivates you to explore and learn more about the exciting world of asynchronous programming and multitasking! 🚀🌟**
**With this foundation, you'll find it much easier to grasp the intricacies of the asyncio library, as this implementation provides a rudimentary understanding of the fundamental concepts underlying asyncio. 📚🔍**

