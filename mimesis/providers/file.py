import re
from typing import Optional

from mimesis.data import EXTENSIONS, MIME_TYPES
from mimesis.enums import FileType, MimeType
from mimesis.exceptions import NonEnumerableError
from mimesis.providers.base import BaseProvider
from mimesis.providers.text import Text


class File(BaseProvider):
    """Class for generate fake data for files."""

    def __init__(self):
        super().__init__()
        self.__text = Text('en')

    def __sub(self, string: str = '') -> str:
        """Replace spaces in string.

        :param str string: String.
        :return: String without spaces.
        """
        replacer = self.random.choice(['_', '-'])
        return re.sub('\s+', replacer, string.strip())

    def extension(self, file_type: Optional[FileType] = None) -> str:
        """Get a random file extension from list.

        :param file_type: Enum object FileType.
        :return: Extension of the file.

        :Example:
            .py
        """
        if file_type is None:
            file_type = FileType.get_random_item()

        if file_type and file_type in FileType:
            return self.random.choice(EXTENSIONS[file_type.value])
        else:
            raise NonEnumerableError('FileType')

    def mime_type(self, type_: Optional[MimeType] = None) -> str:
        """Get a random mime type from list.

        :param type_: Enum object MimeType.
        :return: Mime type.
        :raises ValueError: if type_t is not supported.
        """
        if type_ is None:
            type_ = MimeType.get_random_item()

        if type_ and type_ in MimeType:
            return self.random.choice(MIME_TYPES[type_.value])
        else:
            raise NonEnumerableError('MimeType')

    def size(self, minimum: int = 1, maximum: int = 100) -> str:
        """Get size of file.

        :param int minimum: Maximum value.
        :param int maximum: Minimum value.
        :return: Size of file.

        :Example:
            56 kB
        """
        num = self.random.randint(minimum, maximum)
        unit = self.random.choice(
            ['bytes', 'kB', 'MB', 'GB', 'TB'])

        return '{num} {unit}'.format(
            num=num,
            unit=unit,
        )

    def file_name(self, file_type: Optional[FileType] = None) -> str:
        """Get a random file name with some extension.

        :param str file_type: Enum object FileType
        :return: File name.

        :Example:
            legislative.txt
        """
        name = self.__text.word()
        ext = self.extension(file_type)

        return '{name}{ext}'.format(
            name=self.__sub(name),
            ext=ext,
        )
