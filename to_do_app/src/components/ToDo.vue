<template>
    <div class="to_do">
        <h1>{{ msg }}</h1>
        <form method="POST">
        <input type="text" placeholder="Whatchyah wanna do"/>
        <input type="submit" value="New Todo">
        </form>
        <h2>Your To Do's</h2>
    </div>
</template> 

<script>
export default {
    name: 'ToDo',
    data () {
        return {
            msg: 'This is VueToDo'
        }
    }
}
</script>