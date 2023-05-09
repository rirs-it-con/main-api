from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="RIRS",
        description="This is a very custom OpenAPI schema",
        version="0.0.1",
        routes=app.routes
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema