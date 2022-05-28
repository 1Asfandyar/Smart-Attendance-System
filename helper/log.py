def debug(app, msg="a debug message"):
    app.logger.debug(msg)

def info(app, msg="an info message"):
    app.logger.info(msg)

def warning(app, msg="a warning message"):
    app.logger.warning(msg)

def error(app, msg="an error message"):
    app.logger.error(msg)