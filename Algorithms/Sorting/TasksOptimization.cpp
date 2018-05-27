/**
 * A worker has a set of N tasks to complete. For each task the worker knows the time in minutes it will take to complete. This is dependent on the difficulty of the task. So, a task with difficulty D takes D minutes to complete. The worker has a limited amount of time T during which he wants to complete as many tasks as possible.

As mentioned above the tasks have different difficulty and when switching from one task to another with difficulties D1 and D2, the worker needs |D1 - D2| minutes to prepare for working on the next task.

The number of tasks N is in the range [1, 10,000]. The total time T is in the range [0, 200,000,000]. The task difficulties are integer numbers in the range [1, 10,000].

You need to write a function, which computes the maximum number of tasks that can be completed within the given time T. The function accepts as arguments the number N and T and a list of the task difficulties. It must return one integer - the maximum number of tasks that can be completed within the given time limit.

 *
 *
 */


