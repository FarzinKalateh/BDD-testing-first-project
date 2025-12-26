def before_scenario(context, scenario):
    context.driver = None

def after_scenario(context, scenario):
    if context.driver:
        context.driver.quit()
