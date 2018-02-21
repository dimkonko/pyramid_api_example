import abc


class JsonModel(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def to_json(self):
        pass
