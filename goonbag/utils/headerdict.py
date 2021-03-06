from collections import MutableMapping


class HeaderDict(MutableMapping):
    '''
    Case-insensitive dict that returns keys in TitleCase.
    '''
    def __init__(self, initial=None):
        self._data = {}
        if initial:
            self.update(initial)

    def __getitem__(self, key):
        return self._data[key.lower()]

    def __setitem__(self, key, value):
        self._data[key.lower()] = value

    def __delitem__(self, key):
        del self._data[key.lower()]

    def __iter__(self):
        for key in self._data.keys():
            yield key.title()

    def __len__(self):
        return self._data.__len__()

    def __contains__(self, key):
        return self._data.__contains__(key.lower())

    def keys(self):
        return [key.title() for key in self._data.keys()]

    def items(self):
        return [(key.title(), value) for key, value in self._data.items()]

    def values(self):
        return self._data.values()

    def get(self, key, default=None):
        return self._data.get(key.lower(), default)

    # def __eq__(self):
    # def __ne__(self):
    def pop(self, key, default=None):
        return self._data.pop(key.lower(), default)

    def popitem(self):
        return self._data.popitem()

    def clear(self):
        self._data.clear()

    def update(self, other):
        if isinstance(other, dict):
            other = other.items()
        for key, value in other:
            self[key] = value

    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default
