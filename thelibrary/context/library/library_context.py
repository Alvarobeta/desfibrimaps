from thelibrary_core.infrastructure.context_base import ContextBase


class LibraryContext(ContextBase):

    def _path(self) -> str:
        return 'thelibrary_core/context/library'
