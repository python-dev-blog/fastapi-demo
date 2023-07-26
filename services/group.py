from models import Group
from schemas.inputs import GroupCreate


class GroupService:

    def __init__(self, db):
        self.__db = db

    def create_group(self, group: GroupCreate):
        group_db = Group(name=group.name, description=group.description)
        self.__db.add(group_db)
        self.__db.commit()
        self.__db.refresh(group_db)
        return group_db
