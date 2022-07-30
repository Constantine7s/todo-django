from pydoc import describe
from pyexpat import model
from re import T
from sqlite3 import complete_statement
from this import d
from tkinter import CASCADE
from turtle import title
from venv import create
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)