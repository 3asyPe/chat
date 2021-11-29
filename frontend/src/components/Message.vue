<template>

<div class="message">
  <div class="msg">{{ msg }}</div>
</div>

</template>

<script>
export default {
    name: "message",
    props: {
        msg: {
            type: String,
            default: "",
        }
    },
}
</script>

<style>
.message{
    display: block;
    border: solid black 1px;
    border-radius: 5px;
    padding: 5px 3px;
    margin: 10px 5px;
}

</style>