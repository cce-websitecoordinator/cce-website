# Imports classes from Locust
from locust import HttpUser, task, between

class HelloWorldUser(HttpUser): 
    @task 
    def Home_page(self):
        self.client.get("/") 

    @task
    def dep_about_page(self):
        self.client.get('/department/CSE/about')