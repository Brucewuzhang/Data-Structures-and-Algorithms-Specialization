# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    worker_with_free_time = [[i, 0] for i in range(n_workers)]
    n = n_workers

    def shiftdown(i):
        min_index = i
        l_child_index = 2*i + 1
        r_child_index = 2*i + 2
        for index in [l_child_index, r_child_index]:
            if index <= n-1 and worker_with_free_time[index][1] <= worker_with_free_time[min_index][1]:
                if worker_with_free_time[index][1] < worker_with_free_time[min_index][1]:
                    min_index = index
                elif worker_with_free_time[index][0] < worker_with_free_time[min_index][0]:
                    min_index = index
        if min_index != i:
            worker_with_free_time[i], worker_with_free_time[min_index] = worker_with_free_time[min_index], worker_with_free_time[i]
            shiftdown(min_index)
    for i, job in enumerate(jobs):
        if i < n:
            result.append(AssignedJob(i, 0))
            worker_with_free_time[i][1] = job
            continue
        if i == n:
            # build min heap
            for j in range((n-2) // 2, -1, -1):
                shiftdown(j)
        result.append(AssignedJob(worker_with_free_time[0][0], worker_with_free_time[0][1]))
        worker_with_free_time[0][1] += job
        shiftdown(0)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
