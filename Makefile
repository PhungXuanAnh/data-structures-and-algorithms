test-sort:
	.python3/bin/python -m tests.sorting_test
test-search:
	.python3/bin/python -m tests.searching_test
clean-python-cache:
	py3clean .
