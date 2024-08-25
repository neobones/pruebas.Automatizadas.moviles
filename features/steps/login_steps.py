from behave import given, when, then

@given('the app is launched')
def step_impl(context):
    context.driver.launch_app()

@when('I enter username "{username}"')
def step_impl(context, username):
    context.driver.find_element_by_id('username_field').send_keys(username)

@when('I enter password "{password}"')
def step_impl(context, password):
    context.driver.find_element_by_id('password_field').send_keys(password)

@when('I tap the login button')
def step_impl(context):
    context.driver.find_element_by_id('login_button').click()

@then('I should see the home screen')
def step_impl(context):
    assert context.driver.find_element_by_id('home_screen').is_displayed()