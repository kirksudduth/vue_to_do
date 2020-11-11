<template>
    <div class="to_do">
        <h1>{{ msg }}</h1>
        <input type="text"/>
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