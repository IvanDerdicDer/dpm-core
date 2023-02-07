class InvalidDatabaseObjectException(Exception):
    """
    This exception is raised when given arguments for the DatabaseObject class can't be used to create a valid object.
    """
    pass


class IncorrectPermissionException(Exception):
    """
    This exception is raised when granting or revoking a permission.
    """
    pass
