import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture
def driver(request):
    use_browserstack = request.config.getoption("--use-browserstack")
    driver = DriverFactory.get_driver(use_browserstack)
    yield driver
    driver.quit()

def test_example(driver):
    # Tu código de prueba aquí
    pass

if __name__ == "__main__":
    pytest.main(["--use-browserstack"])