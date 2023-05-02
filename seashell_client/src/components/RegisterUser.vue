<template>
    <div class="sign-in">
        <form @submit="onSubmit" class="sign-in-form">
            <span class="p-float-label">
                <InputText id="value" v-model="value" type="text" :class="{ 'p-invalid': errorMessage }" aria-describedby="text-error" />
                <label for="value">Name - Surname</label>
            </span>
            <small class="p-error" id="text-error">{{ errorMessage || '&nbsp;' }}</small>
            <Button type="submit" label="Submit" />
        </form>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>
.sign-in{
    display: flex;
    justify-content: center;
    height: 40em;
}

.sign-in-form{
        display: flex;
        flex-direction: column;
        gap: 2;
        padding: 2em;
    }


</style>