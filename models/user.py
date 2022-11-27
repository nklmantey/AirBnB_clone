#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 06:30:09 2022

@author: Nelson Otieno
         Nana Kofi Mantey
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel

    Attributes:
        email (str): Public class attribute for User's email
        password (str): Public class attribute for User's password
        first_name (str): Public class attribute for User's first name
        last_name (str): Public class attribute for User's last name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """init method for User class

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
