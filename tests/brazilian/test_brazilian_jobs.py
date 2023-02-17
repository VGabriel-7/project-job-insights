from src.pre_built.brazilian_jobs import read_brazilian_file


keys_english = ['title', 'salary', 'type']

path = 'tests/mocks/brazilians_jobs.csv'


def test_brazilian_jobs():
    returned_keys = read_brazilian_file(path)
    for key in keys_english:
        for returned_key in returned_keys:
            assert key in returned_key
