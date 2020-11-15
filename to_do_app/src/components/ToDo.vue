<template>
    <div class="to_do">
        <h1>{{ msg }}</h1>
        <form method="POST">
        <input v-model="todo" placeholder="Whatchyah wanna do"/>
        <input type="submit" value="New Todo">
        </form>
        <h2>Your To Do's</h2>
        <p>This todo is: {{ todo }}</p>
    </div>
</template> 

<script>
// import create_todo from "../views/todos/create.py"
export default {
    name: 'ToDo',
    data () {
        return {
            msg: 'This is VueToDo',
            todo: "",
        }
    },
    // methods: {
    //     create_todo
    // },
}
</script>