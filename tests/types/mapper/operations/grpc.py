from protos.gen.contracts.services.operations.operation_pb2 import (
    OperationStatus,
    OperationType
)
from tests.types.operations import OperationTestType, OperationTestStatus

OPERATION_TYPE_MAP = {
    OperationTestType.BILL_PAYMENT: OperationType.OPERATION_TYPE_BILL_PAYMENT,
    OperationTestType.CASH_WITHDRAWAL: OperationType.OPERATION_TYPE_CASH_WITHDRAWAL,
    OperationTestType.CASHBACK: OperationType.OPERATION_TYPE_CASHBACK,
    OperationTestType.FEE: OperationType.OPERATION_TYPE_FEE,
    OperationTestType.PURCHASE: OperationType.OPERATION_TYPE_PURCHASE,
    OperationTestType.REVERSAL: OperationType.OPERATION_TYPE_REVERSAL,
    OperationTestType.TOP_UP: OperationType.OPERATION_TYPE_TOP_UP,
    OperationTestType.TRANSFER: OperationType.OPERATION_TYPE_TRANSFER,
    OperationTestType.UNSPECIFIED: OperationType.OPERATION_TYPE_UNSPECIFIED
}

OPERATION_STATUS_MAP = {
    OperationTestStatus.COMPLETED: OperationStatus.OPERATION_STATUS_COMPLETED,
    OperationTestStatus.FAILED: OperationStatus.OPERATION_STATUS_FAILED,
    OperationTestStatus.IN_PROGRESS: OperationStatus.OPERATION_STATUS_IN_PROGRESS,
    OperationTestStatus.REVERSED: OperationStatus.OPERATION_STATUS_REVERSED,
    OperationTestStatus.UNSPECIFIED: OperationStatus.OPERATION_STATUS_UNSPECIFIED
}


def map_operation_type(enum: OperationTestType) -> OperationType:
    return OPERATION_TYPE_MAP.get(enum)


def map_operation_status(enum: OperationTestStatus) -> OperationStatus:
    return OPERATION_STATUS_MAP.get(enum)