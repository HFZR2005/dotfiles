def lookup(code: str, _cache: dict[str, str] = {}) -> str: ...

CLASS_SUCCESSFUL_COMPLETION: str
CLASS_WARNING: str
CLASS_NO_DATA: str
CLASS_SQL_STATEMENT_NOT_YET_COMPLETE: str
CLASS_CONNECTION_EXCEPTION: str
CLASS_TRIGGERED_ACTION_EXCEPTION: str
CLASS_FEATURE_NOT_SUPPORTED: str
CLASS_INVALID_TRANSACTION_INITIATION: str
CLASS_LOCATOR_EXCEPTION: str
CLASS_INVALID_GRANTOR: str
CLASS_INVALID_ROLE_SPECIFICATION: str
CLASS_DIAGNOSTICS_EXCEPTION: str
CLASS_CASE_NOT_FOUND: str
CLASS_CARDINALITY_VIOLATION: str
CLASS_DATA_EXCEPTION: str
CLASS_INTEGRITY_CONSTRAINT_VIOLATION: str
CLASS_INVALID_CURSOR_STATE: str
CLASS_INVALID_TRANSACTION_STATE: str
CLASS_INVALID_SQL_STATEMENT_NAME: str
CLASS_TRIGGERED_DATA_CHANGE_VIOLATION: str
CLASS_INVALID_AUTHORIZATION_SPECIFICATION: str
CLASS_DEPENDENT_PRIVILEGE_DESCRIPTORS_STILL_EXIST: str
CLASS_INVALID_TRANSACTION_TERMINATION: str
CLASS_SQL_ROUTINE_EXCEPTION: str
CLASS_INVALID_CURSOR_NAME: str
CLASS_EXTERNAL_ROUTINE_EXCEPTION: str
CLASS_EXTERNAL_ROUTINE_INVOCATION_EXCEPTION: str
CLASS_SAVEPOINT_EXCEPTION: str
CLASS_INVALID_CATALOG_NAME: str
CLASS_INVALID_SCHEMA_NAME: str
CLASS_TRANSACTION_ROLLBACK: str
CLASS_SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION: str
CLASS_WITH_CHECK_OPTION_VIOLATION: str
CLASS_INSUFFICIENT_RESOURCES: str
CLASS_PROGRAM_LIMIT_EXCEEDED: str
CLASS_OBJECT_NOT_IN_PREREQUISITE_STATE: str
CLASS_OPERATOR_INTERVENTION: str
CLASS_SYSTEM_ERROR: str
CLASS_SNAPSHOT_FAILURE: str
CLASS_CONFIGURATION_FILE_ERROR: str
CLASS_FOREIGN_DATA_WRAPPER_ERROR: str
CLASS_PL_PGSQL_ERROR: str
CLASS_INTERNAL_ERROR: str
SUCCESSFUL_COMPLETION: str
WARNING: str
NULL_VALUE_ELIMINATED_IN_SET_FUNCTION: str
STRING_DATA_RIGHT_TRUNCATION_: str
PRIVILEGE_NOT_REVOKED: str
PRIVILEGE_NOT_GRANTED: str
IMPLICIT_ZERO_BIT_PADDING: str
DYNAMIC_RESULT_SETS_RETURNED: str
DEPRECATED_FEATURE: str
NO_DATA: str
NO_ADDITIONAL_DYNAMIC_RESULT_SETS_RETURNED: str
SQL_STATEMENT_NOT_YET_COMPLETE: str
CONNECTION_EXCEPTION: str
SQLCLIENT_UNABLE_TO_ESTABLISH_SQLCONNECTION: str
CONNECTION_DOES_NOT_EXIST: str
SQLSERVER_REJECTED_ESTABLISHMENT_OF_SQLCONNECTION: str
CONNECTION_FAILURE: str
TRANSACTION_RESOLUTION_UNKNOWN: str
PROTOCOL_VIOLATION: str
TRIGGERED_ACTION_EXCEPTION: str
FEATURE_NOT_SUPPORTED: str
INVALID_TRANSACTION_INITIATION: str
LOCATOR_EXCEPTION: str
INVALID_LOCATOR_SPECIFICATION: str
INVALID_GRANTOR: str
INVALID_GRANT_OPERATION: str
INVALID_ROLE_SPECIFICATION: str
DIAGNOSTICS_EXCEPTION: str
STACKED_DIAGNOSTICS_ACCESSED_WITHOUT_ACTIVE_HANDLER: str
CASE_NOT_FOUND: str
CARDINALITY_VIOLATION: str
DATA_EXCEPTION: str
STRING_DATA_RIGHT_TRUNCATION: str
NULL_VALUE_NO_INDICATOR_PARAMETER: str
NUMERIC_VALUE_OUT_OF_RANGE: str
NULL_VALUE_NOT_ALLOWED_: str
ERROR_IN_ASSIGNMENT: str
INVALID_DATETIME_FORMAT: str
DATETIME_FIELD_OVERFLOW: str
INVALID_TIME_ZONE_DISPLACEMENT_VALUE: str
ESCAPE_CHARACTER_CONFLICT: str
INVALID_USE_OF_ESCAPE_CHARACTER: str
INVALID_ESCAPE_OCTET: str
ZERO_LENGTH_CHARACTER_STRING: str
MOST_SPECIFIC_TYPE_MISMATCH: str
SEQUENCE_GENERATOR_LIMIT_EXCEEDED: str
NOT_AN_XML_DOCUMENT: str
INVALID_XML_DOCUMENT: str
INVALID_XML_CONTENT: str
INVALID_XML_COMMENT: str
INVALID_XML_PROCESSING_INSTRUCTION: str
INVALID_INDICATOR_PARAMETER_VALUE: str
SUBSTRING_ERROR: str
DIVISION_BY_ZERO: str
INVALID_PRECEDING_OR_FOLLOWING_SIZE: str
INVALID_ARGUMENT_FOR_NTILE_FUNCTION: str
INTERVAL_FIELD_OVERFLOW: str
INVALID_ARGUMENT_FOR_NTH_VALUE_FUNCTION: str
INVALID_CHARACTER_VALUE_FOR_CAST: str
INVALID_ESCAPE_CHARACTER: str
INVALID_REGULAR_EXPRESSION: str
INVALID_ARGUMENT_FOR_LOGARITHM: str
INVALID_ARGUMENT_FOR_POWER_FUNCTION: str
INVALID_ARGUMENT_FOR_WIDTH_BUCKET_FUNCTION: str
INVALID_ROW_COUNT_IN_LIMIT_CLAUSE: str
INVALID_ROW_COUNT_IN_RESULT_OFFSET_CLAUSE: str
INVALID_LIMIT_VALUE: str
CHARACTER_NOT_IN_REPERTOIRE: str
INDICATOR_OVERFLOW: str
INVALID_PARAMETER_VALUE: str
UNTERMINATED_C_STRING: str
INVALID_ESCAPE_SEQUENCE: str
STRING_DATA_LENGTH_MISMATCH: str
TRIM_ERROR: str
ARRAY_SUBSCRIPT_ERROR: str
INVALID_TABLESAMPLE_REPEAT: str
INVALID_TABLESAMPLE_ARGUMENT: str
DUPLICATE_JSON_OBJECT_KEY_VALUE: str
INVALID_ARGUMENT_FOR_SQL_JSON_DATETIME_FUNCTION: str
INVALID_JSON_TEXT: str
INVALID_SQL_JSON_SUBSCRIPT: str
MORE_THAN_ONE_SQL_JSON_ITEM: str
NO_SQL_JSON_ITEM: str
NON_NUMERIC_SQL_JSON_ITEM: str
NON_UNIQUE_KEYS_IN_A_JSON_OBJECT: str
SINGLETON_SQL_JSON_ITEM_REQUIRED: str
SQL_JSON_ARRAY_NOT_FOUND: str
SQL_JSON_MEMBER_NOT_FOUND: str
SQL_JSON_NUMBER_NOT_FOUND: str
SQL_JSON_OBJECT_NOT_FOUND: str
TOO_MANY_JSON_ARRAY_ELEMENTS: str
TOO_MANY_JSON_OBJECT_MEMBERS: str
SQL_JSON_SCALAR_REQUIRED: str
FLOATING_POINT_EXCEPTION: str
INVALID_TEXT_REPRESENTATION: str
INVALID_BINARY_REPRESENTATION: str
BAD_COPY_FILE_FORMAT: str
UNTRANSLATABLE_CHARACTER: str
NONSTANDARD_USE_OF_ESCAPE_CHARACTER: str
INTEGRITY_CONSTRAINT_VIOLATION: str
RESTRICT_VIOLATION: str
NOT_NULL_VIOLATION: str
FOREIGN_KEY_VIOLATION: str
UNIQUE_VIOLATION: str
CHECK_VIOLATION: str
EXCLUSION_VIOLATION: str
INVALID_CURSOR_STATE: str
INVALID_TRANSACTION_STATE: str
ACTIVE_SQL_TRANSACTION: str
BRANCH_TRANSACTION_ALREADY_ACTIVE: str
INAPPROPRIATE_ACCESS_MODE_FOR_BRANCH_TRANSACTION: str
INAPPROPRIATE_ISOLATION_LEVEL_FOR_BRANCH_TRANSACTION: str
NO_ACTIVE_SQL_TRANSACTION_FOR_BRANCH_TRANSACTION: str
READ_ONLY_SQL_TRANSACTION: str
SCHEMA_AND_DATA_STATEMENT_MIXING_NOT_SUPPORTED: str
HELD_CURSOR_REQUIRES_SAME_ISOLATION_LEVEL: str
NO_ACTIVE_SQL_TRANSACTION: str
IN_FAILED_SQL_TRANSACTION: str
IDLE_IN_TRANSACTION_SESSION_TIMEOUT: str
INVALID_SQL_STATEMENT_NAME: str
TRIGGERED_DATA_CHANGE_VIOLATION: str
INVALID_AUTHORIZATION_SPECIFICATION: str
INVALID_PASSWORD: str
DEPENDENT_PRIVILEGE_DESCRIPTORS_STILL_EXIST: str
DEPENDENT_OBJECTS_STILL_EXIST: str
INVALID_TRANSACTION_TERMINATION: str
SQL_ROUTINE_EXCEPTION: str
MODIFYING_SQL_DATA_NOT_PERMITTED_: str
PROHIBITED_SQL_STATEMENT_ATTEMPTED_: str
READING_SQL_DATA_NOT_PERMITTED_: str
FUNCTION_EXECUTED_NO_RETURN_STATEMENT: str
INVALID_CURSOR_NAME: str
EXTERNAL_ROUTINE_EXCEPTION: str
CONTAINING_SQL_NOT_PERMITTED: str
MODIFYING_SQL_DATA_NOT_PERMITTED: str
PROHIBITED_SQL_STATEMENT_ATTEMPTED: str
READING_SQL_DATA_NOT_PERMITTED: str
EXTERNAL_ROUTINE_INVOCATION_EXCEPTION: str
INVALID_SQLSTATE_RETURNED: str
NULL_VALUE_NOT_ALLOWED: str
TRIGGER_PROTOCOL_VIOLATED: str
SRF_PROTOCOL_VIOLATED: str
EVENT_TRIGGER_PROTOCOL_VIOLATED: str
SAVEPOINT_EXCEPTION: str
INVALID_SAVEPOINT_SPECIFICATION: str
INVALID_CATALOG_NAME: str
INVALID_SCHEMA_NAME: str
TRANSACTION_ROLLBACK: str
SERIALIZATION_FAILURE: str
TRANSACTION_INTEGRITY_CONSTRAINT_VIOLATION: str
STATEMENT_COMPLETION_UNKNOWN: str
DEADLOCK_DETECTED: str
SYNTAX_ERROR_OR_ACCESS_RULE_VIOLATION: str
INSUFFICIENT_PRIVILEGE: str
SYNTAX_ERROR: str
INVALID_NAME: str
INVALID_COLUMN_DEFINITION: str
NAME_TOO_LONG: str
DUPLICATE_COLUMN: str
AMBIGUOUS_COLUMN: str
UNDEFINED_COLUMN: str
UNDEFINED_OBJECT: str
DUPLICATE_OBJECT: str
DUPLICATE_ALIAS: str
DUPLICATE_FUNCTION: str
AMBIGUOUS_FUNCTION: str
GROUPING_ERROR: str
DATATYPE_MISMATCH: str
WRONG_OBJECT_TYPE: str
INVALID_FOREIGN_KEY: str
CANNOT_COERCE: str
UNDEFINED_FUNCTION: str
GENERATED_ALWAYS: str
RESERVED_NAME: str
UNDEFINED_TABLE: str
UNDEFINED_PARAMETER: str
DUPLICATE_CURSOR: str
DUPLICATE_DATABASE: str
DUPLICATE_PREPARED_STATEMENT: str
DUPLICATE_SCHEMA: str
DUPLICATE_TABLE: str
AMBIGUOUS_PARAMETER: str
AMBIGUOUS_ALIAS: str
INVALID_COLUMN_REFERENCE: str
INVALID_CURSOR_DEFINITION: str
INVALID_DATABASE_DEFINITION: str
INVALID_FUNCTION_DEFINITION: str
INVALID_PREPARED_STATEMENT_DEFINITION: str
INVALID_SCHEMA_DEFINITION: str
INVALID_TABLE_DEFINITION: str
INVALID_OBJECT_DEFINITION: str
INDETERMINATE_DATATYPE: str
INVALID_RECURSION: str
WINDOWING_ERROR: str
COLLATION_MISMATCH: str
INDETERMINATE_COLLATION: str
WITH_CHECK_OPTION_VIOLATION: str
INSUFFICIENT_RESOURCES: str
DISK_FULL: str
OUT_OF_MEMORY: str
TOO_MANY_CONNECTIONS: str
CONFIGURATION_LIMIT_EXCEEDED: str
PROGRAM_LIMIT_EXCEEDED: str
STATEMENT_TOO_COMPLEX: str
TOO_MANY_COLUMNS: str
TOO_MANY_ARGUMENTS: str
OBJECT_NOT_IN_PREREQUISITE_STATE: str
OBJECT_IN_USE: str
CANT_CHANGE_RUNTIME_PARAM: str
LOCK_NOT_AVAILABLE: str
UNSAFE_NEW_ENUM_VALUE_USAGE: str
OPERATOR_INTERVENTION: str
QUERY_CANCELED: str
ADMIN_SHUTDOWN: str
CRASH_SHUTDOWN: str
CANNOT_CONNECT_NOW: str
DATABASE_DROPPED: str
SYSTEM_ERROR: str
IO_ERROR: str
UNDEFINED_FILE: str
DUPLICATE_FILE: str
SNAPSHOT_TOO_OLD: str
CONFIG_FILE_ERROR: str
LOCK_FILE_EXISTS: str
FDW_ERROR: str
FDW_OUT_OF_MEMORY: str
FDW_DYNAMIC_PARAMETER_VALUE_NEEDED: str
FDW_INVALID_DATA_TYPE: str
FDW_COLUMN_NAME_NOT_FOUND: str
FDW_INVALID_DATA_TYPE_DESCRIPTORS: str
FDW_INVALID_COLUMN_NAME: str
FDW_INVALID_COLUMN_NUMBER: str
FDW_INVALID_USE_OF_NULL_POINTER: str
FDW_INVALID_STRING_FORMAT: str
FDW_INVALID_HANDLE: str
FDW_INVALID_OPTION_INDEX: str
FDW_INVALID_OPTION_NAME: str
FDW_OPTION_NAME_NOT_FOUND: str
FDW_REPLY_HANDLE: str
FDW_UNABLE_TO_CREATE_EXECUTION: str
FDW_UNABLE_TO_CREATE_REPLY: str
FDW_UNABLE_TO_ESTABLISH_CONNECTION: str
FDW_NO_SCHEMAS: str
FDW_SCHEMA_NOT_FOUND: str
FDW_TABLE_NOT_FOUND: str
FDW_FUNCTION_SEQUENCE_ERROR: str
FDW_TOO_MANY_HANDLES: str
FDW_INCONSISTENT_DESCRIPTOR_INFORMATION: str
FDW_INVALID_ATTRIBUTE_VALUE: str
FDW_INVALID_STRING_LENGTH_OR_BUFFER_LENGTH: str
FDW_INVALID_DESCRIPTOR_FIELD_IDENTIFIER: str
PLPGSQL_ERROR: str
RAISE_EXCEPTION: str
NO_DATA_FOUND: str
TOO_MANY_ROWS: str
ASSERT_FAILURE: str
INTERNAL_ERROR: str
DATA_CORRUPTED: str
INDEX_CORRUPTED: str
IDLE_SESSION_TIMEOUT: str
SQL_JSON_ITEM_CANNOT_BE_CAST_TO_TARGET_TYPE: str
