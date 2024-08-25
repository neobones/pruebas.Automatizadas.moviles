from utils.driver_factory import DriverFactory

def before_scenario(context, scenario):
    use_browserstack = context.config.userdata.getbool('browserstack', False)
    context.driver = DriverFactory.get_driver(use_browserstack)

def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()