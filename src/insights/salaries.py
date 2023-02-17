from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    salaries = [
        int(job['max_salary']) for job in
        read(path) if job['max_salary'].isnumeric()
    ]

    max_salary = 0
    for salary in salaries:
        max_salary = salary if max_salary < salary else max_salary

    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    salaries = [
        int(job['min_salary']) for job in
        read(path) if job['min_salary'].isnumeric()
    ]

    min_salary = salaries[0]
    for salary in salaries:
        min_salary = salary if min_salary > salary else min_salary

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError
    if (
        not str(job['min_salary']).isnumeric() and
        not str(job['max_salary']).isnumeric()
    ):
        raise ValueError
    if int(str(job['min_salary'])) > int(str(job['max_salary'])):
        raise ValueError
    if not str(salary).replace('-', '').isnumeric():
        raise ValueError

    return int(str(job['min_salary'])) <= int(str(salary)) <= \
        int(str(job['max_salary']))


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
