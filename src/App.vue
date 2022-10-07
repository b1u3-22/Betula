<template>
  <notifications classes="notifications" position="bottom right" />
  <nav class="desktopNav">
    <template v-if="typeOfNav === 'home'">
      <router-link to="/" class="nav-item">
        Domů
        <div class="nav-line" />
      </router-link>
      <router-link to="/home-gallery" class="nav-item">
        Galerie
        <div class="nav-line" />
      </router-link>
      <router-link to="/home-contact" class="nav-item">
        Kontakt
        <div class="nav-line" />
      </router-link> 
      <router-link v-if="!verified" to="/login" class="nav-item">
        Přihlášení
        <div class="nav-line" />
      </router-link>
      <router-link v-if="verified" to="/dashboard" class="nav-item">
        Systém
        <div class="nav-line" />
      </router-link>
    </template>
    <template v-if="typeOfNav === 'dashboard'">
      <router-link to="/" class="nav-item">
        Domů
        <div class="nav-line" />
      </router-link>
      <div class="nav-item" @click="scrollToTop()">
        Zpět nahoru
        <div class="nav-line" />
      </div>
      <div class="nav-item" @click="signOut(true)">
        Odhlášení
        <div class="nav-line" />
      </div>
      <router-link v-if="verified && permissions" to="/settings-general" class="nav-item">
        Nastavení
        <div class="nav-line" />
      </router-link>
      <router-link v-if="verified && permissions" to="/add-post" class="nav-item">
        Přidat příspěvek
        <div class="nav-line" />
      </router-link>
    </template>
    <template v-if="typeOfNav === 'settings'">
      <router-link to="/settings-general" class="nav-item">
        Obecné
        <div class="nav-line" />
      </router-link>
      <router-link to="/settings-finance" class="nav-item">
        Finance
        <div class="nav-line" />
      </router-link>
      <router-link to="/settings-users" class="nav-item">
        Uživatelé
        <div class="nav-line" />
      </router-link>
      <router-link to="/dashboard" class="nav-item">
        Zpět
        <div class="nav-line" />
      </router-link>
    </template>
    <template v-if="typeOfNav === 'addpost'">
      <router-link to="dashboard" class="nav-item">
        Zpět
        <div class="nav-line" />
      </router-link>
    </template>
  </nav>
  <nav class="mobileNav">
    <div class="mobileNavHeader">
      <div class="mobileNavTitle">Menu</div>
      <div class="mobileNavHamburgerContainer" @click="toggleMobileNav">
        <div class="mobileNavHamburgerLine" :class="{mobileNavHamburgerLineTop: mobileNavActive}" />
        <div class="mobileNavHamburgerLine" :class="{mobileNavHamburgerLineMiddle: mobileNavActive}"/>
        <div class="mobileNavHamburgerLine" :class="{mobileNavHamburgerLineBot: mobileNavActive}"/>
      </div>
    </div>
    <div class="mobileNavItems" :class="{mobileNavItemsVisible: mobileNavActive}">
      <template v-if="typeOfNav === 'home'">
        <router-link to="/" class="nav-item">
          Domů
          <div class="nav-line" />
        </router-link>
        <router-link to="/home-gallery" class="nav-item">
          Galerie
          <div class="nav-line" />
        </router-link>
        <router-link to="/home-contact" class="nav-item">
          Kontakt
          <div class="nav-line" />
        </router-link> 
        <router-link v-if="!verified" to="/login" class="nav-item">
          Přihlášení
          <div class="nav-line" />
        </router-link>
        <router-link v-if="verified" to="/dashboard" class="nav-item">
          Systém
          <div class="nav-line" />
        </router-link>
      </template>
      <template v-if="typeOfNav === 'dashboard'">
        <router-link to="/" class="nav-item">
          Domů
          <div class="nav-line" />
        </router-link>
        <div class="nav-item" @click="scrollToTop()">
          Zpět nahoru
          <div class="nav-line" />
        </div>
        <div class="nav-item" @click="signOut(true)">
          Odhlášení
          <div class="nav-line" />
        </div>
        <router-link v-if="verified && permissions" to="/settings-general" class="nav-item">
          Nastavení
          <div class="nav-line" />
        </router-link>
        <router-link v-if="verified && permissions" to="/add-post" class="nav-item">
          Přidat příspěvek
          <div class="nav-line" />
        </router-link>
      </template>
      <template v-if="typeOfNav === 'settings'">
        <router-link to="/settings-general" class="nav-item">
          Obecné
          <div class="nav-line" />
        </router-link>
        <router-link to="/settings-finance" class="nav-item">
          Finance
          <div class="nav-line" />
        </router-link>
        <router-link to="/settings-users" class="nav-item">
          Uživatelé
          <div class="nav-line" />
        </router-link>
        <router-link to="/dashboard" class="nav-item">
          Zpět
          <div class="nav-line" />
        </router-link>
      </template>
      <template v-if="typeOfNav === 'addpost'">
        <router-link to="dashboard" class="nav-item">
          Zpět
          <div class="nav-line" />
        </router-link>
      </template>
    </div>
  </nav>

  <router-view 
    @verifiedFromLogin="(username) => verifiedFromLogin(username)"
    />

  <footer>
    <div class="footerTextContainer">
      <div class="footerMenuContainer">
        <h4 class="footerTitle">Menu</h4>
        <a href="/" class="footerItem">Domů</a>
        <a href="/gallery" class="footerItem">Galerie</a>
        <a href="/home-contact" class="footerItem">Kontakty</a>
        <a href="/dashboard" class="footerItem">Systém</a>
      </div>
      <div class="footerMenuContainer">
        <h4 class="footerTitle">Kontakt</h4>
        <p class="footerItem">{{ generalInfo.address }}</p>
        <p class="footerItem">{{ generalInfo.mobile_phone_0 }}</p>
        <p class="footerItem">{{ generalInfo.mobile_phone_1 }}</p>
        <p class="footerItem">{{ generalInfo.email_0 }}</p>
      </div>
    </div>
    <div class="footerCopyright">© Jiří Sedlák {{ new Date().getFullYear() }}</div>
  </footer>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  components: {
    
  },
  props: [
    
  ],

  methods: {
    scrollToTop: function() {
      window.scrollTo({top: 0, behavior: 'smooth'});
    },
    verifiedFromLogin: function(username){
      this.verified = true;
      this.username = username
      axios
        .post("http://127.0.0.1:5000/getUserPermissions", {"username": this.username})
        .then((response) => {
          if (response.data.permissions === "admin"){
            this.permissions = true;
          }
          else {
            this.permissions = false;
          }
        })
    },
    signOut: function(redirect) {
      this.verified = false;
      if (redirect){
        this.$router.push("/")
      }
      this.$notify({
        type: "success",
        title: "Odhlášení úspěšné",
        text: "Odhlásili jste se ze systému"
      })
    },
    toggleMobileNav: function() {
      this.mobileNavActive = !this.mobileNavActive
    }
  },

  data: function () {
      return {
        typeOfNav: "home",
        generalInfo: {},
        verified: false,
        permissions: false,
        username: "",
        routerViewKey: 0, 
        mobileNavActive: false
      }
  },

  created: function() {
    axios
      .get("http://127.0.0.1:5000/getGeneralInfo")
      .then((response) => {
        for (const [key, value] of Object.entries(response.data)){
          this.generalInfo[key] = value.text
        }
      });
  },

  mounted: function() {
    let path = this.$route.path.replace('/', '');
    if (path.includes('dashboard')){
        this.atDashboard = true;
    }
    else {
      this.atDashboard = false;
    }
  },

  watch: {
    $route: function(to){
      if (this.mobileNavActive){
        this.mobileNavActive = !this.mobileNavActive
      }

      let path = to.path.replace('/', '');
      path === '' ? path = 'home' : '';
      if (path.includes("dashboard")){
        this.typeOfNav = "dashboard"
      }
      else if (path.includes("home")){
        this.typeOfNav = "home"
      }
      else if (path.includes("settings")){
        this.typeOfNav = "settings"
      }
      else if (path.includes("add-post")){
        this.typeOfNav = "addpost"
      }
    }
  }
}

