<template>
    <div class="to_do">
        <h1>{{ msg }}</h1>
        <form method="POST">
        <input v-model="newTodo" placeholder="Whatchyah wanna do"/>
        <input type="submit" value="New Todo">
        </form>
        <h2>Your To Do's</h2>
        <li v-for="todo in todos" :key="todo.id">{{ todo.todo }}</li>
    </div>
</template> 

<script>
// import create_todo from "../views/todos/create.py"
export default {
    name: 'ToDo',
    data () {
        return {
            msg: 'This is VueToDo',
            newTodo: "",
            todos: [
                {
                    id: 1,
                    todo: "wash the car",
                    complete: false
                },
                {
                    id: 2,
                    todo: "walk the dog",
                    complete: false
                },
                {
                    id: 3,
                    todo: "wax the floors",
                    complete: false
                }
                ]
        }
    },
     methods: {
         createTodo(todo) {
             
         }
     },
}
</script>