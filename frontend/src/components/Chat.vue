<template>
    <div class="chat">
        <messages></messages>
        <chat-input v-on:sendMsg="sendMessage"></chat-input>
    </div>
</template>

<script>
import ChatInput from "./ChatInput.vue"
import Messages from "./Messages.vue"

export default {
    name: "chat",
    components: {
        ChatInput,
        Messages,
    },
    created() {
        console.log("Starting connection to WebSocket Server")
        let client_id = Date.now()
        this.connection = new WebSocket(`ws://localhost:8000/ws/${client_id}`)

        this.connection.onmessage = function(event) {
            console.log(event);
        }

        this.connection.onopen = function(event) {
            console.log(event)
            console.log("Successfully connected to the echo websocket server...")
        }

    },
    methods: {
        sendMessage(event){
            console.log("sendMessage")
            this.connection.send(event)
        }
    }
}
</script>

<style>

.chat{
  height: 400px;
  width: 300px;
  background-color: rgb(241, 193, 193);
  border: solid black 2px;
  border-radius: 5px;
  padding: 0;
}

</style>