#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery
import os


app = Celery('tasks', broker='pyamqp://guest@rabbitmq:5673//')


@app.task
def process_file(file_path):
    file_path = f"/code/uploads/{file_path}"
    if file_path.endswith('.txt'):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            processed_content = content.upper()
            new_file_path = file_path.replace('.txt', '_processed.txt')
            with open(new_file_path, 'w') as file:
                file.write(processed_content)
            print(f"Processed file saved at: {new_file_path}")
        except Exception as e:
            print(f"Failed to process file: {e}")
    else:
        print("Unsupported file type")
