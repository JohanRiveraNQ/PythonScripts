import sys
import os
import csv
import pytest # type: ignore

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from user import User

@pytest.fixture
def test_data():
    test_cases = []
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_data.csv'))
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_cases.append(row)
    return test_cases

def test_login(test_data):
    for data in test_data:
        user = User(data['username'], data['password'])
        assert user.login(data['entered_password']) == (data['expected_result'] == 'True')

def test_logout():
    user = User("test_user", "test_password")
    user.login("test_password")
    user.logout()
    assert not user.is_logged_in
