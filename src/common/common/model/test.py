from dataclasses import dataclass
from typing import Optional
from uuid import uuid4 as uuid

COLLECTION_NAME = 'test'

@dataclass
class BaseTestData:
    '''Base attributes of Test type'''
    pass


@dataclass
class TestData(BaseTestData):
    '''Test data'''
    id: Optional[str] = None

@dataclass
class TestItemKeys:
    '''Test DDB item keys'''
    pk: str
    sk: str

    def get_data(self):
        return { k:v for (k, v) in self.__dict__.items() if k not in TestItemKeys.__dict__.keys() }

@dataclass
class TestItem(TestData, TestItemKeys):
    '''Test DDB item'''
    id: str

    def get_data(self):
        return { k:v for (k, v) in self.__dict__.items() if k not in ['sk', 'pk'] }

def create_keys() -> TestItemKeys:
    '''Create keys for DDB'''
    key = '{}#{}'.format(COLLECTION_NAME, str(uuid()))
    return TestItemKeys(**{'pk': key, 'sk': key})

def get_keys_from_id(_id: str) -> TestItemKeys:
    '''Get keys for DDB'''
    key = '{}#{}'.format(COLLECTION_NAME, _id)
    return TestItemKeys(**{'pk': key, 'sk': key})

def get_id_from_keys(keys: TestItemKeys) -> str:
    '''Get id from keys'''
    return keys.pk.split('#')[1]