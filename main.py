import os
# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration

from app import create_app


env = os.getenv("FLASK_ENV")
app = create_app(env)

app.run()
# sentry_sdk.init(
#     dsn="https://9620404d04c94f4aaa3b08244641c14b@o1003000.ingest.sentry.io/5963353",
#     integrations=[FlaskIntegration()],
#     traces_sample_rate=1.0,
# )