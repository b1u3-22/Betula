<template>
  <div class="login">
    <form class="loginForm">
      <h1 class="loginFormTitle">Přihlášení</h1>
      <label class="loginFormLabel" for="username">Vaše přihlašovací jméno *</label>
      <input class="loginFormInput" type="text" id="username" name="username" placeholder="JanNovak" v-model="username">
      <label class="loginFormLabel" for="password">Váše heslo *</label>
      <input class="loginFormInput" type="password" id="password" name="password" placeholder="Vaše heslo" v-model="password">
      <div class="loginFormBottomContainer">
        <div class="loginFormWarning">* Toto pole je povinné</div>
        <ButtonAction @click="verifyUser()">Přihlásit</ButtonAction>
      </div>
    </form>
  </div>
</template>
<script>
import ButtonAction from '@/components/ButtonAction.vue';
import axios from 'axios';
// @ is an alias to /src

export default {
  name: 'LoginView',
  components: {
    ButtonAction
  },
  data: function() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    verifyUser: function(){
     axios
      .post("http://127.0.0.1:5000/verifyUser", {"username": this.username, "password": this.password})
      .then((response) => {
        if (!response.data.verified){
          this.$notify({
            type: "warn",
            title: "Přihlášení se nezdařilo",
            text: "Špatné přihlašovací jméno nebo heslo"
          })
        }

        else {
          this.$notify({
            type: "success",
            title: "Přihlášení úspěšné",
            text: "Přihlásili jste se do systému"
          })
          this.$emit('verifiedFromLogin', this.username)
          this.$router.push("/dashboard")
        }
      })
    }
  }
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');
@import "@/assets/colors.scss";


.login {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;
  min-height: 79vh;
  overflow-x: hidden;

  .loginForm {
    display: flex;
    flex-flow: column nowrap;
    align-items: flex-start;
    justify-content: flex-end;
    max-width: 600px;
    width: 80%;
    margin: 48px 0 0 0;
    box-shadow: 10px 10px 40px #D8D8D8;
    padding: 55px;

    .loginFormTitle {
      font-weight: 700;
      color: $background-dark;
      font-size: 2.2rem;
      margin: 0 0 25px 0;
    }

    .loginFormLabel {
      font-weight: 700;
      font-size: 0.75rem;
      color: $primary;
      margin: 0 0 10px 0;
    }

      .loginFormInput {
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

    .loginFormBottomContainer {
      display: flex;
      flex-flow: column nowrap;
      justify-content: flex-end;
      align-items: flex-end;
      width: 100%;

      .loginFormWarning {
        color: $primary;
        font-weight: 400;
        font-size: 0.625rem;
        margin: 0 0 15px 0;
      }
    }
  }
}

@media (max-width: 600px){
  .loginForm {
    max-width: 80%;
  }
}


</style>