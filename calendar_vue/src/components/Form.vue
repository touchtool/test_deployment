<template>
    <form>     
    <label>Name:</label>
    <input type="text" v-model="dataForm.name" required> <br>
    <router-link to="/about" tag="button">Create</router-link>

    </form>
</template>

<script>

export default {
    name: "Form",
    data(){
        return {
            dataForm:{
                name:null
            }
        }
    },
    methods: {
        getData(e){
            e.preventDefault();
            console.log(this.dataForm);
        }
        
    }

}
</script>

<style>
    form {
        max-width: 420px;
        margin: 30px auto;
        background: #E2FFF5;
        text-align: left;
        padding: 40px;
        border-radius: 10px;
    }
    label {
        color: rgb(170, 170, 170);
        display: inline-block;
        margin: 25px 0 15px;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }
    input {
        display: block;
        padding: 10px 6px;
        width: 100%;
        box-sizing: none;
        border-bottom: 1px solid #ddd;
        color: #555;
    }
    button {
        position: relative;
        background-color: #73c6b6;
        border: none;
        font-size: 15px;
        color: #FFFFFF;
        padding: 20px;
        width: 100px;
        text-align: center;
        transition-duration: 0.4s;
        text-decoration: none;
        overflow: hidden;
        cursor: pointer;
        border-radius: 10px;
    }

    button:after {
        content: "";
        border-radius: 10px;
        background: #f1f1f1;
        display: block;
        position: absolute;
        padding-top: 300%;
        padding-left: 350%;
        margin-left: -20px !important;
        margin-top: -120%;
        opacity: 0;
        transition: all 0.8s
        
    }

    button:active:after {
        padding: 0;
        margin: 0;
        opacity: 1;
        border-radius: 10px;
        transition: 0s
    }
</style>
