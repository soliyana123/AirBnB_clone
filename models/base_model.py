#!/usr/bin/python3
"""
Class base model
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    def __init__(self, *args, **kwargs):
        """ initialization """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    setattr(self, key, type(self))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)



    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    
    def save(self):
        """
        save method  updates the public instance attribute updated_at
        with the current datetim
        """
        self.updated_at = datetime.now()
        models.storage.save()



    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
