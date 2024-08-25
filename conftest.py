def pytest_addoption(parser):
    parser.addoption("--use-browserstack", action="store_true", default=False, help="run the tests on BrowserStack")