</script>

<style lang="scss">

@import "@/assets/colors.scss";
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');

html {
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch;
  font-size: 16px;
}

body {
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Montserrat', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  background-color: $background-light;
}

.notifications {
  margin: 0 5px 5px;
  padding: 15px;
  color: #ffffff;
  background: $primary;

  .notification-title {
    font-size: 1.2rem;
    font-weight: 600;
  }

  .notification-content {
    font-size: 1rem;
    font-weight: 400;
  }

  // types (green, amber, red)
  &.success {
    background: #68cd86;
  }

  &.warn {
    background: #ffb648;
  }

  &.error {
    background: #e54d42;
  }
}

.desktopNav {
  padding: 15px;
  position: fixed;
  top: 0;
  width: 100vw;
  display: flex;
  flex-flow: row nowrap;
  justify-content: center;
  align-items: flex-start;
  background-color: $background-dark;
  box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.25);
  z-index: 999999;
}

.mobileNav {
  width: 100vw;
  display: none;
  visibility: hidden;
  flex-flow: column nowrap;
  justify-content:  flex-start;
  align-items: flex-start;
  position: fixed;
  background-color: $background-dark;
  z-index: 999999;

  .mobileNavHeader {
    width: 100%;
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    box-sizing: border-box;
    height: 56px;

    .mobileNavTitle {
      color: $background-light;
      font-weight: 600;
      font-size: 1.5rem;
    }

    .mobileNavHamburgerContainer {
      display: flex;
      flex-flow: column nowrap;
      align-items: center;
      justify-content: center;

      .mobileNavHamburgerLine {
        width: 34px;
        height: 4px;
        border-radius: 4px;
        background-color: $background-light;
        margin: 4px 0;
        transition: all 220ms ease-in-out;
      }

      .mobileNavHamburgerLineTop {
        margin-bottom: -4px;
        transform: rotate(45deg);
      }

      .mobileNavHamburgerLineMiddle {
        margin: 0;
        opacity: 0;
      }

      .mobileNavHamburgerLineBot {
        margin-top: -4px;
        transform: rotate(-45deg);
      }
    }
  }

  .mobileNavItems {
    display: none;
    visibility: collapse;
    flex-flow: column nowrap;
    align-items: center;
    justify-content: center;
    width: 100%;
    margin: 0 0 15px 0;

    .nav-item {
      font-size: 1.7rem;
      margin: 5px 0;
    }
  }

  .mobileNavItemsVisible {
    display: flex;
    visibility: visible;
    animation: mobileNavSlideDown 220ms ease-in-out forwards;
  }
}

