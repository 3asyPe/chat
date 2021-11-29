<template>
    <div class="chat">
        <messages :messages="messages"></messages>
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
    data(){
        return {
            connection: null,
            messages: []
        }
    },
    created() {
        console.log("Starting connection to WebSocket Server")
        let client_id = Date.now()
        this.connection = new WebSocket(`ws://localhost:8000/ws/${client_id}`)

        this.connection.onmessage = (event) => {
            let data = JSON.parse(event.data)
            let message = {
                message: data.message,
                owner: null,
            }
            if (data.client_id == client_id){
                message.owner = "me"
            } else {
                message.owner = data.client_id
            }
            console.log(client_id)
            console.log(message)
            this.messages.push(message)
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