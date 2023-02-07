from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from abc import ABC, abstractmethod
from source.dpm_core_exceptions import InvalidDatabaseObjectException
from enum import Enum


class UserType(Enum):
    BASIC: str = 'basic'


@dataclass_json()
@dataclass()
class DatabaseObject(ABC):
    database: str = field(default='')
    schema: str = field(default='')
    table: str = field(default='')

    def _is_valid(
            self
    ) -> None:
        """
        This method checks if the given arguments can create a valid object.
        If they can not the InvalidDatabaseObjectException is raised.
        :return:
        """
        # No arguments were given
        if not (self.database or self.schema or self.table):
            raise InvalidDatabaseObjectException(
                "No arguments were given"
            )

        # Schema was not given when database, and table were
        if self.database and self.table and not self.schema:
            raise InvalidDatabaseObjectException(
                f"Schema argument was not given when database, "
                f"and table arguments were given:\n"
                f"\tdatabase > {self.database}\n"
                f"\ttable > {self.table}"
            )

    def __post_init__(self):
        self._is_valid()

    def _object(
            self
    ) -> str:
        """
        Method that builds a valid database object string.
        This is a basic implementation that will probably need to be overwritten.
        :return:
        """
        to_return = ''

        if self.database:
            to_return += self.database + '.'

        if self.schema:
            to_return += self.schema + '.'

        if self.table:
            to_return += self.table + '.'

        to_return = to_return[:-1]

        return to_return

    @abstractmethod
    def exists(
            self
    ) -> bool:
        """
        Checks if the object.
        :return:
        """
        pass


@dataclass_json()
@dataclass()
class Role(ABC):
    name: str

    @abstractmethod
    def exists(
            self
    ) -> bool:
        """
        Method that checks if the role exists in the database.
        :return:
        """
        pass

    @abstractmethod
    def create(
            self
    ) -> bool:
        """
        Method that creates the role in the database.
        :return:
        """
        pass

    @abstractmethod
    def delete(
            self
    ) -> bool:
        """
        Method that deletes the role from the database.
        :return:
        """
        pass


@dataclass_json()
@dataclass()
class User(ABC):
    name: str
    type: UserType = field(default=UserType.BASIC)
    roles: list[Role | str] = field(default_factory=list)

    @abstractmethod
    def _add_to_roles(
            self
    ) -> None:
        """
        Method that adds the user to its roles.
        :return:
        """
        pass

    def __post_init__(
            self
    ) -> None:
        self._add_to_roles()

    @abstractmethod
    def exists(
            self
    ) -> bool:
        """
        Method that checks if the user exists in the database.
        :return:
        """
        pass

    @abstractmethod
    def create(
            self
    ) -> bool:
        """
        Method that creates the user in the database.
        :return:
        """
        pass

    @abstractmethod
    def delete(
            self
    ) -> bool:
        """
        Method that deletes the user from the database.
        :return:
        """
        pass


@dataclass_json()
@dataclass()
class Permission(ABC):
    grant: str
    to: Role | User | str
    on: DatabaseObject | str

    @abstractmethod
    def exists(
            self
    ) -> bool:
        """
        Method that checks if the permission exists in the database.
        :return:
        """
        pass

    @abstractmethod
    def grant(
            self
    ) -> None:
        """
        Method that grants the permission to the user/role on the database object
        :return:
        """
        pass

    @abstractmethod
    def revoke(
            self
    ) -> None:
        """
        Method that revokes the permission from the user/role.
        :return:
        """
        pass
