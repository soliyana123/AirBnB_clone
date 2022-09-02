#!/usr/bin/python3
"""
Class base model
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
   def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
