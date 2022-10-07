<template>
    <div class="addpost">
        <div class="addpostSaveButtonContainer" @click="savePost">
            <img :src="require('@/assets/icons/save.svg')" class="addpostSaveButtonIcon" />
            <div class="addpostSaveButtonText">Uložit příspěvek</div>
        </div>
        <div class="addpostTextContainer">
            <div class="addpostHeader">
                <label class="addpostLabel" for="postTitle">Nadpis příspěvku</label>
                <input type="text" name="postTitle" ref="postTitle" id="postTitle" v-model="postTitle" placeholder="Oznámení" class="addpostInput addpostInputTall">
            </div>
            <div class="addpostParagraph">
                <label class="addpostLabel" for="postText">Text příspěvku</label>
                <textarea type="text" name="postText" id="postText" v-model="postText" placeholder="Text vašeho oznámení nebo příspěvku" class="addpostInput addpostInputLong"/>
            </div>
        </div>
    </div>
  </template>
  <script>
  // @ is an alias to /src
  import axios from 'axios';
import { getCurrentInstance } from 'vue'
  
  export default {
    name: 'NewPostView',
    components: {

    },
    data: function() {
      return {
        postTitle: "",
        postText: ""
      }
    },
    methods: {
        savePost: function() {
            if (this.postTitle === ""){
                this.$notify({
                    type: "warn",
                    title: "Chybějící údaje",
                    text: "Příspěvek musí mít nadpis"
                })
                this.$refs.postTitle.focus();
            }
            else {
                axios.post("127.0.0.1:5000/newPost", {postTitle: this.postTitle, postText: this.postText})
                .then(() => {
                    this.$notify({
                        type: "success",
                        title: "Uloženo",
                        text: "Příspěvek byl uložen"
                    })
                })
                .catch(() => {
                        this.$notify({
                        type: "error",
                        title: "Něco se pokazilo",
                        text: "Nepodařilo se uložit příspěvek"
                    })
                })
            }
        }
    },
    mounted: function() {

    },
    created: function() {
        if (!getCurrentInstance().parent.ctx.$parent.verified){
            this.$router.push("/login")
        }
        else if (!getCurrentInstance().parent.ctx.$parent.permissions){
            this.$router.push("/dashboard")
        }
    }
  }
  </script>
  
  <style scoped lang="scss">
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
  @import "@/assets/colors.scss";
  

  .addpost {
    padding: 90px 0 0 0;
    min-height: 74vh;
    margin: 0;
    overflow-x: hidden;
    display: flex;
    flex-flow: column nowrap;
    justify-content: flex-start;
    align-items: center;

    .addpostSaveButtonContainer {
        position: fixed;
        bottom: 5px;
        left: 5px;
        height: 50px;
        background-color: $primary;
        display: flex;
        flex-flow: row nowrap;
        padding: 15px;
        justify-content: center;
        align-items: center;
        box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.25);
        z-index: 999999;
        box-sizing: border-box;
        cursor: pointer;

        //.addpostSaveButtonIcon {
        //    height: 50px;
        //}

        .addpostSaveButtonText {
            font-weight: 700;
            color: $background-light;
            margin-left: 5px;
            font-size: 1.2rem;
        }
    }

    .addpostTextContainer {
        width: 80%;
        box-shadow: 10px 10px 40px #D8D8D8;
        padding: 3% 5%;
        display: flex;
        flex-flow: column nowrap;
        align-items: flex-start;
        justify-content: flex-start;

        .addpostHeader {
            display: flex;
            flex-flow: column nowrap;
            align-items: flex-start;
            justify-content: flex-start;
            width: 100%;
        }

        .addpostParagraph {
            display: flex;
            flex-flow: column nowrap;
            align-items: flex-start;
            justify-content: flex-start;
            width: 100%;
        }
    }
  }

  .addpostLabel {
    font-weight: 700;
    color: $primary
  }

  .addpostInput {
    border: none;
    border-bottom: solid 2px $background-dark;
    background-color: $background-light;
    width: 100%;
    color: $background-dark;
    font-size: 1.125rem;
    font-weight: 500;
    margin: 0 0 22px 0;
    transition: all 220ms ease-in-out;
    font-family: 'Montserrat', sans-serif;
    resize: none;
    

    &:focus {
        outline: none;
        border-color: $primary;
    }

    &::placeholder {
        color: #A7A7A7;
        font-weight: 400;
    }
  }

  .addpostInputTall {
    font-size: 3rem;
    font-weight: 600;

    &::placeholder {
        color: #A7A7A7;
        font-weight: 600;
    }
  }

  .addpostInputLong {
    resize: vertical;
    height: 700px;
    max-height: 30vh;
  }
  
  @media (max-width: 600px){
    .addpost {
        .addpostTextContainer {
            width: 100%;
            box-sizing: border-box;
        }

        .addpostSaveButtonContainer {
            border-radius: 50%;

            .addpostSaveButtonText {
                display: none;
                visibility: collapse;
            }
        }
    }
    
  }
  
  
  </style>