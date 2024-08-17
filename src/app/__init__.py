import pydantic
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session


def handle_exceptions(*, app: FastAPI):
    @app.exception_handler(pydantic.ValidationError)
    async def query_params_validation_error_handler(
        request: Request,
        exc: pydantic.ValidationError,
    ) -> Response:
        return JSONResponse(
            status_code=422,
            content={
                "detail": exc.errors(),
            },
        )
