<template>
<div class="messages">
  <message :msg="'test message 1'"></message>
  <message :msg="'test message 2'"></message>
  <message :msg="'test message 3'"></message>
</div>
</template>

<script>
import Message from "./Message.vue"

export default {
    name: "messages",
    components: {
        Message,
    }
}
</script>

<style scoped>

.messages{
    padding: 0;
    height: 90%;
    width: 100%;
}

</style>