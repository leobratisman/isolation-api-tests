import uuid

import allure
from httpx import Response, QueryParams

from tests.clients.http.client import HTTPTestClient, build_http_test_client
from tests.config import test_settings
from tests.schema.operations import (
    GetOperationResponseTestSchema,
    GetOperationsResponseTestSchema,
    GetOperationsQueryTestSchema
)
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes


class OperationsHTTPTestClient(HTTPTestClient):
    @allure.step("Get operations")
    def get_operations_api(self, query_params: QueryParams) -> Response:
        return self.get(APITestRoutes.OPERATIONS, params=query_params)

    @allure.step("Get operation")
    def get_operation_api(self, operation_id: uuid.UUID) -> Response:
        return self.get(f"{APITestRoutes.OPERATIONS}/{operation_id}")

    def get_operations(self, query_params: GetOperationsQueryTestSchema) -> GetOperationsResponseTestSchema:
        response = self.get_operations_api(QueryParams(**query_params.model_dump(mode="json", by_alias=True)))
        response.raise_for_status()
        return GetOperationsResponseTestSchema.model_validate_json(response.text)

    def get_operation(self, operation_id: uuid.UUID) -> GetOperationResponseTestSchema:
        response = self.get_operation_api(operation_id)
        response.raise_for_status()
        return GetOperationResponseTestSchema.model_validate_json(response.text)


def build_operations_http_test_client() -> OperationsHTTPTestClient:
    client = build_http_test_client(
        logger=get_test_logger("OPERATIONS_HTTP_TEST_CLIENT"),
        config=test_settings.operations_http_client,
    )
    return OperationsHTTPTestClient(client=client)
