from fastapi import FastAPI
from graphene import ObjectType, List, String, Schema,Field 
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp
from schemas import CourseType
import json

class Query(ObjectType):
  course_list = None
  get_course = Field(List(CourseType), id=String())
  async def resolve_get_course(self, info, id=None):
    with open("./courses.json") as courses:
      course_list = json.load(courses)
    if (id):
      for course in course_list:
        if course['id'] == id: return [course]
    return course_list
    
app = FastAPI()
app.add_route("/", GraphQLApp(schema=Schema(query=Query),executor_class=AsyncioExecutor))

print("FastAPi server is enabled")