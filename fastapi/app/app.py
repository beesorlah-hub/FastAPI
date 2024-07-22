from fastapi import FastAPI
app = FastAPI()

# minimal app - get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return{"ping": "pong"}





# Get --> Read Todo
@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return{"data" : todos}


# Post --> Create Todo
@app.post('/todo', tags=['todos'])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return{
        "data": "A todo has been added !"
    }

# Post --> Create Todo
@app.put('/todo/{id}', tags=['todos'])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] = body['Activity']
            return{
                "data": f"Todo with {id} has been updated"
            }
    return {
        "data":f"Todo with this id number {id} was not found !"
        }
    
# Delete --> Delete Todo
@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return {
                "data" : f"todo with {id} has been deleted"
            }
    return {
        "data": f"This todo with {id} wasn't found!"
        }


todos = [
    {"id" : "1", 
     "Activity": "Coding for 10 hrs. "},
     {
         "id" : "2",
         "Activity" : "Go to IITA with Boo of life"
     }
]