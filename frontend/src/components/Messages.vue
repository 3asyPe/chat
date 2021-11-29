<template>
<div class="messages">
    <message 
        :key="index" 
        v-for="(msg, index) in messages" 
        :msg="msg.message"
        :owned="msg.owner == 'me'"
        >
    </message>
</div>
</template>

<script>
import Message from "./Message.vue"

export default {
    name: "messages",
    props: {
        messages: Array,
    },
    components: {
        Message,
    },
}
</script>

<style scoped>

.messages{
    padding: 0;
    height: 90%;
    width: 100%;
}

</style>