<template>

<div class="chat-input">
  <input type="text" class="c-input" placeholder="Type message" v-model="msg">
  <button class="c-send" @click="sendMessage">Send</button>
</div>

</template>

<script>
export default {
    name: "chat-input",
    props: {

    },
    data(){
        return {
            msg: "",
        }
    },
    methods: {
        sendMessage(){
            this.$emit("sendMsg", this.msg)
        }
    }
}
</script>

<style>

.chat-input{
    display: flex;
    height: 10%;
    width: 100%;
}

.c-input{
    width: 80%;
    height: 100%;
    padding: 0;
    margin: 0;
}

.c-send{
    width: 20%;
    height: 100%;
    background: transparent;
    outline: none;
    border: none;
}

</style>