.router-link-exact-active {
  .nav-line {
    width: 100% !important;
  }
}

.nav-item {
font-weight: 600;
font-size: 1.125rem;
display: flex;
flex-flow: column nowrap;
align-items: flex-end;
justify-content: flex-start;
width: fit-content;
text-decoration: none;
color: $background-light;
margin: 0 2%;
cursor: pointer;

  .nav-line {
    display: inline;
    width: 0%;
    height: 3px;
    background-color: $primary;
    transition: all 200ms ease-in-out;
  }

  &:hover {
    align-items: flex-start;
  }

  &:hover > .nav-line{
    width: 100%;

  }

  .router-link-exact-active {
    color: $primary
  }

}

footer {
  background-color: #F1F1F1;
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-end;
  align-items: stretch;
  padding: 2% 3% 1% 3%;

  .footerTextContainer {
    display: flex;
    flex-flow: row nowrap;
    align-items: flex-start;
    justify-content: flex-start;

    .footerMenuContainer {
      display: flex;
      flex-flow: column nowrap;
      justify-content: flex-start;
      align-items: flex-start;
      margin: 0 10% 0 0;

      .footerTitle {
        margin: 0;
        padding: 0;
        font-size: 1.125rem;
        font-weight: 700;
      }

      .footerItem {
        margin: 3px 0;
        padding: 0;
        font-size: 1rem;
        font-weight: 400;
        cursor: pointer;
        text-decoration: none;
        color: black;
      }
    }
  }
}

@keyframes mobileNavSlideDown {
  from {
    opacity: 0;
    //transform: translateY(-50px);
    max-height: 0;
  }

  to {
    opacity: 1;
    //transform: translateY(0);
    max-height: 200px;
  }
}

@media (max-width: 1000px) {
  html {
    font-size: 12px;
  }
}

@media (max-width: 700px) {
  html {
    font-size: 8px;
  }
}

@media (max-width: 600px) {
  html {
    font-size: 14px;
  }

  .desktopNav {
    display: none;
    visibility: collapse;
  }

  .mobileNav {
    display: flex;
    visibility: visible;
  }

  footer {
    padding: 4% 6% 2% 6%;

    .footerTextContainer {
      margin-bottom: 22px;
    }
  }
}


</style>
