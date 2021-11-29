<template>

<div class="message">
  <div class="msg" :class="{'owned': owned, 'received': !owned}">{{ msg }}</div>
</div>

</template>

<script>
export default {
    name: "message",
    props: {
        msg: {
            type: String,
            default: "",
        },
        owned: {
            type: Boolean,
            default: false
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

.owned{
    background-color: green;
}

.received{
    background-color: red;
}

</style>